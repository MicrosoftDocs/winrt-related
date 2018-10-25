---
author: stevewhims
description: A base class, for you to derive from, that represents a non-observable associative collection.
title: winrt::map_base struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 08/27/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, map, associative, collection
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::map_base struct template (C++/WinRT)

A base class from which you can derive to implement your own custom non-observable associative collection. For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename D, typename K, typename V>
struct map_base : map_view_base<D, K, V, impl::collection_version>
```

### Template parameters
`typename D`
Your derived type name.

`typename K`
The type of the keys in the collection.

`typename V`
The type of the values in the collection.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[map_base::Clear function](#mapbaseclear-function)|Removes all elements from the **map_base** object.|
|[map_base::First function](#mapbasefirst-function)|Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **map_base** object.|
|[map_base::GetView function](#mapbasegetview-function)|Retrieves an immutable view of the **map_base** object.|
|[map_base::HasKey function](#mapbasehaskey-function)|Determines whether the specified key belongs to an element in the **map_base** object.|
|[map_base::Insert function](#mapbaseinsert-function)|Inserts or updates an element in the **map_base** object.|
|[map_base::Lookup function](#mapbaselookup-function)|Looks up the element identified by the specified key, and retrieves the corresponding value.|
|[map_base::Remove function](#mapbaseremove-function)|Removes an element from the **map_base** object.|
|[map_base::Size function](#mapbasesize-function)|Retrieves the number of elements in the **map_base** object.|

## Iterators
A **map_base** is a range, and that range is defined by internal free functions (each of which retrieves an iterator) that are compatible with standard language features. Because of this, you can enumerate the elements in a **map_base** object with a range-based `for` statement.

You can also retrieve an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) from the [map_base::First](#mapbasefirst-function) function, and use that to iterate through the elements in a **map_base** object.

```cppwinrt
...
#include <iostream>
using namespace winrt;
using namespace Windows::Foundation::Collections;
...
struct MyMap :
    implements<MyMap, IMap<winrt::hstring, int>, IMapView<winrt::hstring, int>, IIterable<IKeyValuePair<winrt::hstring, int>>>,
    winrt::map_base<MyMap, winrt::hstring, int>
{
    auto& get_container() const noexcept
    {
        return m_values;
    }

    auto& get_container() noexcept
    {
        return m_values;
    }

private:
    std::map<winrt::hstring, int> m_values{
        { L"AliceBlue", 0xfff0f8ff }, { L"AntiqueWhite", 0xfffaebd7 }
    };
};
...
IMap<winrt::hstring, int> map{ winrt::make<MyMap>() };

for (auto const& el : map)
{
    std::wcout << el.Key().c_str() << L", " << std::hex << el.Value() << std::endl;
}

IIterator<IKeyValuePair<winrt::hstring, int>> it{ map.First() };
while (it.HasCurrent())
{
    std::wcout << it.Current().Key().c_str() << L", " << std::hex << it.Current().Value() << std::endl;
    it.MoveNext();
}
```

## map_base::Clear function
Removes all elements from the **map_base** object.

### Syntax
```cppwinrt
void Clear() noexcept;
```

## map_base::First function
Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **map_base** object.

### Syntax
```cppwinrt
auto First();
```

### Return value
An [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **map_base** object.

## map_base::GetView function
Retrieves an immutable view of the **map_base** object.

### Syntax
```cppwinrt
winrt::Windows::Foundation::Collections::IMapView<K, V> GetView() const;
```

### Return value
An [**IMapView**](/uwp/api/windows.foundation.collections.imapview_k_v_) containing an immutable view of the **map_base**.

## map_base::HasKey function
Determines whether the specified key belongs to an element in the **map_base** object.

### Syntax
```cppwinrt
bool HasKey(K const& key) const noexcept;
```

### Parameters
`key`
The key to look for.

### Return value
`true` if an element containing the key is found, otherwise `false`.

## map_base::Insert function
Inserts or updates an element in the **map_base** object.

### Syntax
```cppwinrt
bool Insert(K const& key, V const& value);
```

### Parameters
`key`
The key associated with the element to insert or update.

`value`
The value to insert or replace.

### Return value
`true` if an element with the specified key was found and updated; otherwise `false`.

## map_base::Lookup function
Looks up the element identified by the specified key, and retrieves the corresponding value.

### Syntax
```cppwinrt
V Lookup(K const& key) const;
```

### Parameters
`key`
The key to look up.

### Return value
The value corresponding to the key being looked up if found, otherwise a [winrt::hresult_out_of_bounds](error-handling/hresult-out-of-bounds.md) exception is thrown.

## map_base::Remove function
Removes an element from the **map_base** object.

### Syntax
```cppwinrt
void Remove(K const& key);
```

### Parameters
`key`
The key associated with the element to remove.

## map_base::Size function
Retrieves the number of elements in the **map_base** object.

### Syntax
```cppwinrt
uint32_t Size() const noexcept;
```

### Return value
A value representing the number of elements in the **map_base** object.

## See also 
* [winrt namespace](winrt.md)
* [winrt::single_threaded_map function template](single-threaded-map.md)
* [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections)
