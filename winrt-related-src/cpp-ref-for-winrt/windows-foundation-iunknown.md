---
author: stevewhims
description: Every C++/WinRT runtime class (whether a Windows or a third party runtime class) derives from winrt::Windows::Foundation::IUnknown.
title: winrt::Windows::Foundation::IUnknown struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 04/10/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, iunknown
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::Windows::Foundation::IUnknown struct ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
Every C++/WinRT runtime class (whether a Windows or a third party runtime class) derives from **winrt::Windows::Foundation::IUnknown**. It represents the COM [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface, and it provides facilities such as querying for a different interface, abi functions, and comparison operators.

## Syntax
```cppwinrt
struct IUnknown
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[IUnknown::IUnknown constructor](#iunknowniunknown-constructor)|Initializes a new instance of the **IUnknown** struct, optionally with a copy or move of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[IUnknown::as function](#iunknownas-function)|Returns the requested interface, if it is supported. Throws if it is not.|
|[IUnknown::try_as function](#iunknowntryas-function)|Returns the requested interface, if it is supported. Returns `null`, or `false`, if it is not.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[IUnknown::operator bool](#iunknownoperator-bool)|Checks whether or not the **IUnknown** object is referencing an interface.|
|[IUnknown::operator= (assignment operator)](#iunknownoperator-assignment-operator)|Assigns a value to the **IUnknown** object.|

## Free functions
|Function|Description|
|------------|-----------------|
|[attach_abi function](#iunknownattachabi-function)|Attaches an **IUnknown** object to a raw pointer that owns a reference to its target; an additional reference is not added.|
|[copy_from_abi function](#iunknowncopyfromabi-function)|Copies to an **IUnknown** object from another pointer. Decrements the reference count on any currently referenced interface or object, copies the raw pointer parameter, and begins managing the lifetime of the interface or object pointed to by it.|
|[copy_to_abi function](#iunknowncopytoabi-function)|Copies to another pointer from an **IUnknown** object. Increments the reference count on any currently referenced interface or object, and copies that interface or object's memory address into the parameter.|
|[detach_abi function](#iunknowndetachabi-function)|Detaches from the raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) without decrementing the reference count, perhaps to return it to a caller.|
|[get_abi function](#iunknowngetabi-function)|Returns the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer should you need to pass it to a function.|
|[get_unknown function](#iunknowngetunknown-function)|Returns the address of the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) as a pointer to **IUnknown**; this function helps you call methods (such as COM methods) that expect a pointer to **IUnknown**.|
|[put_abi function](#iunknownputabi-function)|Returns the address of the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer as a pointer to a pointer to **void**; this function helps you call methods (such as COM methods) that return references as out parameters via a pointer to a pointer to **void**.|
|[swap function](#swap-function)|Swaps the contents of the two **IUnknown** parameters so that they point at one another's target.|

## Free operators
|Function|Description|
|------------|-----------------|
|[operator!= (inequality operator)](#operator-inequality-operator)|Returns a value indicating whether the two parameters refer to different targets.|
|[operator< (less-than operator)](#operator-less-than-operator)|Returns a value indicating whether the first parameter's target occurs earlier in memory than that of the second parameter.|
|[operator<= (less-than-or-equal-to operator)](#operator-less-than-or-equal-to-operator)|Returns a value indicating whether the first parameter's target occurs earlier in memory than, or at the same location as, that of the second parameter.|
|[operator== (equality operator)](#operator-equality-operator)|Returns a value indicating whether the two parameters refer to the same interface and/or object.|
|[operator> (greater-than operator)](#operator-greater-than-operator)|Returns a value indicating whether the first parameter's target occurs later in memory than that of the second parameter.|
|[operator>= (greater-than-or-equal-to operator)](#operator-greater-than-or-equal-to-operator)|Returns a value indicating whether the first parameter's target occurs later in memory than, or at the same location as, that of the second parameter.|

## IUnknown::IUnknown constructor
Initializes a new instance of the **IUnknown** struct, optionally with a copy or move of the input data.

### Syntax
```cppwinrt
IUnknown() noexcept;
IUnknown(std::nullptr_t) noexcept;
IUnknown(winrt::Windows::Foundation::IUnknown const& other) noexcept;
IUnknown(winrt::Windows::Foundation::IUnknown&& other) noexcept;
```

### Parameters
`other`
Another **IUnknown** that initializes the **IUnknown** object.

## IUnknown::as function
Returns the requested interface, if it is supported. Throws if it is not. This function is useful if you want to query for an interface that you don't need to pass back to your caller.

### Syntax
```cppwinrt
template <typename To> auto as() const;
template <typename To> void as(To& to) const;
```

### Template parameters
`typename To`
The type of the requested interface.

### Parameters
`to`
A reference to a value to receive the requested interface.

### Return value 
A **com_ptr** referencing the requested interface, or a strongly-typed smart pointer for the requested interface (either declared by C++/WinRT or by a third party).

## IUnknown::try_as function
Returns the requested interface, if it is supported. Returns `null` (the `auto`-returning overload), or `false` (the `bool`-returning overload), if it is not. This function is useful if you want to query for an interface that you don't need to pass back to your caller.

### Syntax
```cppwinrt
template <typename To> auto try_as() const noexcept;
template <typename To> bool try_as(To& to) const noexcept;
```

### Template parameters
`typename To`
The type of the requested interface.

### Parameters
`to`
A reference to a value to receive the requested interface.

### Return value 
A **com_ptr** referencing the requested interface, or a strongly-typed smart pointer for the requested interface (either declared by C++/WinRT or by a third party), if the requested interface is supported, otherwise `null` (the `auto`-returning overload) or `false` (the `bool`-returning overload).

## IUnknown::operator bool
Checks whether or not the **IUnknown** object is referencing an interface. If the **IUnknown** object is not referencing an interface, then it is logically null; otherwise it is logically not null.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **IUnknown** object is referencing an interface (logically not null), otherwise `false` (logically null).

## IUnknown::operator= (assignment operator)
Assigns a value to the **IUnknown** object.

### Syntax
```cppwinrt
winrt::Windows::Foundation::IUnknown& operator=(winrt::Windows::Foundation::IUnknown const& other) noexcept;
winrt::Windows::Foundation::IUnknown& operator=(winrt::Windows::Foundation::IUnknown&& other) noexcept;
winrt::Windows::Foundation::IUnknown& operator=(std::nullptr_t) noexcept;
```

### Parameters
`other`
An **IUnknown** value to assign to the **IUnknown** object, either by copy or by move.

### Return value
A reference to the **IUnknown** object.

## attach_abi function
Attaches an **IUnknown** object to a raw pointer that owns a reference to its target; an additional reference is not added. If needed, you can use this function to coalesce references.

### Syntax
```cppwinrt
void attach_abi(winrt::Windows::Foundation::IUnknown& object, void* value) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

`value`
A raw pointer that owns a reference to its target.

## copy_from_abi function
Copies to an **IUnknown** object from another pointer. Decrements the reference count on any currently referenced interface or object, copies the raw pointer parameter, and begins managing the lifetime of the interface or object pointed to by it.

### Syntax
```cppwinrt
void copy_from_abi(winrt::Windows::Foundation::IUnknown& object, void* value) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

`value`
A raw pointer to a target whose lifetime should be managed by the **IUnknown** object.

## copy_to_abi function
Copies to another pointer from an **IUnknown** object. Increments the reference count on any currently referenced interface or object, and copies that interface or object's memory address into the parameter. This function lets you hand out a reference to the same interface without calling [QueryInterface](https://msdn.microsoft.com/library/windows/desktop/ms682521).

### Syntax
```cppwinrt
void copy_to_abi(winrt::Windows::Foundation::IUnknown const& object, void*& value) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

`value`
A raw pointer reference; via which to copy the pointer to the **IUnknown** object's target.

## detach_abi function
Detaches an **IUnknown** object from its raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) without decrementing the reference count, perhaps to return it to a caller.

