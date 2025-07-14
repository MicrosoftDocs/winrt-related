---

description: A type that you can use to declare a custom delegate type for your own events.
title: winrt::delegate struct template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/24/2018
ms.topic: reference
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, delegate, handler
ms.workload: ["cplusplus"]
---

# winrt::delegate struct template (C++/WinRT)
A type that you can use to declare a custom delegate type for your own events. **delegate** supports any number of parameters, and they are not limited to Windows Runtime types.

The **delegate** type has no ABI (it has no interface for use across application binaries), so its use case is when you're both authoring and consuming an event within the same project. For more details of that scenario, see [Parameterized delegates, simple signals, and callbacks within a project](/windows/uwp/cpp-and-winrt-apis/author-events#parameterized-delegates-simple-signals-and-callbacks-within-a-project).

For more info about handling events, and code examples, see [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events).

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

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

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
delegate(std::nullptr_t = nullptr) noexcept; // (1)

template <typename L>
delegate(L lHandler); // (2)

template <typename F>
delegate(F* fHandler); // (3)

template <typename O, typename M>
delegate(O* object, M method); // (4)

template <typename O, typename M>
delegate(winrt::com_ptr<O>&& object, M method); // (5)

template <typename O, typename M>
delegate(winrt::weak_ref<O>&& object, M method); // (6)

template <typename O, typename M>
delegate(winrt::weak_ref<O>&& object, L lHandler); // (7)

template <typename O, typename M>
delegate(std::shared_ptr<O>&& object, M method); // (8)

template <typename O, typename M>
delegate(std::weak_ptr<O>&& object, M method); // (9)

template <typename O, typename M>
delegate(std::weak_ptr<O>&& object, L lHandler); // (10)
```

### Template parameters
`typename L`
A lambda type, or more generally, any type that supports function call syntax, such as a `std::function`.

`typename F`
A free function type.

`typename O`
An object type.

`typename M`
A pointer-to-member-function type.

### Parameters
`lHandler`
A lambda object, or more generally, an object that supports function call syntax, such as a `std::function`, which will handle the event.

`fHandler`
A pointer-to-free-function, which will handle the event.

`object`
An object, one of whose member functions will handle the event.
Depending on the overload, this object may be represented by a raw pointer or a smart pointer.

`method`
A pointer-to-member-function, which will handle the event.

### Remarks

The default constructor (1) constructs an empty delegate.

Constructor (2) constructs a delegate which calls the lambda with the delegate arguments.

Constructor (3) constructs a delegate which calls the function with the delegate arguments.

Constructor (4) constructs a delegate which calls the pointed-to object's method with the delegate arguments.

Constructor (5) constructs a delegate which calls the referenced object's method with the delegate arguments.

Constructor (6) constructs a delegate which attempts to resolve the `weak_ref` to a strong reference.
If successful, then it calls the object's method with the delegate arguments; otherwise, it does nothing.

Constructor (7) constructs a delegate which attempts to resolve the `weak_ref` to a strong reference.
If successful, then it calls the lambda with the delegate arguments; otherwise, it does nothing.
Requires C++/WinRT version 2.0.240111.5.

Constructor (8) constructs a delegate which calls the shared object's method with the delegate arguments.
Requires C++/WinRT version 2.0.240111.5.

Constructor (9) constructs a delegate which attempts to resolve the `weak_ptr` to a shared pointer.
If successful, then it calls the shared object's method with the delegate arguments; otherwise, it does nothing.
Requires C++/WinRT version 2.0.240111.5.

Constructor (10) constructs a delegate which attempts to resolve the `weak_ptr` to a shared pointer.
If successful, then it calls the lambda with the delegate arguments; otherwise, it does nothing.
Requires C++/WinRT version 2.0.240111.5.

## delegate::operator() (function call operator)
Invokes the delegate represented by the **delegate** object with the provided arguments.

### Syntax
```cppwinrt
void operator()(T const&... args) const
```

## See also
* [winrt namespace](winrt.md)
* [Author events in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-events)
* [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events)
* [winrt::event struct template](event.md)
