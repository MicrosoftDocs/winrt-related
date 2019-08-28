---
author: stevewhims
description: A reference-counted COM smart pointer template.
title: winrt::com_ptr struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/10/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, com, smart, pointer
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::com_ptr struct template (C++/WinRT)
A reference-counted COM smart pointer template. **com_ptr** represents a pointer to the interface or runtime class implementation type specified by the template parameter. It automatically manages the reference count for its target through a private raw pointer.

## Syntax
```cppwinrt
template <typename T>
struct com_ptr
```

### Template parameters
`typename T`
The interface, or runtime class implementation type, a pointer to which is represented by the **com_ptr**. This is the type of the smart pointer's target.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member type aliases
|Alias name|Type|
|------------|-----------------|
|com_ptr::type|A synonym for an implementation-defined representation of the `typename T` template parameter.|

## Constructors
|Constructor|Description|
|------------|-----------------|
|[com_ptr::com_ptr constructor](#com_ptrcom_ptr-constructor)|Initializes a new instance of the **com_ptr** struct, optionally with a copy or move of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[com_ptr::as function](#com_ptras-function)|Returns the requested interface, if it is supported. Throws if it is not.|
|[com_ptr::attach function](#com_ptrattach-function)|Attaches to a raw pointer that owns a reference to its target; an additional reference is not added.|
|[com_ptr::capture function](#com_ptrcapture-function)|Calls a specified function or method (automatically calling [winrt::check_hresult](/uwp/cpp-ref-for-winrt/error-handling/check-hresult) on it), and captures the interface pointer that's output from the function or method as a `void**`.|
|[com_ptr::copy_from function](#com_ptrcopy_from-function)|Copies from another pointer. Decrements the reference count on any currently referenced interface or object, copies the raw pointer parameter, and begins managing the lifetime of the interface or object pointed to by it.|
|[com_ptr::copy_to function](#com_ptrcopy_to-function)|Copies to another pointer from the **com_ptr** object. Increments the reference count on any currently referenced interface or object, and copies that interface or object's memory address into the parameter.|
|[com_ptr::detach function](#com_ptrdetach-function)|Detaches from the referenced interface or object without decrementing the reference count, perhaps to return it to a caller.|
|[com_ptr::get function](#com_ptrget-function)|Returns the underlying raw pointer should you need to pass it to a function.|
|[com_ptr::put function](#com_ptrput-function)|Returns the address of the underlying raw pointer; this function helps you call methods (such as COM methods) that return references as out parameters via a pointer to a pointer.|
|[com_ptr::put_void function](#com_ptrput_void-function)|Returns the address of the underlying raw pointer as a pointer to a pointer to **void**; this function helps you call methods (such as COM methods) that return references as out parameters via a pointer to a pointer to **void**.|
|[com_ptr::try_as function](#com_ptrtry_as-function)|Returns the requested interface, if it is supported. Returns `nullptr`, or `false`, if it is not.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[com_ptr::operator bool](#com_ptroperator-bool)|Checks whether or not the smart pointer is referencing an interface or object.|
|[com_ptr::operator* (indirection operator)](#com_ptroperator-indirection-operator)|Returns a reference to the **com_ptr**'s target so that you can pass it to a function that expects a reference to the target type **T**.|
|[com_ptr::operator= (assignment operator)](#com_ptroperator-assignment-operator)|Assigns a value to the **com_ptr** object.|
|[com_ptr::operator-> (arrow operator)](#com_ptroperator--arrow-operator)|To afford access to the referenced interface or object's methods, returns the underlying raw pointer.|

## Free functions
|Function|Description|
|------------|-----------------|
|[attach_abi function](#attach_abi-function)|Attaches a **com_ptr** object to a raw pointer that owns a reference to its target; an additional reference is not added.|
|[detach_abi function](#detach_abi-function)|Detaches a **com_ptr** object from its raw interface without decrementing the reference count, perhaps to return it to a caller.|
|[swap function](#swap-function)|Swaps the contents of the two **com_ptr** parameters so that they point at one another's target.|

## Free operators
|Function|Description|
|------------|-----------------|
|[operator!= (inequality operator)](#operator-inequality-operator)|Returns a value indicating whether the two parameters refer to different targets.|
|[operator< (less-than operator)](#operator-less-than-operator)|Returns a value indicating whether the first parameter's target occurs earlier in memory than that of the second parameter.|
|[operator<= (less-than-or-equal-to operator)](#operator-less-than-or-equal-to-operator)|Returns a value indicating whether the first parameter's target occurs earlier in memory than, or at the same location as, that of the second parameter.|
|[operator== (equality operator)](#operator-equality-operator)|Returns a value indicating whether the two parameters refer to the same interface and/or object.|
|[operator> (greater-than operator)](#operator-greater-than-operator)|Returns a value indicating whether the first parameter's target occurs later in memory than that of the second parameter.|
|[operator>= (greater-than-or-equal-to operator)](#operator-greater-than-or-equal-to-operator)|Returns a value indicating whether the first parameter's target occurs later in memory than, or at the same location as, that of the second parameter.|

## com_ptr::com_ptr constructor
Initializes a new instance of the **com_ptr** struct, optionally with a copy or move of the input data.

### Syntax
```cppwinrt
com_ptr(winrt::com_ptr const& other) noexcept;
com_ptr(std::nullptr_t = nullptr) noexcept;
template <typename U> com_ptr(winrt::com_ptr<U> const& other) noexcept;
template <typename U> com_ptr(winrt::com_ptr<U>&& other) noexcept;
```

### Template parameters
`typename U`
The target type pointed to by the input smart pointer.

### Parameters
`other`
Another **com_ptr** that initializes the **com_ptr** object. The parameter's **T** must be convertible to the **com_ptr** object's **T**.

## com_ptr::as function
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

## com_ptr::attach function
Attaches to a raw pointer that owns a reference to its target; an additional reference is not added. If needed, you can use this function to coalesce references.

### Syntax
```cppwinrt
void attach(T* value) noexcept;
```

### Parameters
`value`
A raw pointer that owns a reference to its target.

## com_ptr::capture function
Calls a specified function or method (automatically calling [winrt::check_hresult](/uwp/cpp-ref-for-winrt/error-handling/check-hresult) on it), and captures the interface pointer that's output from the function or method as a `void**`.

### Syntax
```cppwinrt
template <typename F, typename...Args>
void capture(F function, Args&&...args);

template <typename O, typename M, typename...Args>
void capture(winrt::com_ptr<O> const& object, M method, Args&&...args);
```

### Template parameters
`typename F`
A function object type, such as a free function, or **std::function**.

`typename O`
An interface type.

`typename M`
A method type.

`typename Args`
Zero or more argument types.

### Parameters
`function`
A function object of type `F`.

`object`
A **winrt::com_ptr** of type `O`.

`object`
A method (implemented by `O`) of type `M`.

`args`
Zero or more arguments of type `Args`.

### Remarks

- The `capture(F function, Args&&...args)` overload invokes the function object.
- The `capture(winrt::com_ptr<O> const& object, M method, Args&&...args)` overload invokes the method on the object.

Both overloads pass through (to the invokee) any additional arguments that you provide. Both overloads also pass the two additional arguments that such invokees require&mdash;specifically, a **REFIID** (the ID of the target of the **winrt::com_ptr**), and a **void\*\*** (The address of a pointer to the target of the **winrt::com_ptr**).

### Example

```cppwinrt
winrt::com_ptr<IDXGIAdapter> adapter
...
winrt::com_ptr<IDXGIFactory2> factory;
factory.capture(adapter, &IDXGIAdapter::GetParent);
```

### Return value
A **com_ptr** referencing the requested interface, or a strongly-typed smart pointer for the requested interface (either declared by C++/WinRT or by a third party), if the requested interface is supported, otherwise `nullptr` (the `auto`-returning overload), or `false` (the `bool`-returning overload).

## com_ptr::copy_from function
Copies from another pointer. Decrements the reference count on any currently referenced interface or object, copies the raw pointer parameter, and begins managing the lifetime of the interface or object pointed to by it.

### Syntax
```cppwinrt
void copy_from(T* other) noexcept;
```

### Parameters
`other`
A raw pointer to a target whose lifetime should be managed by the **com_ptr** object.

## com_ptr::copy_to function
Copies to another pointer from the **com_ptr** object. Increments the reference count on any currently referenced interface or object, and copies that interface or object's memory address into the parameter. This function lets you hand out a reference to the same interface without calling [QueryInterface](https://msdn.microsoft.com/library/windows/desktop/ms682521).

### Syntax
```cppwinrt
void copy_to(T** other) const noexcept;
```

### Parameters
`other`
A raw pointer's address; into which to copy the pointer to the **com_ptr** object's target.

## com_ptr::detach function
Detaches from the referenced interface or object without decrementing the reference count, perhaps to return it to a caller.

### Syntax
```cppwinrt
T* detach() noexcept;
```

### Return value
A pointer to the interface or object referenced by the **com_ptr** object.

## com_ptr::get function
Returns the underlying raw pointer should you need to pass it to a function. You may call [AddRef](https://msdn.microsoft.com/library/windows/desktop/ms691379), [Release](https://msdn.microsoft.com/library/windows/desktop/ms682317), or [QueryInterface](https://msdn.microsoft.com/library/windows/desktop/ms682521) on the returned pointer.

### Syntax
```cppwinrt
T* get() const noexcept;
```

### Return value 
A pointer to the interface or object referenced by the **com_ptr** object.

## com_ptr::put function
Returns the address of the underlying raw pointer; this function helps you call methods (such as COM methods) that return references as out parameters via a pointer to a pointer. If the **com_ptr** object already has a target, then assign `nullptr` to the **com_ptr** object before calling this function, otherwise the function will assert.

### Syntax
```cppwinrt
T** put() noexcept;
```

### Return value 
The address of the underlying raw pointer.

## com_ptr::put_void function
Returns the address of the underlying raw pointer as a pointer to a pointer to **void**; this function helps you call methods (such as COM methods) that return references as out parameters via a pointer to a pointer to **void**. If the **com_ptr** object already has a target, then assign `nullptr` to the **com_ptr** object before calling this function, otherwise the function will assert.

### Syntax
```cppwinrt
void** put_void() noexcept;
```

### Return value 
The address of the underlying raw pointer as a pointer to a pointer to **void**.

## com_ptr::try_as function
Returns the requested interface, if it is supported. Returns `nullptr` (the `auto`-returning overload), or `false` (the `bool`-returning overload), if it is not. This function is useful if you want to query for an interface that you don't need to pass back to your caller.

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
A **com_ptr** referencing the requested interface, or a strongly-typed smart pointer for the requested interface (either declared by C++/WinRT or by a third party), if the requested interface is supported, otherwise `nullptr` (the `auto`-returning overload), or `false` (the `bool`-returning overload).

## com_ptr::operator bool
Checks whether or not the smart pointer is referencing an interface or object. If the smart pointer is not referencing an interface or object, then it is logically null; otherwise it is logically not null.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the smart pointer is referencing an interface or object (logically not null), otherwise `false` (logically null).

## com_ptr::operator* (indirection operator)
Returns a reference to the **com_ptr**'s target so that you can pass it to a function that expects a reference to the target type **T**.

### Syntax
```cppwinrt
T& operator*() const noexcept;
```

### Return value
A reference to the **com_ptr**'s target.

## com_ptr::operator= (assignment operator)
Assigns a value to the **com_ptr** object.

### Syntax
```cppwinrt
winrt::com_ptr& operator=(winrt::com_ptr const& other) noexcept;
template <typename U> winrt::com_ptr& operator=(winrt::com_ptr<U> const& other) noexcept;
template <typename U> winrt::com_ptr& operator=(winrt::com_ptr<U>&& other) noexcept;
```

### Template parameters
`typename U`
The type pointed to by the value being assigned.

### Parameters
`other`
A **com_ptr** value to assign to the **com_ptr** object. The parameter's **T** must be convertible to the **com_ptr** object's **T**.

### Return value
A reference to the **com_ptr** object.

## com_ptr::operator-> (arrow operator)
To afford access to the referenced interface or object's methods, returns the underlying raw pointer. You may not call [AddRef](https://msdn.microsoft.com/library/windows/desktop/ms691379) nor [Release](https://msdn.microsoft.com/library/windows/desktop/ms682317) on the returned pointer, but you may call [QueryInterface](https://msdn.microsoft.com/library/windows/desktop/ms682521).

### Syntax
```cppwinrt
auto operator->() const noexcept;
```

### Return value
A pointer to the interface or object referenced by the **com_ptr** object.

## attach_abi function
Attaches a **com_ptr** object to a raw pointer that owns a reference to its target; an additional reference is not added. If needed, you can use this function to coalesce references.

### Syntax
```cppwinrt
void attach_abi(winrt::com_ptr<T>& object, T* value) noexcept;
```

### Parameters
`object`
A **com_ptr** object to operate on.

`value`
A raw pointer that owns a reference to its target.

## detach_abi function
Detaches a **com_ptr** object from its raw interface without decrementing the reference count, perhaps to return it to a caller.

### Syntax
```cppwinrt
auto detach_abi(winrt::com_ptr<T>& object) noexcept;
```

### Parameters
`object`
A **com_ptr** object to operate on.

### Return value
A pointer to the raw interface referenced by the **com_ptr** object.

## operator!= (inequality operator)
Returns a value indicating whether the two parameters refer to different targets.

### Syntax
```cppwinrt
template <typename T> bool operator!=(winrt::com_ptr<T> const& left, winrt::com_ptr<T> const& right) noexcept;
template <typename T> bool operator!=(winrt::com_ptr<T> const& left, std::nullptr_t) noexcept;
template <typename T> bool operator!=(std::nullptr_t, winrt::com_ptr<T> const& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the two parameters point to different targets, otherwise `false`.

## operator< (less-than operator)
Returns a value indicating whether the first parameter's target occurs earlier in memory than that of the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator<(winrt::com_ptr<T> const& left, winrt::com_ptr<T> const& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is less than that of the second parameter, otherwise `false`.

## operator<= (less-than-or-equal-to operator)
Returns a value indicating whether the first parameter's target occurs earlier in memory than, or at the same location as, that of the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator<=(winrt::com_ptr<T> const& left, winrt::com_ptr<T> const& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is less than or equal to that of the second parameter, otherwise `false`.

## operator== (equality operator)
Returns a value indicating whether the two parameters refer to the same interface and/or object.

### Syntax
```cppwinrt
template <typename T> bool operator==(winrt::com_ptr<T> const& left, std::nullptr_t) noexcept;
template <typename T> bool operator==(std::nullptr_t, winrt::com_ptr<T> const& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the two parameters point to the same target, otherwise `false`.

## operator> (greater-than operator)
Returns a value indicating whether the first parameter's target occurs later in memory than that of the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator>(winrt::com_ptr<T> const& left, winrt::com_ptr<T> const& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is greater than that of the second parameter, otherwise `false`.

## operator>= (greater-than-or-equal-to operator)
Returns a value indicating whether the first parameter's target occurs later in memory than, or at the same location as, that of the second parameter.

### Syntax
```cppwinrt
template <typename T> bool operator>=(winrt::com_ptr<T> const& left, winrt::com_ptr<T> const& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose target's memory address to compare with that of the other parameter.

### Return value
`true` if the first parameter's target's memory address is greater than or equal to that of the second parameter, otherwise `false`.

## swap function
Swaps the contents of the two **com_ptr** parameters so that they point at one another's target.

### Syntax
```cppwinrt
void swap(winrt::com_ptr& left, winrt::com_ptr& right) noexcept;
```

### Parameters
`left` `right`
A **com_ptr** value whose pointer to mutually swap with that of the other parameter.

## See also 
* [winrt namespace](winrt.md)
