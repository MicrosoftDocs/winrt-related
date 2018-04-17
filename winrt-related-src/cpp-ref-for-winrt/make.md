---
author: stevewhims
description: A factory method that returns an instance of a projected type or interface when parameterized with the corresponding implementation type.
title: winrt::make function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 04/13/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, construct, instantiate, projected, projection, implementation
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::make function template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A factory method that, when a C++/WinRT implementation type is provided as a type parameter, returns one of the following.

- If a corresponding projected type exists for the implementation type, then the implementation is a Windows Runtime class (runtime class) implementation. This is the case when consuming a type implemented in a component, or consuming a type from XAML UI. An instance of the projected type is returned in this case.
- If there is no projected type, then the implementation is being consumed locally. In this case, the default (projected) interface of the implementation type is returned.

For an explanation of the implementation type and projected type concepts, see [Implementation and projected types for a C++/WinRT runtime class](/windows/uwp/cpp-and-winrt-apis/ctors-runtimeclass-activation). For more details, code, and a walkthrough of calling **make** in practice, see [XAML; binding a control to C++/WinRT properties and collections](/windows/uwp/cpp-and-winrt-apis/binding-prop-collection#add-a-property-of-type-booksku-to-mainpage). Also see [make_self](make-self.md).

## Syntax
```cppwinrt
template <typename D, typename... Args, std::enable_if_t<!impl::has_composable<D>::value && !impl::has_class_type<D>::value>* = nullptr>
auto make(Args&&... args)

template <typename D, typename... Args, std::enable_if_t<!impl::has_composable<D>::value && impl::has_class_type<D>::value>* = nullptr>
auto make(Args&&... args)

template <typename D, typename... Args, std::enable_if_t<impl::has_composable<D>::value>* = nullptr>
auto make(Args&&... args)
```

### Template parameters
`typename D`
An implementation type.

### Parameters
`args`
Any constructor arguments for the constructor being invoked.

### Return value 
An instance of the projected type if the implementation is a runtime class implementation, otherwise the default interface of the implementation type.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17133.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::make_self function template](make-self.md)
* [Implementation and projected types for a C++/WinRT runtime class](/windows/uwp/cpp-and-winrt-apis/ctors-runtimeclass-activation)
* [XAML; binding a control to C++/WinRT properties and collections](/windows/uwp/cpp-and-winrt-apis/binding-prop-collection#add-a-property-of-type-booksku-to-mainpage)
