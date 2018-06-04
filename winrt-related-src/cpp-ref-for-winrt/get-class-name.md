---
author: stevewhims
description: A helper function that retrieves a string containing the fully-qualified type name of a specified Windows Runtime class.
title: winrt::get_class_name function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/30/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, runtime, class, name, string
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_class_name function ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A helper function that retrieves a string containing the fully-qualified type name of the Windows Runtime class represented by an object of a given projected type.

For an explanation of the implementation type and projected type concepts, see [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis) and [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis).

## Syntax
```cppwinrt
inline winrt::hstring get_class_name(winrt::Windows::Foundation::IInspectable const& object);
```

### Parameters
`object`
An instance of the projected type for a Windows Runtime class (any runtime class; whether it's a Windows type, or a second- or third-party type).

### Return value
A [winrt::hstring](hstring.md) containing the fully-qualified type name of the Windows Runtime class represented by `object`. Note that the type of the Windows Runtime class is returned, not that of the projected type. In the example below, the C++/WinRT projected type is **winrt::Windows::Foundation::Uri**, but the value returned from **winrt::get_class_name** is "Windows.Foundation.Uri", which is the type name of the runtime class.

### Example
```cppwinrt
winrt::Windows::Foundation::Uri contosoUri{ L"http://www.contoso.com" };
winrt::hstring name = winrt::get_class_name(contosoUri);
assert(name == L"Windows.Foundation.Uri");
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis)
* [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis)
