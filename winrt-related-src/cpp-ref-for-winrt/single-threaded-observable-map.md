---

description: A function template that creates and returns an object of a type that implements an observable associative collection (map). The object is returned as an **IObservableMap**.
title: winrt::single_threaded_observable_map function template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 08/25/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, associative, observable, collection, map
ms.workload: ["cplusplus"]
---

# winrt::single_threaded_observable_map function template (C++/WinRT)

A function template that creates and returns an object of a type that implements an observable associative collection (map). The object is returned as an [**IObservableMap**](/uwp/api/windows.foundation.collections.iobservablemap_k_v_), and that's the interface via which you call the returned object's functions and properties.

You can optionally pass an existing **std::map** or **std::unordered_map** *rvalue* into the function&mdash;either pass a temporary object, or call **std::move** on an *lvalue*.

For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename K, typename V, typename Compare = std::less<K>, typename Allocator = std::allocator<std::pair<K const, V>>>
winrt::Windows::Foundation::Collections::IObservableMap<K, V> single_threaded_observable_map()

template <typename K, typename V, typename Compare = std::less<K>, typename Allocator = std::allocator<std::pair<K const, V>>>
winrt::Windows::Foundation::Collections::IObservableMap<K, V> single_threaded_observable_map(std::map<K, V, Compare, Allocator>&& values)

template <typename K, typename V, typename Hash = std::hash<K>, typename KeyEqual = std::equal_to<K>, typename Allocator = std::allocator<std::pair<K const, V>>>
winrt::Windows::Foundation::Collections::IObservableMap<K, V> single_threaded_observable_map(std::unordered_map<K, V, Hash, KeyEqual, Allocator>&& values)
```

### Template parameters
`typename K`
The type of the keys in the collection.

`typename V`
The type of the values in the collection.

`typename Compare`
The type of the comparator to use to compare keys.

`typename Allocator`
The type of the allocator of the associative container from which you initialize the collection, if you pass one, otherwise the default allocator.

### Parameters
`values`
An optional reference to an *rvalue* of type **std::map** or **std::unordered_map** from which to initialize the elements of the collection object.

### Return value 
An [**IObservableMap**](/uwp/api/windows.foundation.collections.iobservablemap_k_v_) representing a new collection object.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also
* [winrt namespace](winrt.md)
* [winrt::observable_map_base struct template](observable-map-base.md)
* [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections)