### Syntax
```cppwinrt
void* detach_abi(winrt::Windows::Foundation::IUnknown& object) noexcept;
void* detach_abi(winrt::Windows::Foundation::IUnknown&& object) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

### Return value
A pointer to the raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) referenced by the **IUnknown** object.

## get_abi function
Returns the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer should you need to pass it to a function. You may call [AddRef](https://msdn.microsoft.com/library/windows/desktop/ms691379), [Release](https://msdn.microsoft.com/library/windows/desktop/ms682317), or [QueryInterface](https://msdn.microsoft.com/library/windows/desktop/ms682521) on the returned pointer.

### Syntax
```cppwinrt
void* get_abi(winrt::Windows::Foundation::IUnknown const& object) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

### Return value 
A pointer to the raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) referenced by the **IUnknown** object.

## get_unknown function
Returns the address of the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) as a pointer to **IUnknown**; this function helps you call methods (such as COM methods) that expect a pointer to **IUnknown**.

### Syntax
```cppwinrt
::IUnknown* get_unknown(winrt::Windows::Foundation::IUnknown const& object) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

### Return value 
The address of the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) as a pointer to **IUnknown**.

## operator!= (inequality operator)
Returns a value indicating whether the two parameters refer to different targets.

### Syntax
```cppwinrt
bool operator!=(winrt::Windows::Foundation::IUnknown const& left, winrt::Windows::Foundation::IUnknown const& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the two parameters point to different targets, otherwise `false`.

## operator< (less-than operator)
Returns a value indicating whether the first parameter's target occurs earlier in memory than that of the second parameter.

### Syntax
```cppwinrt
bool operator<(winrt::Windows::Foundation::IUnknown const& left, winrt::Windows::Foundation::IUnknown const& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is less than that of the second parameter, otherwise `false`.

## operator<= (less-than-or-equal-to operator)
Returns a value indicating whether the first parameter's target occurs earlier in memory than, or at the same location as, that of the second parameter.

### Syntax
```cppwinrt
bool operator<=(winrt::Windows::Foundation::IUnknown const& left, winrt::Windows::Foundation::IUnknown const& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is less than or equal to that of the second parameter, otherwise `false`.

## operator== (equality operator)
Returns a value indicating whether the two parameters refer to the same interface and/or object.

### Syntax
```cppwinrt
bool operator==(winrt::Windows::Foundation::IUnknown const& left, winrt::Windows::Foundation::IUnknown const& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the two parameters point to the same target, otherwise `false`.

## operator> (greater-than operator)
Returns a value indicating whether the first parameter's target occurs later in memory than that of the second parameter.

### Syntax
```cppwinrt
bool operator>(winrt::Windows::Foundation::IUnknown const& left, winrt::Windows::Foundation::IUnknown const& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is greater than that of the second parameter, otherwise `false`.

## operator>= (greater-than-or-equal-to operator)
Returns a value indicating whether the first parameter's target occurs later in memory than, or at the same location as, that of the second parameter.

### Syntax
```cppwinrt
bool operator>=(winrt::Windows::Foundation::IUnknown const& left, winrt::Windows::Foundation::IUnknown const& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is greater than or equal to that of the second parameter, otherwise `false`.

## put_abi function
Returns the address of the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer as a pointer to a pointer to **void**; this function helps you call methods (such as COM methods) that return references as out parameters via a pointer to a pointer to **void**.

### Syntax
```cppwinrt
void** put_abi(winrt::Windows::Foundation::IUnknown& object) noexcept;
```

### Parameters
`object`
An **IUnknown** value to operate on.

### Return value 
The address of the underlying raw [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer.

## swap function
Swaps the contents of the two **IUnknown** parameters so that they point at one another's target.

### Syntax
```cppwinrt
void swap(winrt::Windows::Foundation::IUnknown& left, winrt::Windows::Foundation::IUnknown& right) noexcept;
```

### Parameters
`left` `right`
An **IUnknown** value whose pointers to mutually swap with that of the other parameter.

## See also 
* [winrt namespace](winrt.md)
