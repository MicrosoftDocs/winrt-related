---
description: A marker type used to indicate that instances of a type do not count toward the module object count.
title: winrt::no_module_lock struct (C++/WinRT)
dev_langs: ["C++"]
ms.date: 09/20/2023
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, marker, type
ms.workload: ["cplusplus"]
---

# winrt::no_module_lock marker struct (C++/WinRT)

A marker type used to indicate to the [**implements**](implements.md) base struct that instances of a type do not count toward the module object count. As a result, **implements** does not increment the module lock when an instance is constructed, nor does it decrement the module lock when an instance is destructed. For a usage example of marker types, see [Marker types](implements.md#marker-types).

## Syntax
```cppwinrt
struct winrt::no_module_lock
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
