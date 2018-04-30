---
author: stevewhims
description: A type that you can use to declare a custom delegate type for your own events.
title: winrt::delegate struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "jillfra"
ms.date: 04/24/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, delegate, handler
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::delegate struct template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A type that you can use to declare a custom delegate type for your own events in cases where you need to support passing non-C++/WinRT types as delegate parameters. For more info about handling events, and code examples, see [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events).

## Syntax
```cppwinrt
template <typename... T>
struct delegate : Windows::Foundation::IUnknown
```

### Template parameters
`typename... T`
A variadic template parameter pack containing the types of the parameters that the delegate is passed when it's called.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[delegate::delegate constructor](#delegatedelegate-constructor)|Initializes a new instance of the **delegate** struct from the input data.|

## Member operators
|Operator|Description| 
|------------|-----------------|
|[delegate::operator() (function call operator)](#delegateoperator-function-call-operator)|Invokes the delegate represented by the **delegate** object with the provided arguments.|

## delegate::delegate constructor
Initializes a new instance of the **delegate** struct from the input data.

### Syntax
```cppwinrt
delegate(std::nullptr_t = nullptr) noexcept;

template <typename L>
delegate(L lHandler);

template <typename F>
delegate(F* fHandler);

template <typename O, typename M>
delegate(O* object, M method);
```

### Template parameters
`typename L`
A lambda function type.

`typename F`
A free function type.

`typename O`
An object type.

`typename M`
A pointer-to-member-function type.

### Parameters
`lHandler`
A lambda function, which will handle the event.

`fHandler`
A pointer-to-free-function, which will handle the event.

`object`
A pointer to an object, one of whose member functions will handle the event.

`method`
A pointer-to-member-function, which will handle the event.

## delegate::operator() (function call operator)
Invokes the delegate represented by the **delegate** object with the provided arguments.

### Syntax
```cppwinrt
void operator()(T const&... args) const
```

## See also
* [winrt namespace](winrt.md)
* [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events)
* [winrt::event struct template](event.md)
