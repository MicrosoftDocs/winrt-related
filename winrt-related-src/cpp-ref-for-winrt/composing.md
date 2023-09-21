---
description: A marker type used to indicate that the type is the outer class of a composable class.
title: winrt::composing struct (C++/WinRT)
dev_langs: ["C++"]
ms.date: 09/20/2023
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, marker, type
ms.workload: ["cplusplus"]
---

# winrt::composing marker struct (C++/WinRT)

A marker type used to indicate to the [**implements**](implements.md) base struct that the type is the outer class of a composable class. This marker type is generated automatically by cppwinrt.exe when necessary, and you should avoid using it manually. For a usage example of marker types, see [Marker types](implements.md#marker-types).

## Syntax
```cppwinrt
struct winrt::composing
```

## Remarks

If your runtime class derives from another runtime class,
you can call methods on your base class by using the `base_type` type alias.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
