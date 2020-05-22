---
description: A view, or span, of a contiguous series of values for passing to and from Windows Runtime APIs.
title: winrt::com_array struct template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 05/10/2019
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, array, view, com_array, span
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::com_array struct template (C++/WinRT)

An array of objects; used for passing parameters to and from Windows Runtime APIs. **com_array** uses the COM allocator for memory allocation and freeing, hence the name.

**winrt::com_array** derives from **winrt::array_view**. See the [**winrt::array_view**](array-view.md) struct template topic, which documents members and free operators that are also available to **winrt::com_array**. However, be aware of the difference in semantics between the base type **winrt::array_view** (which is a non-owning view, or span, of a contiguous series of values), and **winrt::com_array** (which allocates and frees its own elements).

## Syntax

```cppwinrt
template <typename T>
struct com_array : winrt::array_view<T>
```

### Template parameters

`typename T`
The type of the values (elements) that the **com_array** contains.

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors

|Constructor|Description|
|------------|-----------------|
|[com_array::com_array constructor](#com_arraycom_array-constructor)|Initializes a new instance of the **com_array** struct with a copy of the input data, or with default values of `T` if no data is provided.|

## Member functions

|Function|Description|
|------------|-----------------|
|[com_array::clear function](#com_arrayclear-function)|Makes the **com_array** object empty.|

## Member operators

|Operator|Description|
|------------|-----------------|
|[com_array::operator= (assignment operator)](#com_arrayoperator-assignment-operator)|Assigns a value to the **com_array** object.|

## Free functions

|Function|Description|
|------------|-----------------|
|[detach_abi function](#detach_abi-function)|Detaches the **com_array** object from its raw values, perhaps to return them to a caller. The **com_array** is cleared. Also see [winrt::detach_abi function](/uwp/cpp-ref-for-winrt/detach-abi).|
|[put_abi function](#put_abi-function)|Retrieves the address of the **com_array** so that it can be set to another value. Also see [winrt::put_abi function](/uwp/cpp-ref-for-winrt/put-abi).|
|[swap function](#swap-function)|Swaps the contents of the two **com_array** parameters.|

## com_array::com_array constructor

Initializes a new instance of the **com_array** struct with a copy of the input data, or with default values of `T` if no data is provided.

### Syntax

```cppwinrt
com_array() noexcept;
com_array(uint32_t const count);
com_array(uint32_t const count, T const& value);
template <typename InIt> com_array(InIt first, InIt last);
com_array(std::vector<T> const& vectorValue);
template <size_t N> com_array(std::array<T, N> const& arrayValue);
template <uint32_t N> com_array(T const(&rawArrayValue)[N])
com_array(std::initializer_list<T> initializerListValue);
com_array(void* ptr, uint32_t const count, winrt::take_ownership_from_abi_t) noexcept;
com_array(com_array&& comArrayValue) noexcept;
```

### Template parameters

`typename InIt`
An input iterator, which provides the input data.

`size_t N` `uint32_t N`
The number of values (elements) in the input data.

### Parameters

`arrayValue`
A **std::array** value that initializes the **com_array** object.

`comArrayValue`
Another **com_array** that initializes the **com_array** object. After the constructor returns, *comArrayValue* will be empty.

`count`
The element count of the **com_array** object.

`first` `last`
A pair of input iterators. The values in the range [*first*, *last*) are used to initialize the **com_array** object.

`initializerListValue`
An initializer list value that initializes the **com_array** object.

`ptr`
A pointer to a block of N values, which you've allocated by using [CoTaskMemAlloc](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemalloc). The **com_array** object takes ownership of this memory.

`rawArrayValue`
A C-style array that initializes the **com_array** object.

`value`
The value to give to each element of the **com_array** object.

`vectorValue`
A **std::vector** value that initializes the **com_array** object.

## com_array::clear function

Makes the **com_array** object empty.

### Syntax

```cppwinrt
void clear() noexcept;
```

## detach_abi function

Detaches the **com_array** object from its raw values, perhaps to return them to a caller. The **com_array** is cleared. Also see [winrt::detach_abi function](/uwp/cpp-ref-for-winrt/detach-abi).

### Syntax

```cppwinrt
auto detach_abi(winrt::com_array<T>& object) noexcept;
auto detach_abi(winrt::com_array<T>&& object) noexcept;
```

### Parameters

`object`
A **com_array** object to operate on.

### Return value

A two-element tuple containing an element count, and the contiguous series of values that the **com_array** spanned.

## com_array::operator= (assignment operator)

Assigns a value to the **com_array** object.

### Syntax

```cppwinrt
com_array& operator=(winrt::com_array&& comArrayValue) noexcept;
```

### Parameters

`comArrayValue`
A **com_array** value to assign to the **com_array** object.

### Return value

A reference to the **com_array** object.

## put_abi function

Retrieves the address of the **com_array** so that it can be set to another value. Also see [winrt::put_abi function](/uwp/cpp-ref-for-winrt/put-abi).

### Syntax

```cppwinrt
template<typename T> auto put_abi(winrt::com_array<T>& object) noexcept;
```

### Parameters

`object`
A **com_array** object to operate on.

### Return value

The address of the **com_array**, ready to be set to another value.

## swap function

Swaps the contents of the two **com_array** parameters.

### Syntax

```cppwinrt
friend void swap(winrt::com_array& left, winrt::com_array& right) noexcept;
```

### Parameters

`left` `right`
A **com_array** value whose contents to mutually swap with those of the other parameter.

### Example

```cppwinrt
using namespace winrt;
...
    com_array<byte> left{ 1,2,3 };
    com_array<byte> right{ 4,5,6 };
    swap(left, right);
```

## See also 

* [winrt namespace](winrt.md)
