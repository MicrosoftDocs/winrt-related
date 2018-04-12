---
author: stevewhims
description: A view, or span, of a contiguous series of values.
title: winrt::array_view struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 04/10/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, array, view, array_view, span
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::array_view struct template (C++/WinRT)
A view, or span, of a contiguous series of values. For more examples and info about **winrt::array_view**, see [Standard C++ data types and C++/WinRT](/windows/uwp/cpp-and-winrt-apis/std-cpp-data-types).

## Syntax
```cppwinrt
template <typename T>
struct array_view
```

### Template parameters
`typename T`
The type of the values (elements) that the **array_view** views, or spans.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17133.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[array_view::array_view constructor](#arrayviewarrayview-constructor)|Initializes a new instance of the **array_view** struct with a copy of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[array_view::at function](#arrayviewat-function)|Returns a reference to the element at the specified position within the **array_view** object.|
|[array_view::back function](#arrayviewback-function)|Returns a reference to the last element in the **array_view** object.|
|[array_view::begin function](#arrayviewbegin-function)|Returns an iterator to the first element in the **array_view** object.|
|[array_view::cbegin function](#arrayviewcbegin-function)|Returns a const iterator to the first element in the **array_view** object.|
|[array_view::cend function](#arrayviewcend-function)|Returns a const iterator to one beyond the end of (one beyond the last element in) the **array_view** object.|
|[array_view::crbegin function](#arrayviewcrbegin-function)|Returns a const reverse iterator to one beyond the end of (one beyond the last element in) the **array_view** object.|
|[array_view::crend function](#arrayviewcrend-function)|Returns a const reverse iterator to the first element in the **array_view** object.|
|[array_view::data function](#arrayviewdata-function)|Returns a pointer to the underlying data being viewed by the **array_view** object.|
|[array_view::empty function](#arrayviewempty-function)|Returns a value indicating whether the **array_view** object is empty (is a view on zero elements).|
|[array_view::end function](#arrayviewend-function)|Returns an iterator to one beyond the end of (one beyond the last element in) the **array_view** object.|
|[array_view::front function](#arrayviewfront-function)|Returns a reference to the first element in the **array_view** object.|
|[array_view::rbegin function](#arrayviewrbegin-function)|Returns a reverse iterator to one beyond the end of (one beyond the last element in) the **array_view** object.|
|[array_view::rend function](#arrayviewrend-function)|Returns a reverse iterator to the first element in the **array_view** object.|
|[array_view::size function](#arrayviewsize-function)|Returns the number of elements in the **array_view** object.|

## Member operators
|Operator|Description| 
|------------|-----------------|
|[array_view::operator[] &lpar;subscript operator)](#arrayviewoperator-subscript-operator)|Returns a reference to the element at the specified position within the **array_view** object.|

## Free operators
|Operator|Description| 
|------------|-----------------| 
|[operator!= (inequality operator)](#operator-inequality-operator)|Returns a value indicating whether the two parameters are unequal to one another.|
|[operator< (less-than operator)](#operator-less-than-operator)|Returns a value indicating whether the first parameter is less than the second parameter.|
|[operator<= (less-than-or-equal-to operator)](#operator-less-than-or-equal-to-operator)|Returns a value indicating whether the first parameter is less than or equal to the second parameter.|
|[operator== (equality operator)](#operator-equality-operator)|Returns a value indicating whether the two parameters are equal to one another.|
|[operator> (greater-than operator)](#operator-greater-than-operator)|Returns a value indicating whether the first parameter is greater than the second parameter.|
|[operator>= (greater-than-or-equal-to operator)](#operator-greater-than-or-equal-to-operator)|Returns a value indicating whether the first parameter is greater than or equal to the second parameter.|

## Iterators
An **array_view** is a range, and that range is defined by the [array_view::begin](#arrayviewbegin-function) and [array_view::end](#arrayviewend-function) member functions, each of which returns an iterator (also see [array_view::cbegin](#arrayviewcbegin-function) and [array_view::cend](#arrayviewcend-function)). Because of this, you can enumerate the characters in an **array_view** object with either a range-based `for` statement, or with the **std::for_each** template function.

```cppwinrt
#include <iostream>
using namespace winrt;
...
template <typename T>
void Iterators(array_view<T> const& theArrayView)
{
	for (T& element : theArrayView)
	{
		std::wcout << element << " ";
	}

	std::for_each(theArrayView.cbegin(), theArrayView.cend(), [](T const& element) { std::wcout << element << " "; });
}
```

## array_view::array_view constructor
Initializes a new instance of the **array_view** struct with a copy of the input data.

### Syntax
```cppwinrt
array_view() noexcept
template <typename C, uint32_t N> array_view(C(&rawArrayValue)[N]) noexcept
template <typename C, uint32_t N> array_view(std::array<C, N> const& arrayValue) noexcept
template <typename C, uint32_t N> array_view(std::array<C, N>& arrayValue) noexcept
array_view(std::initializer_list<T> initializerListValue) noexcept
template <typename C> array_view(std::vector<C> const& vectorValue) noexcept
template <typename C> array_view(std::vector<C>& vectorValue) noexcept
array_view(T* first, T* last) noexcept
```

### Template parameters
`typename C`
The type of the values (elements) in the input data.

`uint32_t N`
The number of values (elements) in the input data.

### Parameters
`rawArrayValue`
A raw array value that initializes the **array_view** object.

`arrayValue`
A **std::array** value that initializes the **array_view** object.

`initializerListValue`
An initializer list value that initializes the **array_view** object.

`vectorValue`
A **std::vector** value that initializes the **array_view** object.

`first` `last`
Pointers to values with which to initialize the **array_view** object. If `first` equals `last`, then the **array_view** object is empty.

### Example
```cppwinrt
using namespace winrt;
...
void Constructors()
{
	// array_view() noexcept
	array_view<byte const> fromDefault{};

	byte theRawArray[]{ 99, 98, 97 };

	// template <typename C, uint32_t N> array_view(C(&value)[N]) noexcept
	array_view<byte const> fromRawArray{ theRawArray };

	const std::array<byte, 3> theConstArray{ 99, 98, 97 };

	// template <typename C, uint32_t N> array_view(std::array<C, N>& value) noexcept
	array_view<byte const> fromConstArray{ theConstArray };

	std::array<byte, 3> theArray{ 99, 98, 97 };

	// template <typename C, uint32_t N> array_view(std::array<C, N> const& value) noexcept
	array_view<byte const> fromArray{ theArray };

	// array_view(std::initializer_list<T> value) noexcept
	array_view<byte const> fromInitializerList{ 99, 98, 97 };

	const std::vector<byte> theConstVector{ 99, 98, 97 };

	// template <typename C> array_view(std::vector<C> const& value) noexcept
	array_view<byte const> fromConstVector{ theConstVector };

	std::vector<byte> theVector{ 99, 98, 97 };

	// template <typename C> array_view(std::vector<C>& value) noexcept
	array_view<byte const> fromVector{ theVector };

	// array_view(T* first, T* last) noexcept
	array_view<byte const> fromRange{ theArray.data(), theArray.data() + 2 }; // just the first two elements.
}
```

## array_view::at function
Returns a reference to the element at the specified position within the **array_view** object.

### Syntax
```cppwinrt
T& at(uint32_t const pos)
T const& at(uint32_t const pos) const
```

### Parameters
`pos`
A zero-based element position, or index.

### Return value
A reference to the element at the specified position within the **array_view** object.

## array_view::back function
Returns a reference to the last element in the **array_view** object.

### Syntax
```cppwinrt
T const& back() const noexcept
T& back() noexcept
```

### Return value
A reference to the last element in the **array_view** object.

## array_view::begin function
Returns an iterator to the first element in the **array_view** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
stdext::checked_array_iterator<T const> begin() const noexcept
stdext::checked_array_iterator<T> begin() noexcept
```

### Return value
An iterator to the first element in the **array_view** object.

## array_view::cbegin function
Returns a const iterator to the first element in the **array_view** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
stdext::checked_array_iterator<T const> cbegin() const noexcept
```

### Return value
A const iterator to the first element in the **array_view** object.

## array_view::cend function
Returns a const iterator to one beyond the end of (one beyond the last element in) the **array_view** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
stdext::checked_array_iterator<T const> cend() const noexcept
```

### Return value
A const iterator to one beyond the end of (one beyond the last element in) the **array_view** object.

## array_view::crbegin function
Returns a const reverse iterator to one beyond the end of (one beyond the last element in) the **array_view** object.

### Syntax
```cppwinrt
std::reverse_iterator<stdext::checked_array_iterator<T const>> crbegin() const noexcept
```

### Return value
A const reverse iterator to one beyond the end of (one beyond the last element in) the **array_view** object.

## array_view::crend function
Returns a const reverse iterator to the first element in the **array_view** object.

### Syntax
```cppwinrt
std::reverse_iterator<stdext::checked_array_iterator<T const>> crend() const noexcept
```

### Return value
A const reverse iterator to the first element in the **array_view** object.

## array_view::data function
Returns a pointer to the underlying data being viewed by the **array_view** object.

### Syntax
```cppwinrt
T const* data() const noexcept
T* data() noexcept
```

### Return value
A pointer to the underlying data being viewed by the **array_view** object.

## array_view::empty function
Returns a value indicating whether the **array_view** object is empty (is a view on zero elements).

### Syntax
```cppwinrt
bool empty() const noexcept
```

### Return value
`true` if the **array_view** object is empty (is a view on zero elements), otherwise `false`.

## array_view::end function
Returns an iterator to one beyond the end of (one beyond the last element in) the **array_view** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
stdext::checked_array_iterator<T const> end() const noexcept
stdext::checked_array_iterator<T> end() noexcept
```

### Return value
An iterator to one beyond the end of (one beyond the last element in) the **array_view** object.

## array_view::front function
Returns a reference to the first element in the **array_view** object.

### Syntax
```cppwinrt
T const& front() const noexcept
T& front() noexcept
```

### Return value
A reference to the first element in the **array_view** object.

## array_view::operator[] &lpar;subscript operator)
Returns a reference to the element at the specified position within the **array_view** object.

### Syntax
```cppwinrt
T const& operator[](uint32_t const pos) const noexcept
T& operator[](uint32_t const pos) noexcept
```

### Parameters
`pos`
A zero-based element position, or index.

### Return value
A reference to the element at the specified position within the **array_view** object.

## array_view::rbegin function
Returns a reverse iterator to one beyond the end of (one beyond the last element in) the **array_view** object.

### Syntax
```cppwinrt
std::reverse_iterator<stdext::checked_array_iterator<T const>> rbegin() const noexcept
std::reverse_iterator<stdext::checked_array_iterator<T>> rbegin() noexcept
```

### Return value
A reverse iterator to one beyond the end of (one beyond the last element in) the **array_view** object.

## array_view::rend function
Returns a reverse iterator to the first element in the **array_view** object.

### Syntax
```cppwinrt
std::reverse_iterator<stdext::checked_array_iterator<T const>> rend() const noexcept
std::reverse_iterator<stdext::checked_array_iterator<T>> rend() noexcept
```

### Return value
A reverse iterator to the first element in the **array_view** object.

## array_view::size function
Returns the number of elements in the **array_view** object.

### Syntax
```cppwinrt
uint32_t size() const noexcept
```

### Return value
A `uint32_t` containing the number of elements in the **array_view** object.

## operator!= (inequality operator)
Returns a value indicating whether the two parameters are unequal to one another.

### Syntax
```cppwinrt
template <typename T> bool operator!=(winrt::array_view<T> const& left, winrt::array_view<T> const& right) noexcept
```

### Parameters
`left` `right`
An **array_view** value to compare with the other parameter.

### Return value
`true` if the two parameters are unequal to one another, otherwise `false`.

## operator< (less-than operator)
Returns a value indicating whether the first parameter is less than the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator<(winrt::array_view<T> const& left, winrt::array_view<T> const& right) noexcept
```

### Parameters
`left` `right`
An **array_view** value to compare with the other parameter.

### Return value
`true` if the first parameter is less than the second parameter, otherwise `false`.

## operator<= (less-than-or-equal-to operator)
Returns a value indicating whether the first parameter is less than or equal to the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator<=(winrt::array_view<T> const& left, winrt::array_view<T> const& right) noexcept
```

### Parameters
`left` `right`
An **array_view** value to compare with the other parameter.

### Return value
`true` if the first parameter is less than or equal to the second parameter, otherwise `false`.

## operator== (equality operator)
Returns a value indicating whether the two parameters are equal to one another.

### Syntax
```cppwinrt
template <typename T> bool operator==(winrt::array_view<T> const& left, winrt::array_view<T> const& right) noexcept
```

### Parameters
`left` `right`
An **array_view** value to compare with the other parameter.

### Return value
`true` if the two parameters are equal to one another, otherwise `false`.

## operator> (greater-than operator)
Returns a value indicating whether the first parameter is greater than the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator>(winrt::array_view<T> const& left, winrt::array_view<T> const& right) noexcept
```

### Parameters
`left` `right`
An **array_view** value to compare with the other parameter.

### Return value
`true` if the first parameter is greater than the second parameter, otherwise `false`.

## operator>= (greater-than-or-equal-to operator)
Returns a value indicating whether the first parameter is greater than or equal to the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator>=(winrt::array_view<T> const& left, winrt::array_view<T> const& right) noexcept
```

### Parameters
`left` `right`
An **array_view** value to compare with the other parameter.

### Return value
`true` if the first parameter is greater than or equal to the second parameter, otherwise `false`.

## See also 
* [winrt namespace](winrt.md)
