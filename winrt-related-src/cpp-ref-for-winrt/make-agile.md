---

description: A helper function that returns an [agile_ref](agile-ref.md) object, representing an agile reference to a C++/WinRT object or interface.
title: winrt::make_agile function template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/19/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, agile
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::make_agile function template (C++/WinRT)

A helper function that returns an [agile_ref](agile-ref.md) object, representing an agile reference to a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object or interface. For more info, and code examples, see [Agile objects in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/agile-objects).

## Syntax
```cppwinrt
template <typename T>
agile_ref<T> make_agile(T const& object);
```

### Template parameters
`typename T`
The type of C++/WinRT object or interface to make an agile reference to.

### Parameters
`object`
The C++/WinRT object or interface to make an agile reference to.

### Return value 
A [agile_ref](agile-ref.md) representing an agile reference to the C++/WinRT object or interface.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::agile_ref struct template](agile-ref.md)
* [Agile objects in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/agile-objects)
