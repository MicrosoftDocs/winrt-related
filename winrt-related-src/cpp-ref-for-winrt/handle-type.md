---

description: The template for the winrt::handle and winrt::file_handle structs.
title: winrt::handle_type struct template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 05/14/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::handle_type struct template (C++/WinRT)

The template for the [**winrt::handle**](handle.md) and [**winrt::file_handle**](file-handle.md) structs, among others.

> [!NOTE]
> You can define your own handle traits (see, for example, **handle_traits** or **file_handle_traits** in `\cppwinrt\winrt\base.h`), and use them with **winrt::handle_type** as `typename T`. Copy one of those examples from `base.h` into your own source code file, and provide your own handle type and implementation. There are more details in the MSDN Magazine article [Windows with C++](/archive/msdn-magazine/2011/july/msdn-magazine-windows-with-c-c-and-the-windows-api).

## Syntax
```cppwinrt
template <typename T>
struct handle_type
```

### Template parameters
`typename T`
A traits type that specifies the kind of handle being represented (a handle, a file handle, or some other type).

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member type aliases
|Alias name|Type|
|------------|-----------------|
|handle_type::type|A synonym for **typename T::type**, where **T** is the `typename T` template parameter.|

## Constructors
|Constructor|Description|
|------------|-----------------|
|[handle_type::handle_type constructor](#handle_typehandle_type-constructor)|Initializes a new instance of the **handle_type** struct, optionally with a copy or move of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[handle_type::attach function](#handle_typeattach-function)|Attaches to a handle value, and takes ownership of it.|
|[handle_type::close function](#handle_typeclose-function)|Closes the underlying handle.|
|[handle_type::detach function](#handle_typedetach-function)|Detaches from the underlying handle.|
|[handle_type::get function](#handle_typeget-function)|Returns the underlying handle should you need to pass it to a function.|
|[handle_type::put function](#handle_typeput-function)|Returns the address of the underlying handle; this function helps you call methods that return references as out parameters via a pointer to a handle.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[handle_type::operator bool](#handle_typeoperator-bool)|Checks whether or not the **handle_type** object currently represents a valid handle.|
|[handle_type::operator= (assignment operator)](#handle_typeoperator-assignment-operator)|Assigns a value to the **handle_type** object.|

## Free functions
|Function|Description|
|------------|-----------------|
|[swap function](#swap-function)|Swaps the contents of the two **handle_type** parameters so that they contain one another's handle.|

## handle_type::handle_type constructor
Initializes a new instance of the **handle_type** struct, optionally with a copy or move of the input data.

### Syntax
```cppwinrt
handle_type() noexcept;
explicit handle_type(handle_type::type value) noexcept;
handle_type(handle_type&& other) noexcept;
```

### Parameters
`value`
A value that initializes the **handle_type** object.

`other`
Another **handle_type** that initializes the **handle_type** object.

## handle_type::attach function
Attaches to a handle value, and takes ownership of it.

### Syntax
```cppwinrt
void attach(handle_type::type value) noexcept;
```

### Parameters
`value`
A handle value to attach to.

## handle_type::close function
Closes the underlying handle.

### Syntax
```cppwinrt
void close() noexcept;
```

## handle_type::detach function
Detaches from the underlying handle.

### Syntax
```cppwinrt
handle_type::type detach() noexcept;
```

### Return value
The underlying handle formerly represented by the **handle_type** object.

## handle_type::get function
Returns the underlying handle, should you need to pass it to a function.

### Syntax
```cppwinrt
handle_type::type get() const noexcept;
```

### Return value 
The underlying handle represented by the **handle_type** object.

## handle_type::put function
Returns the address of the underlying handle; this function helps you call methods that return references as out parameters via a pointer to a handle.

### Syntax
```cppwinrt
handle_type::type* put() noexcept;
```

### Return value 
The address of the underlying handle represented by the **handle_type** object.

## handle_type::operator bool
Checks whether or not the **handle_type** object currently represents a valid handle.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **handle_type** object currently represents a valid handle, otherwise `false`.

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
Swaps the contents of the two **handle_type** parameters so that they contain one another's handle.

### Syntax
```cppwinrt
void swap(winrt::handle_type& left, winrt::handle_type& right) noexcept;
```

### Parameters
`left` `right`
A **handle_type** value whose handle to mutually swap with that of the other parameter.

## See also 
* [winrt namespace](winrt.md)
* [winrt::handle struct](handle.md)
* [winrt::file_handle struct](file-handle.md)
