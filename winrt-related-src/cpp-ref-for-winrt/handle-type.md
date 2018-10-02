---
author: stevewhims
description: The template for the winrt::handle and winrt::file_handle structs.
title: winrt::handle_type struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/14/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::handle_type struct template (C++/WinRT)

The template for the [**winrt::handle**](handle.md) and [**winrt::file_handle**](file-handle.md) structs.

## Syntax
```cppwinrt
template <typename T>
struct handle_type
```

### Template parameters
`typename T`
A traits type that specifies the kind of handle being represented (either a handle or a file handle).

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member type aliases
|Alias name|Type|
|------------|-----------------|
|event::delegate_type|A synonym for **typename T::type**, where **T** is the `typename T` template parameter.|

## Constructors
|Constructor|Description|
|------------|-----------------|
|[handle_type::handle_type constructor](#handletypehandletype-constructor)|Initializes a new instance of the **handle_type** struct, optionally with a copy or move of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[handle_type::attach function](#handletypeattach-function)|Attaches to a HANDLE value, and takes ownership of it.|
|[handle_type::close function](#handletypeclose-function)|Closes the underlying HANDLE.|
|[handle_type::detach function](#handletypedetach-function)|Detaches from the underlying HANDLE.|
|[handle_type::get function](#handletypeget-function)|Returns the underlying HANDLE should you need to pass it to a function.|
|[handle_type::put function](#handletypeput-function)|
Returns the address of the underlying HANDLE; this function helps you call methods that return references as out parameters via a pointer to a HANDLE.
|

## Member operators
|Operator|Description|
|------------|-----------------|
|[handle_type::operator bool](#handletypeoperator-bool)|Checks whether or not the **handle_type** object currently represents a valid HANDLE.|
|[handle_type::operator= (assignment operator)](#handletypeoperator-assignment-operator)|Assigns a value to the **handle_type** object.|

## Free functions
|Function|Description|
|------------|-----------------|
|[swap function](#swap-function)|Swaps the contents of the two **handle_type** parameters so that they contain one another's HANDLE.|

## handle_type::handle_type constructor
Initializes a new instance of the **handle_type** struct, optionally with a copy or move of the input data.

### Syntax
```cppwinrt
handle_type() noexcept;
handle_type(HANDLE value) noexcept;
handle_type(handle_type&& other) noexcept;
```

### Parameters
`value`
A HANDLE value that initializes the **handle_type** object.

`other`
Another **handle_type** that initializes the **handle_type** object.

## handle_type::attach function
Attaches to a HANDLE value, and takes ownership of it.

### Syntax
```cppwinrt
void attach(HANDLE value) noexcept;
```

### Parameters
`value`
A HANDLE value to attach to.

## handle_type::close function
Closes the underlying HANDLE.

### Syntax
```cppwinrt
void close() noexcept;
```

## handle_type::detach function
Detaches from the underlying HANDLE.

### Syntax
```cppwinrt
HANDLE detach() noexcept;
```

### Return value
The underlying HANDLE formerly represented by the **handle_type** object.

## handle_type::get function
Returns the underlying HANDLE should you need to pass it to a function.

### Syntax
```cppwinrt
HANDLE get() const noexcept;
```

### Return value 
The underlying HANDLE represented by the **handle_type** object.

## handle_type::put function
Returns the address of the underlying HANDLE; this function helps you call methods that return references as out parameters via a pointer to a HANDLE.

### Syntax
```cppwinrt
HANDLE* put() noexcept;
```

### Return value 
The address of the underlying HANDLE represented by the **handle_type** object.

## handle_type::operator bool
Checks whether or not the **handle_type** object currently represents a valid HANDLE.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **handle_type** object currently represents a valid HANDLE, otherwise `false`.

## handle_type::operator= (assignment operator)
Assigns a value to the **handle_type** object.

### Syntax
```cppwinrt
winrt::handle_type& operator=(winrt::handle_type&& other) noexcept;
```

### Parameters
`other`
A **handle_type** value to assign to the **handle_type** object.

### Return value
A reference to the **handle_type** object.

## swap function
Swaps the contents of the two **handle_type** parameters so that they contain one another's HANDLE.

### Syntax
```cppwinrt
void swap(winrt::handle_type& left, winrt::handle_type& right) noexcept;
```

### Parameters
`left` `right`
A **handle_type** value whose HANDLE to mutually swap with that of the other parameter.

## See also 
* [winrt namespace](winrt.md)
* [winrt::handle struct](handle.md)
* [winrt::file_handle struct](file-handle.md)
