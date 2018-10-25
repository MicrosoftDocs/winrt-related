---
author: stevewhims
description: A base class, for you to derive from, that represents an observable vector.
title: winrt::observable_vector_base struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 08/27/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, vector, observable, collection
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::observable_vector_base struct template (C++/WinRT)

A base class from which you can derive to implement your own custom observable vector. For more info, and code examples, see [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections).

## Syntax
```cppwinrt
template <typename D, typename T>
struct observable_vector_base : vector_base<D, T>
```

### Template parameters
`typename D`
Your derived type name.

`typename T`
The type of the elements in the **observable_vector_base**.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|-|-|
|[observable_vector_base::Append function](#observablevectorbaseappend-function)|Appends an element to the end of the **observable_vector_base** object.|
|[observable_vector_base::Clear function](#observablevectorbaseclear-function)|Removes all elements from the **observable_vector_base** object.|
|[observable_vector_base::First function](#observablevectorbasefirst-function)|Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **observable_vector_base** object.|
|[observable_vector_base::GetAt function](#observablevectorbasegetat-function)|Retrieves the element at the specified index in the **observable_vector_base** object.|
|[observable_vector_base::GetMany function](#observablevectorbasegetmany-function)|Retrieves a collection of elements in the **observable_vector_base** object beginning at the given index.|
|[observable_vector_base::GetView function](#observablevectorbasegetview-function)|Retrieves an immutable view of the **observable_vector_base** object.|
|[observable_vector_base::IndexOf function](#observablevectorbaseindexof-function)|Retrieves the index of a specified element in the **observable_vector_base** object.|
|[observable_vector_base::InsertAt function](#observablevectorbaseinsertat-function)|Inserts an element at the specified index in the **observable_vector_base** object.|
|[observable_vector_base::RemoveAt function](#observablevectorbaseremoveat-function)|Removes the element at the specified index in the **observable_vector_base** object.|
|[observable_vector_base::RemoveAtEnd function](#observablevectorbaseremoveatend-function)|Removes the last element from the **observable_vector_base** object.|
|[observable_vector_base::ReplaceAll function](#observablevectorbasereplaceall-function)|Replaces all the elements in the **observable_vector_base** object with the specified elements.|
|[observable_vector_base::SetAt function](#observablevectorbasesetat-function)|Sets the value of the element at the specified index in the **observable_vector_base** object.|
|[observable_vector_base::Size function](#observablevectorbasesize-function)|Retrieves the number of elements in the **observable_vector_base** object.|
|[observable_vector_base::VectorChanged function](#observablevectorbasevectorchanged-function)|Registers and revokes a delegate that handles the vector-changed event of the **observable_vector_base** object.|

## Iterators
A **observable_vector_base** is a range, and that range is defined by internal free functions (each of which retrieves an iterator) that are compatible with standard language features. Because of this, you can enumerate the elements in a **observable_vector_base** object with a range-based `for` statement.

You can also retrieve an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) from the [observable_vector_base::First](#observablevectorbasefirst-function) function, and use that to iterate through the elements in a **observable_vector_base** object.

```cppwinrt
...
#include <iostream>
using namespace winrt;
using namespace Windows::Foundation::Collections;
...
struct MyObservableVector :
    implements<MyObservableVector, IObservableVector<float>, IVector<float>, IVectorView<float>, IIterable<float>>,
    winrt::observable_vector_base<MyObservableVector, float>
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
IObservableVector<float> coll{ winrt::make<MyObservableVector>() };

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

## observable_vector_base::Append function
Appends an element to the end of the **observable_vector_base** object.

### Syntax
```cppwinrt
void Append(T const& value);
```

### Parameters
`value`
The element to append.

## observable_vector_base::Clear function
Removes all elements from the **observable_vector_base** object.

### Syntax
```cppwinrt
void Clear() noexcept;
```

## observable_vector_base::First function
Retrieves an [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **observable_vector_base** object.

### Syntax
```cppwinrt
auto First();
```

### Return value
An [**IIterator**](/uwp/api/windows.foundation.collections.iiterator_t_) representing the first element in the **observable_vector_base** object.

## observable_vector_base::GetAt function
Retrieves the element at the specified index in the **observable_vector_base** object.

### Syntax
```cppwinrt
T GetAt(uint32_t const index) const;
```

### Parameters
`index`
A zero-based element index.

### Return value
The element at the specified index in the **observable_vector_base** object.

## observable_vector_base::GetMany function
Retrieves a collection of elements in the **observable_vector_base** object beginning at the given index.

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

## observable_vector_base::GetView function
Retrieves an immutable view of the **observable_vector_base** object.

### Syntax
```cppwinrt
winrt::Windows::Foundation::Collections::IVectorView<T> GetView() const noexcept;
```

### Return value
An [**IVectorView**](/uwp/api/windows.foundation.collections.ivectorview_t_) containing an immutable view of the **observable_vector_base**.

## observable_vector_base::IndexOf function
Retrieves the index of a specified element in the **observable_vector_base** object.

### Syntax
```cppwinrt
bool IndexOf(T const& value, uint32_t& index) const noexcept;
```

### Parameters
`value`
The element, in the **observable_vector_base** object, to look for.

`index`
The zero-based index of the element if the element is found, otherwise the number of elements in the **observable_vector_base** object.

### Return value
`true` if the element is found, otherwise `false`.

## observable_vector_base::InsertAt function
Inserts an element at the specified index in the **observable_vector_base** object.

### Syntax
```cppwinrt
void InsertAt(uint32_t const index, T const& value);
```

### Parameters
`index`
The zero-based index at which to insert the element.

`value`
The element to insert.

## observable_vector_base::RemoveAt function
Removes the element at the specified index in the **observable_vector_base** object.

### Syntax
```cppwinrt
void RemoveAt(uint32_t const index);
```

### Parameters
`index`
The zero-based index of the element to remove.

## observable_vector_base::RemoveAtEnd function
Removes the last element from the **observable_vector_base** object.

### Syntax
```cppwinrt
void RemoveAtEnd();
```

## observable_vector_base::ReplaceAll function
Replaces all the elements in the **observable_vector_base** object with the specified elements.

### Syntax
```cppwinrt
void ReplaceAll(array_view<T const> value);
```

### Parameters
`value`
An [**array_view**](array-view.md) containing the new elements.

## observable_vector_base::SetAt function
Sets the value of the element at the specified index in the **observable_vector_base** object.

### Syntax
```cppwinrt
void SetAt(uint32_t const index, T const& value);
```

### Parameters
`index`
The zero-based index of the element whose value to set.

`value`
The element value to set.

## observable_vector_base::Size function
Retrieves the number of elements in the **observable_vector_base** object.

### Syntax
```cppwinrt
uint32_t Size() const noexcept;
```

### Return value
A value representing the number of elements in the **observable_vector_base** object.

## observable_vector_base::VectorChanged function
Registers and/or revokes a delegate that handles the vector-changed event of the **observable_vector_base** object.

### Syntax
```cppwinrt
// Register
winrt::event_token VectorChanged(winrt::Windows::Foundation::Collections::VectorChangedEventHandler<T> const& handler);

// Revoke with event_token
void VectorChanged(winrt::event_token const cookie);

// Revoke with event_revoker
VectorChanged_revoker VectorChanged(winrt::auto_revoke_t, winrt::Windows::Foundation::Collections::VectorChangedEventHandler<T> const& handler) const;
```

### Return value
Either `void`, a [**winrt::event_token**](event-token.md) with which you can revoke a registered delegate, or a **VectorChanged_revoker** (a type alias for a [**winrt::event_revoker\<IObservableVector\<T\>\>**](event-revoker.md)) with which you can revoke a registered delegate.

### Example

```cppwinrt
winrt::event_revoker<IObservableVector<float>> m_event_revoker;
...
m_event_revoker = coll.VectorChanged(winrt::auto_revoke, [this](IObservableVector<float> const&, IVectorChangedEventArgs const&)
{
    ...
});
```

## See also 
* [winrt namespace](winrt.md)
* [winrt::single_threaded_observable_vector function template](single-threaded-observable-vector.md)
* [Collections with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/collections)
