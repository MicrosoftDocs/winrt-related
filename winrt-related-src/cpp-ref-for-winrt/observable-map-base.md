---

description: A base class, for you to derive from, that represents an observable associative collection.
title: winrt::observable_map_base struct template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 08/27/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, map, associative, collection
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::observable_map_base struct template (C++/WinRT))

A base class from which you can derive to implement your own custom observable associative collection. For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename D, typename K, typename V>
struct observable_map_base : map_base<D, K, V>
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

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[observable_map_base::Clear function](#observable_map_baseclear-function)|Removes all elements from the **observable_map_base** object.|
|[observable_map_base::First function](#observable_map_basefirst-function)|Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **observable_map_base** object.|
|[observable_map_base::GetView function](#observable_map_basegetview-function)|Retrieves an immutable view of the **observable_map_base** object.|
|[observable_map_base::HasKey function](#observable_map_basehaskey-function)|Determines whether the specified key belongs to an element in the **observable_map_base** object.|
|[observable_map_base::Insert function](#observable_map_baseinsert-function)|Inserts or updates an element in the **observable_map_base** object.|
|[observable_map_base::Lookup function](#observable_map_baselookup-function)|Looks up the element identified by the specified key, and retrieves the corresponding value.|
|[observable_map_base::MapChanged function](#observable_vector_basemapchanged-function)|Registers and revokes a delegate that handles the map-changed event of the **observable_map_base** object.|
|[observable_map_base::Remove function](#observable_map_baseremove-function)|Removes an element from the **observable_map_base** object.|
|[observable_map_base::Size function](#observable_map_basesize-function)|Retrieves the number of elements in the **observable_map_base** object.|

## Iterators
A **observable_map_base** is a range, and that range is defined by internal free functions (each of which retrieves an iterator) that are compatible with standard language features. Because of this, you can enumerate the elements in a **observable_map_base** object with a range-based `for` statement.

You can also retrieve an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) from the [observable_map_base::First](#observable_map_basefirst-function) function, and use that to iterate through the elements in a **observable_map_base** object.

```cppwinrt
...
#include <iostream>
using namespace winrt;
using namespace Windows::Foundation::Collections;
...
struct MyObservableMap :
    implements<MyObservableMap, IObservableMap<winrt::hstring, int>, IMap<winrt::hstring, int>, IMapView<winrt::hstring, int>, IIterable<IKeyValuePair<winrt::hstring, int>>>,
    winrt::observable_map_base<MyObservableMap, winrt::hstring, int>
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
IObservableMap<winrt::hstring, int> map{ winrt::make<MyObservableMap>() };

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

## observable_map_base::Clear function
Removes all elements from the **observable_map_base** object.

### Syntax
```cppwinrt
void Clear() noexcept;
```

## observable_map_base::First function
Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **observable_map_base** object.

### Syntax
```cppwinrt
auto First();
```

### Return value
An [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **observable_map_base** object.

## observable_map_base::GetView function
Retrieves an immutable view of the **observable_map_base** object.

### Syntax
```cppwinrt
winrt::Windows::Foundation::Collections::IMapView<K, V> GetView() const;
```

### Return value
An [**IMapView**](/uwp/api/windows.foundation.collections.imapview_k_v_) containing an immutable view of the **observable_map_base**.

## observable_map_base::HasKey function
Determines whether the specified key belongs to an element in the **observable_map_base** object.

### Syntax
```cppwinrt
bool HasKey(K const& key) const noexcept;
```

### Parameters
`key`
The key to look for.

### Return value
`true` if an element containing the key is found, otherwise `false`.

## observable_map_base::Insert function
Inserts or updates an element in the **observable_map_base** object.

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

## observable_map_base::Lookup function
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

## observable_vector_base::MapChanged function
Registers and/or revokes a delegate that handles the map-changed event of the **observable_map_base** object.

### Syntax
```cppwinrt
// Register
winrt::event_token MapChanged(winrt::Windows::Foundation::Collections::MapChangedEventHandler<K, V> const& handler);

// Revoke with event_token
void MapChanged(winrt::event_token const cookie);

// Revoke with event_revoker
MapChanged_revoker MapChanged(winrt::auto_revoke_t, winrt::Windows::Foundation::Collections::MapChangedEventHandler<K, V> const& handler) const
```

### Return value
Either `void`, a [**winrt::event_token**](event-token.md) with which you can revoke a registered delegate, or a **MapChanged_revoker** (a type alias for a [**winrt::event_revoker\<IObservableMap\<K, V\>\>**](event-revoker.md)) with which you can revoke a registered delegate.

### Example

```cppwinrt
winrt::event_revoker<IObservableMap<winrt::hstring, int>> m_event_revoker;
...
m_event_revoker = map.MapChanged(winrt::auto_revoke, [this](IObservableMap<winrt::hstring, int> const&, IMapChangedEventArgs<winrt::hstring> const&)
{
    ...
});
```

## observable_map_base::Remove function
Removes an element from the **observable_map_base** object.

### Syntax
```cppwinrt
void Remove(K const& key);
```

### Parameters
`key`
The key associated with the element to remove.

## observable_map_base::Size function
Retrieves the number of elements in the **observable_map_base** object.

### Syntax
```cppwinrt
uint32_t Size() const noexcept;
```

### Return value
A value representing the number of elements in the **observable_map_base** object.

## See also 
* [winrt namespace](winrt.md)
* [winrt::single_threaded_observable_map function template](single-threaded-observable-map.md)
* [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections)
