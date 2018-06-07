---
author: stevewhims
description: A type that you can use to declare and implement an event of a specified delegate type.
title: winrt::event struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/25/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, event, delegate
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::event struct template ([C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt))
A type that you can use to declare and implement an event of a specified delegate type. Subscribers pass their event-handling delegates to an event; the event registers those delegates in a collection; then, when it is raised, the event invokes its registered delegates in turn so that subscribers can handle the event. For more info about authoring events, and code examples, see [Author events in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-events).

## Syntax
```cppwinrt
template <typename Delegate>
struct event
```

### Template parameters
`typename Delegate`
The type of delegate that can register to handle the event.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member type aliases
|Alias name|Type|
|------------|-----------------|
|event::delegate_type|A synonym for the `typename Delegate` template parameter.|

## Constructors
|Constructor|Description|
|------------|-----------------|
|[event::event constructor](#eventevent-constructor)|Initializes a new instance of the **event** struct.|

## Member functions
|Function|Description|
|------------|-----------------|
|[event::add function](#eventadd-function)|Registers a delegate with the **event** object.|
|[event::remove function](#eventremove-function)|Revokes a delegate's registration from the **event** object.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[event::operator() (function call operator)](#eventoperator-function-call-operator)|Invokes all of the **event** object's registered delegates with the provided arguments.|
|[event::operator bool](#eventoperator-bool)|Checks whether the **event** object has any delegates registered with it.|

## event::event constructor
Initializes a new instance of the **event** struct.

### Syntax
```cppwinrt
event();
```

## event::add function
Registers a delegate with the **event** object.

### Syntax
```cppwinrt
winrt::event_token add(Delegate const& delegate);
```

### Parameters
`delegate`
A delegate to register with the **event** object.

### Return value 
A [**winrt::event_token**](event-token.md) that can subsequently be used to revoke the delegate's registration.

## event::operator() (function call operator)
Invokes all of the **event** object's registered delegates with the provided arguments.

### Syntax
```cppwinrt
template<typename... Arg>
void operator()(Arg const&... args)
```

### Template parameters
`typename... Arg`
A variadic template parameter pack containing the types of the parameters that the delegate is passed when it's called.

### Parameters
`args`
A variable argument list containing the arguments that the delegate is passed when it's called.

## event::operator bool
Checks whether the **event** object has any delegates registered with it.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **event** object has any registered delegates, otherwise `false`.

## event::remove function
Revokes a delegate's registration from the **event** object.

### Syntax
```cppwinrt
void remove(winrt::event_token const token);
```

### Parameters
`token`
A [**winrt::event_token**](event-token.md) that identifies the delegate whose registration to revoke.

## See also
* [winrt namespace](winrt.md)
* [Author events in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-events)
* [winrt::delegate struct template](delegate.md)
* [winrt::event_token struct](event-token.md)
