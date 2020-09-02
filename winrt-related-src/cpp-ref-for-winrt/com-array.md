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

Represents a C-style conformant array of data where the underlying buffer is allocated and freed via the COM task allocator, hence the name. It's typically used to represent a C-style conformant array that's allocated by one component, and freed by another.

**winrt::com_array** is used for passing parameters to and from Windows Runtime APIs. If you're authoring APIs then you'll probably need to construct a **winrt::com_array** to return a projected array to the caller; either as the return value, or through an output parameter.

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
|[put_abi function](#put_abi-function)|Retrieves the address of the **com_array** so that it can be set to another value. Also see [winrt::put_abi function](./put-abi.md).|
|[swap function](#swap-function)|Swaps the contents of the two **com_array** parameters.|

## com_array::com_array constructor

Initializes a new instance of the **com_array** struct with a copy of the input data, or with default values of `T` if no data is provided.

### Syntax

The constructors are numbered, and described further in **Remarks** below.

```cppwinrt
1.  com_array() noexcept;
2.  com_array(uint32_t const count);
3.  com_array(uint32_t const count, T const& value);
4.  template <typename InIt> com_array(InIt first, InIt last);
5.  com_array(std::vector<T> const& vectorValue);
6.  template <size_t N> com_array(std::array<T, N> const& arrayValue);
7.  template <uint32_t N> com_array(T const(&rawArrayValue)[N])
8.  com_array(std::initializer_list<T> initializerListValue);
9.  com_array(void* ptr, uint32_t const count, winrt::take_ownership_from_abi_t) noexcept;
10. com_array(com_array&& comArrayValue) noexcept;
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

### Remarks

The constructors are numbered in **Syntax** above.

#### 1. Default constructor

Constructs an empty buffer.

#### 2. Capacity constructor; default value

Creates a buffer of *count* elements, all of which are copies of a default-constructed **T**.

This is similar to (but not the same as) creating a buffer of *count* elements, each of which is a default-constructed **T**.

```cppwinrt
auto players{ winrt::com_array<MediaPlayer>(50) };
```

The **MediaPlayer** object's default constructor creates a reference to a new media player object, and its copy constructor copies the reference. Therefore, the above line of code creates an array of 50 references to the same media player object. It doesn't create an array of 50 different media player objects.

#### 3. Capacity constructor; explicit value

Creates a buffer of *count* elements, each of which is a copy of the provided *value*.

`winrt::com_array(2, 42)` is interpreted as an attempt to use the range constructor (4). But it fails because 2 and 42 aren't iterators. To get this to be interpreted as a capacity constructor with an explicit **int32_t** value, use an explicitly unsigned integer as the first parameter: `com_array(2u, 42)`.

#### 4. Range constructor

Creates a buffer that is a copy of the range [*first*, *last*).

State the underlying type **T** explicitly, like this.

```cppwinrt
auto a{ winrt::com_array<T>(source.begin(), source.end()) };
```

To move the range, rather than copying it, use the **std::move_iterator** iterator adaptor.

```cppwinrt
auto a{ winrt::com_array<T>(std::move_iterator(source.begin()),
                            std::move_iterator(source.end())) };
```

#### 5. Vector constructor

Creates a buffer that is a copy of the contents of *vectorValue*.

#### 6. Array constructor

Creates a buffer that is a copy of the contents of *arrayValue*.

#### 7. C-style array constructor

Creates a buffer that is a copy of the contents of the C-style array *rawArrayValue*.

#### 8. Initializer-list constructor

Creates a buffer that is a copy of the contents of the initializer list *initializerListValue*.

#### 9. ABI constructor

Takes ownership of a buffer of specified length.

This lowest-level of the constructors. Use it when you have a block of memory already allocated via **Co­Task­Mem­Alloc**, and you want the **com_array** to assume responsibility for it. To emphasize the special requirements for this constructor, the final argument must be **winrt::take_ownership_from_abi**.

#### 10. Move constructor

Moves the resources from another **com_array** of the same type, leaving the original empty.

#### Constructors 5, 6, and 7

Copies are taken of the contents of the provided container. You can use the range constructor (4) with the **std::move_iterator** iterator adaptor to move the contents into the **com_array** instead of copying them.

## com_array::clear function

Makes the **com_array** object empty.

### Syntax

```cppwinrt
void clear() noexcept;
```

## detach_abi function

Detaches the **com_array** object from its raw values, perhaps to return them to a caller. The **com_array** is cleared. Also see [winrt::detach_abi function](./detach-abi.md).

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

Retrieves the address of the **com_array** so that it can be set to another value. Also see [winrt::put_abi function](./put-abi.md).

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