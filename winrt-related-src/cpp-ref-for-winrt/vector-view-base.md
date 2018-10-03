---
author: stevewhims
description: A base class, for you to derive from, that represents a view of a contiguous sequence of elements in a general-purpose collection.
title: winrt::vector_view_base struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 08/25/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, vector, view, collection
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::vector_view_base struct template (C++/WinRT)

A base class from which you can derive to implement your own custom view, or span, of a contiguous sequence of elements in a general-purpose collection. For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename D, typename T, typename Version = impl::no_collection_version>
struct vector_view_base : iterable_base<D, T, Version>
```

### Template parameters
`typename D`
Your derived type name.

`typename T`
The type of the elements that the **vector_view_base** views, or spans.

`typename Version`
A type that provides versioning policy and services to the collection.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[vector_view_base::First function](#vectorviewbasefirst-function)|Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element viewed by the **vector_view_base** object.|
|[vector_view_base::GetAt function](#vectorviewbasegetat-function)|Retrieves the element at the specified index viewed by the **vector_view_base** object.|
|[vector_view_base::GetMany function](#vectorviewbasegetmany-function)|Retrieves a collection of elements viewed by the **vector_view_base** object beginning at the given index.|
|[vector_view_base::IndexOf function](#vectorviewbaseindexof-function)|Retrieves the index of a specified element viewed by the **vector_view_base** object.|
|[vector_view_base::Size function](#vectorviewbasesize-function)|Retrieves the number of elements viewed by the **vector_view_base** object.|

## Iterators
A **vector_view_base** is a range, and that range is defined by internal free functions (each of which retrieves an iterator) that are compatible with standard language features. Because of this, you can enumerate the elements viewed by a **vector_view_base** object with a range-based `for` statement.

You can also retrieve an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) from the [vector_view_base::First](#vectorviewbasefirst-function) function, and use that to iterate through the elements viewed by a **vector_view_base** object.

```cppwinrt
...
#include <iostream>
using namespace winrt;
using namespace Windows::Foundation::Collections;
...
struct MyVectorView :
    implements<MyVectorView, IVectorView<float>, IIterable<float>>,
    winrt::vector_view_base<MyVectorView, float>
{
    auto& get_container() const noexcept
    {
        return m_values;
    }

private:
    std::vector<float> m_values{ 0.1f, 0.2f, 0.3f };
};
...
IVectorView<float> view{ winrt::make<MyVectorView>() };

for (float el : view)
{
    std::wcout << el << std::endl;
}

IIterator<float> it{ view.First() };
while (it.HasCurrent())
{
    std::wcout << it.Current() << std::endl;
    it.MoveNext();
}
```

## vector_view_base::First function
Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element viewed by the **vector_view_base** object.

### Syntax
```cppwinrt
auto First();
```

### Return value
An [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element viewed by the **vector_view_base** object.

## vector_view_base::GetAt function
Retrieves the element at the specified index viewed by the **vector_view_base** object.

### Syntax
```cppwinrt
T GetAt(uint32_t const index) const;
```

### Parameters
`index`
A zero-based element index.

### Return value
The element at the specified index viewed by the **vector_view_base** object.

## vector_view_base::GetMany function
Retrieves a collection of elements viewed by the **vector_view_base** object beginning at the given index.

### Syntax
```cppwinrt
uint32_t GetMany(uint32_t const startIndex, array_view<T> values) const;
```

### Parameters
`startIndex`
A zero-based element index to start at.

`values`
An [**array_view**](array-view.md) to copy the items into.

### Return value
A value representing the number of elements retrieved.

## vector_view_base::IndexOf function
Retrieves the index of a specified element viewed by the **vector_view_base** object.

### Syntax
```cppwinrt
bool IndexOf(T const& value, uint32_t& index) const noexcept;
```

### Parameters
`value`
The element, viewed by the **vector_view_base** object, to look for.

`index`
The zero-based index of the element if the element is found, otherwise the number of elements viewed by the **vector_view_base** object.

### Return value
`true` if the element is found, otherwise `false`.

## vector_view_base::Size function
Retrieves the number of elements viewed by the **vector_view_base** object.

### Syntax
```cppwinrt
uint32_t Size() const noexcept;
```

### Return value
A value representing the number of elements viewed by the **vector_view_base** object.

## See also 
* [winrt namespace](winrt.md)
* [winrt::single_threaded_vector function template](single-threaded-vector.md)
* [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections)
