---
author: stevewhims
description: A function template that creates and returns an object of a type that implements a general-purpose collection. The object is returned as an **IVector**.
title: winrt::single_threaded_vector function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 08/25/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, collection
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::single_threaded_vector function template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))

> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A function template that creates and returns an object of a type that implements a general-purpose (but not observable) collection. The object is returned as an [**IVector**](/uwp/api/windows.foundation.collections.ivector_t_), and that's the interface via which you call the returned object's functions and properties.

You can optionally pass an existing **std::vector** *rvalue* into the function&mdash;either pass a temporary object, or call **std::move** on an *lvalue*.

For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename T, typename Allocator = std::allocator<T>>
winrt::Windows::Foundation::Collections::IVector<T> single_threaded_vector(std::vector<T, Allocator>&& values = {});
```

### Template parameters
`typename T`
The type of the elements of the collection.

`typename Allocator`
The type of the allocator of the vector from which you initialize the collection, if you pass one, otherwise the default allocator.

### Parameters
`values`
An optional reference to an *rvalue* of type **std::vector** from which to initialize the elements of the collection object.

### Return value 
An [**IVector**](/uwp/api/windows.foundation.collections.ivector_t_) representing a new collection object.

## Requirements
**Minimum supported SDK:** Windows 10 SDK Preview Build 17661

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections)
