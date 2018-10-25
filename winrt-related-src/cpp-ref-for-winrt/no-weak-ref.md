---
author: stevewhims
description: A marker type used to opt out of weak reference support.
title: winrt::array_view struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/13/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, marker, type
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::no_weak_ref marker struct (C++/WinRT)

A marker type passed to the [**implements**](implements.md) base struct to opt out of weak reference support, which is otherwise provided automatically. As a result, **implements** does not implement the [IWeakReferenceSource interface](https://msdn.microsoft.com/library/windows/desktop/hh802476). See [Strong and weak references in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/weak-references). For a usage example, see [Marker types](implements.md#marker-types).

## Syntax
```cppwinrt
struct winrt::no_weak_ref
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
