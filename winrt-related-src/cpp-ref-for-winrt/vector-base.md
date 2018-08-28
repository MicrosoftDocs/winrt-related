---
author: stevewhims
description: A base class, for you to derive from, that represents a non-observable general-purpose collection known as a vector.
title: winrt::vector_base struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 08/26/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, vector, collection
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::vector_base struct template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))

> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A base class from which you can derive to implement your own custom non-observable general-purpose collection. For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename D, typename T>
struct vector_base : vector_view_base<D, T, impl::collection_version>
```

### Template parameters
`typename D`
Your derived type name.

`typename T`
The type of the elements in the **vector_base**.

## Requirements
**Minimum supported SDK:** Windows 10 SDK Preview Build 17661

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|-|-|
|[vector_base::Append function](#vectorbaseappend-function)|Appends an element to the end of the **vector_base** object.|
|[vector_base::Clear function](#vectorbaseclear-function)|Removes all elements from the **vector_base** object.|
|[vector_base::First function](#vectorbasefirst-function)|Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **vector_base** object.|
|[vector_base::GetAt function](#vectorbasegetat-function)|Retrieves the element at the specified index in the **vector_base** object.|
|[vector_base::GetMany function](#vectorbasegetmany-function)|Retrieves a collection of elements in the **vector_base** object beginning at the given index.|
|[vector_base::GetView function](#vectorbasegetview-function)|Retrieves an immutable view of the **vector_base** object.|
|[vector_base::IndexOf function](#vectorbaseindexof-function)|Retrieves the index of a specified element in the **vector_base** object.|
|[vector_base::InsertAt function](#vectorbaseinsertat-function)|Inserts an element at the specified index in the **vector_base** object.|
|[vector_base::RemoveAt function](#vectorbaseremoveat-function)|Removes the element at the specified index in the **vector_base** object.|
|[vector_base::RemoveAtEnd function](#vectorbaseremoveatend-function)|Removes the last element from the **vector_base** object.|
|[vector_base::ReplaceAll function](#vectorbasereplaceall-function)|Replaces all the elements in the **vector_base** object with the specified elements.|
|[vector_base::SetAt function](#vectorbasesetat-function)|Sets the value of the element at the specified index in the **vector_base** object.|
|[vector_base::Size function](#vectorbasesize-function)|Retrieves the number of elements in the **vector_base** object.|

## Iterators
A **vector_base** is a range, and that range is defined by internal free functions (each of which retrieves an iterator) that are compatible with standard language features. Because of this, you can enumerate the elements in a **vector_base** object with a range-based `for` statement.

You can also retrieve an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) from the [vector_base::First](#vectorbasefirst-function) function, and use that to iterate through the elements in a **vector_base** object.

```cppwinrt
...
#include <iostream>
using namespace winrt;
using namespace Windows::Foundation::Collections;
...
struct MyVector :
    implements<MyVector, IVector<float>, IVectorView<float>, IIterable<float>>,
    winrt::vector_base<MyVector, float>
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
    std::vector<float> m_values{ 0.1f, 0.2f, 0.3f };
};
...
IVector<float> coll{ winrt::make<MyVector>() };

for (auto const& el : coll)
{
    std::wcout << el << std::endl;
}

IIterator<float> it{ coll.First() };
while (it.HasCurrent())
{
    std::wcout << it.Current() << std::endl;
    it.MoveNext();
}
```

## vector_base::Append function
Appends an element to the end of the **vector_base** object.

### Syntax
```cppwinrt
void Append(T const& value);
```

### Parameters
`value`
The element to append.

## vector_base::Clear function
Removes all elements from the **vector_base** object.

### Syntax
```cppwinrt
void Clear() noexcept;
```

## vector_base::First function
Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **vector_base** object.

### Syntax
```cppwinrt
auto First();
```

### Return value
An [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **vector_base** object.

## vector_base::GetAt function
Retrieves the element at the specified index in the **vector_base** object.

### Syntax
```cppwinrt
T GetAt(uint32_t const index) const;
```

### Parameters
`index`
A zero-based element index.

### Return value
The element at the specified index in the **vector_base** object.

## vector_base::GetMany function
Retrieves a collection of elements in the **vector_base** object beginning at the given index.

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

## vector_base::GetView function
Retrieves an immutable view of the **vector_base** object.

### Syntax
```cppwinrt
winrt::Windows::Foundation::Collections::IVectorView<T> GetView() const noexcept;
```

### Return value
An [**IVectorView**](/uwp/api/windows.foundation.collections.ivectorview_t_) containing an immutable view of the **vector_base**.

## vector_base::IndexOf function
Retrieves the index of a specified element in the **vector_base** object.

### Syntax
```cppwinrt
bool IndexOf(T const& value, uint32_t& index) const noexcept;
```

### Parameters
`value`
The element, in the **vector_base** object, to look for.

`index`
The zero-based index of the element if the element is found, otherwise the number of elements in the **vector_base** object.

### Return value
`true` if the element is found, otherwise `false`.

## vector_base::InsertAt function
Inserts an element at the specified index in the **vector_base** object.

### Syntax
```cppwinrt
void InsertAt(uint32_t const index, T const& value);
```

### Parameters
`index`
The zero-based index at which to insert the element.

`value`
The element to insert.

## vector_base::RemoveAt function
Removes the element at the specified index in the **vector_base** object.

### Syntax
```cppwinrt
void RemoveAt(uint32_t const index);
```

### Parameters
`index`
The zero-based index of the element to remove.

## vector_base::RemoveAtEnd function
Removes the last element from the **vector_base** object.

### Syntax
```cppwinrt
void RemoveAtEnd();
```

## vector_base::ReplaceAll function
Replaces all the elements in the **vector_base** object with the specified elements.

### Syntax
```cppwinrt
void ReplaceAll(array_view<T const> value);
```

### Parameters
`value`
An [**array_view**](array-view.md) containing the new elements.

## vector_base::SetAt function
Sets the value of the element at the specified index in the **vector_base** object.

### Syntax
```cppwinrt
void SetAt(uint32_t const index, T const& value);
```

### Parameters
`index`
The zero-based index of the element whose value to set.

`value`
The element value to set.

## vector_base::Size function
Retrieves the number of elements in the **vector_base** object.

### Syntax
```cppwinrt
uint32_t Size() const noexcept;
```

### Return value
A value representing the number of elements in the **vector_base** object.

## See also 
* [winrt namespace](winrt.md)
