---

description: A token returned when registering an event-handling delegate with an event; can be used to revoke the registration of the same delegate.
title: winrt::event_token struct (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/25/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, delegate, handler
ms.workload: ["cplusplus"]
---

# winrt::event_token struct (C++/WinRT)
A token returned when registering an event-handling delegate with an event; can be used to revoke the registration of the same delegate. For more info about handling events, and code examples, see [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events).

## Syntax
```cppwinrt
struct event_token
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Data members
|Function|Description|
|------------|-----------------|
|[event_token::value data member](#event_tokenvalue-data-member)|An opaque numeric value uniquely representing the registration of a delegate with an event.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[event_token::operator bool](#event_tokenoperator-bool)|Checks whether or not the **event_token** object is valid and initialized.|

## Free operators
|Operator|Description|
|------------|-----------------|
|[operator== (equality operator)](#operator-equality-operator)|Returns a value indicating whether the two parameters are equal to one another.|

## event_token::operator bool
Checks whether or not the **event_token** object is valid and initialized.

### Syntax
```cppwinrt
explicit operator bool() const noexcept;
```

### Return value
`true` if the **event_token** object is valid and initialized (the value of its `value` field is not zero), otherwise `false`.

## event_token::value data member
An opaque numeric value uniquely representing the registration of a delegate with an event.

### Syntax
```cppwinrt
int64_t value{};
```

## operator== (equality operator)
Returns a value indicating whether the two parameters are equal to one another.

### Syntax
```cppwinrt
inline bool operator==(winrt::event_token const& left, winrt::event_token const& right) noexcept;
```

### Parameters
`left` `right`
An **event_token** value to compare with the other parameter.

### Return value
`true` if the two parameters are equal to one another, otherwise `false`.

## See also 
* [winrt namespace](winrt.md)
* [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events)
* [winrt::event struct template](event.md)
