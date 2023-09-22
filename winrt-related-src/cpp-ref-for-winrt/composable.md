---
description: A marker type used to indicate that the type can be the inner class of a composable class.
title: winrt::composable struct (C++/WinRT)
dev_langs: ["C++"]
ms.date: 09/20/2023
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, marker, type
ms.workload: ["cplusplus"]
---

# winrt::composable marker struct (C++/WinRT)

A marker type used to indicate to the [**implements**](implements.md) base struct that the type can be the inner class of a composable class. This marker type is generated automatically by cppwinrt.exe when ncessary, and you should avoid using it manually. For a usage example of marker types, see [Marker types](implements.md#marker-types).

## Syntax
```cppwinrt
struct winrt::composable
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
