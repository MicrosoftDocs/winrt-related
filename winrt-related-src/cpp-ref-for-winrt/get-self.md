---
author: stevewhims
description: A helper function which, given an object of a projected type, retrieves a pointer to the implementation.
title: winrt::get_self function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 08/29/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, projected, implementation, type
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_self function template (C++/WinRT)

> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A helper function which, given an object of a projected type, retrieves a pointer to the implementation. For more details, and code examples, see [Instantiating and returning implementation types and interfaces](/windows/uwp/cpp-and-winrt-apis/author-apis#instantiating-and-returning-implementation-types-and-interfaces).

## Syntax
```cppwinrt
template <typename D, typename I>
D* get_self(I const& from) noexcept
```

### Template parameters
`typename D`
An implementation type.

`typename I`
A projected interface type.

### Parameters
`from`
An object of a projected type, a pointer to whose implementation to retrieve.

### Return value 
A pointer to the implementation object that implements the interface object.

## Requirements
**Minimum supported SDK:** Windows 10 SDK Preview Build 17661

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
