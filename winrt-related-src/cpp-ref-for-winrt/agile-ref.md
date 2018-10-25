---
author: stevewhims
description: A type representing an agile reference to a C++/WinRT object or interface.
title: winrt::agile_ref struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/19/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, agile
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::agile_ref struct template (C++/WinRT)
A type representing an agile reference to a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) object or interface. For more info, and code examples, see [Agile objects in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/agile-objects).

## Syntax
```cppwinrt
template <typename T>
struct agile_ref
```

### Template parameters
`typename T`
The type of C++/WinRT object or interface an agile reference to which is represented by the **agile_ref** object. This is the type of the agile reference's target.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[agile_ref::agile_ref constructor](#agilerefagileref-constructor)|Initializes a new instance of the **agile_ref** struct, optionally with a copy of the input data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[agile_ref::get function](#agilerefget-function)|Retrieves a proxy to the target of the **agile_ref** object that may safely be used within any thread context in which **get** is called.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[agile_ref::operator bool](#agilerefoperator-bool)|Checks whether the **agile_ref** object is targeting a C++/WinRT object.|

## agile_ref::agile_ref constructor
Initializes a new instance of the **agile_ref** struct, optionally with a copy of the input data.

### Syntax
```cppwinrt
agile_ref(std::nullptr_t = nullptr) noexcept;
agile_ref(T const& object);
```

### Parameters
`object`
A C++/WinRT object or interface that initializes the **agile_ref** object.

## agile_ref::get function
Retrieves a proxy to the target of the **agile_ref** object, which may safely be used within any thread context in which **get** is called.

### Syntax
```cppwinrt
T get() const;
```

### Return value 
A proxy to the C++/WinRT object or interface referenced by the **agile_ref** object.

## agile_ref::operator bool
Checks whether the **agile_ref** object is targeting a valid C++/WinRT object or interface.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **agile_ref** object has a valid target, otherwise `false`.

## See also 
* [winrt namespace](winrt.md)
* [Agile objects in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/agile-objects)
