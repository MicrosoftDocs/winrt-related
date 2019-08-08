---
author: stevewhims
description: MIDL 3.0 can coexist in the same source file with classic MIDLRT; this topic shows how to transition to MIDL 3.0 from MIDLRT.
title: Transition to MIDL 3.0 from classic MIDLRT
ms.author: stwhi
ms.date: 08/07/2019
ms.topic: reference
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0, 3, midl3, transition, port, from, MIDLRT
ms.localizationpriority: medium
---

# Transition to MIDL 3.0 from classic MIDLRT

MIDLRT is also known as MIDL 2.0. See [MIDL 1.0, 2.0, and 3.0](/uwp/midl-3/intro#midl-10-20-and-30).

MIDL 3.0 can coexist in the same source file with classic MIDLRT; you're not required to convert the IDL file all at once. No new compiler options are required to express that you're using MIDL 3.0. The existing `/winrt` option enables both classic MIDLRT and MIDL 3.0.

You can add MIDL 3.0 content to an existing MIDLRT type. Specifically, you can use MIDL 3.0 to define interfaces that are added to runtime class definitions authored in MIDLRT. This allows using new techniques, while not requiring a full conversion of a type or a file. Here's an example.

```idl
// Existing RTIDL interface definition.
[contract(FooContract, 1), exclusiveto(SampleClass), uuid(...)]
interface ISampleClass : IInspectable
{
    HRESULT Method1([in] boolean something, [in] HSTRING other);
}

// New MIDL 3.0 interface added; needs exclusiveto(), but not uuid().
[contract(FooContract, 2), exclusiveto(SampleClass)]
interface ISampleClass2
{
    Windows.Foundation.IAsyncOperation<String> TransformAsync(UInt32 count);
    String NameProperty { get; };
}

[contract(FooContract, 1)]
runtimeclass SampleClass
{
    [default] interface ISampleClass;
    // Reference to MIDL 3.0-defined interface.
    [contract(FooContract, 2)] interface ISampleClass2;
}
```

Adding MIDL 3.0 constructs into existing MIDLRT runtimeclass definitions produces an error like this.

```console
1>midl : error MIDL9008 : internal compiler problem - See documentation for suggestions on how to find a workaround.
errors in directory t:\compdev1\src\mincore\coreui\published\idl
t:\compdev1\src\midl : error MIDL9008 : internal compiler problem - See documentation for suggestions on how to find a workaround.
1>midl: Assertion failed: pN->NodeKind() == NODE_INTERFACE_GROUP_MEMBER, file com\rpc\midl\midlrt\front\nodeskl.cxx, line 1403
1>NMAKE : fatal error U1077: 't:\compdev1\src\tools\x86\midl.EXE' : return code '0x2330'
```

Fix this either by converting the full class to MIDL 3.0, or by the technique above that adds a new interface and adds that to the class.