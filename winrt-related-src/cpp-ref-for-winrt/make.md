---
author: stevewhims
description: A factory method that returns an instance of the projected type for a runtime class when parameterized with the corresponding implementation type.
title: winrt::make function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 04/10/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, construct, instantiate, projected, projection, implementation
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::make function template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A factory method that returns an instance of the projected type for a runtime class when parameterized with the corresponding implementation type. For an explanation of the implementation type and projected type concepts, see [Implementation and projected types for a C++/WinRT runtime class](/windows/uwp/cpp-and-winrt-apis/ctors-runtimeclass-activation). For more details, code, and a walkthrough of calling **make** in practice, see [XAML; binding a control to C++/WinRT properties and collections](/windows/uwp/cpp-and-winrt-apis/binding-prop-collection#add-a-property-of-type-booksku-to-mainpage). Also see [make_self](make-self.md).

## Syntax
```cppwinrt
template <typename D, typename... Args, std::enable_if_t<!impl::has_composable<D>::value && impl::has_class_type<D>::value>* = nullptr>
auto make(Args&&... args)
```

### Template parameters
`typename D`
The implementation type for a runtime class.

### Parameters
`args`
Any constructor arguments for the constructor being invoked.

### Return value 
A newly-created instance of the projected type for the runtime class.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17133.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::make_self function template](make-self.md)
* [Implementation and projected types for a C++/WinRT runtime class](/windows/uwp/cpp-and-winrt-apis/ctors-runtimeclass-activation)
* [XAML; binding a control to C++/WinRT properties and collections](/windows/uwp/cpp-and-winrt-apis/binding-prop-collection#add-a-property-of-type-booksku-to-mainpage)
