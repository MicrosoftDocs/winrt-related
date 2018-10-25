---
author: stevewhims
description: A type representing a weak reference to a C++/WinRT object or interface.
title: winrt::weak_ref struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/10/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, weak
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::weak_ref struct template (C++/WinRT)

A type representing a weak reference to a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object or interface. For more info, and code examples, see [Strong and weak references in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/weak-references).

## Syntax
```cppwinrt
template <typename T>
struct weak_ref
```

### Template parameters
`typename T`
The type of C++/WinRT object or interface a weak reference to which is represented by the **weak_ref** object. This is the type of the weak reference's target.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[weak_ref::weak_ref constructor](#weakrefweakref-constructor)|Initializes a new instance of the **weak_ref** struct, optionally with a copy of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[weak_ref::get function](#weakrefget-function)|Increments the reference count and retrieves the C++/WinRT object or interface weakly referenced by the **weak_ref** object.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[weak_ref::operator bool](#weakrefoperator-bool)|Checks whether the **weak_ref** object is targeting a C++/WinRT object that hasn't yet been destroyed.|

## weak_ref::weak_ref constructor
Initializes a new instance of the **weak_ref** struct, optionally with a copy of the input data.

### Syntax
```cppwinrt
weak_ref(std::nullptr_t = nullptr) noexcept;
weak_ref(T const& object);
weak_ref(com_ptr<T> const& object);
```

### Parameters
`object`
A C++/WinRT object or interface or smart pointer that initializes the **weak_ref** object.

## weak_ref::get function
Increments the reference count and retrieves the C++/WinRT object or interface weakly referenced by the **weak_ref** object.

### Syntax
```cppwinrt
auto get() const noexcept;
```

### Return value 
The C++/WinRT object or interface weakly referenced by the **weak_ref** object, or `nullptr` if the weak reference's target has been destroyed.

## weak_ref::operator bool
Checks whether the **weak_ref** object is targeting a C++/WinRT object that hasn't yet been destroyed.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **weak_ref** object is targeting a C++/WinRT object that hasn't yet been destroyed, otherwise `false`.

## See also 
* [winrt namespace](winrt.md)
* [Strong and weak references in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/weak-references)
