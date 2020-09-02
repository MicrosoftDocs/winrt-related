---
description: A function template that calls a specified function or method, captures the interface pointer that's output from the function or method, and returns it as a [winrt::com_ptr](./com-ptr.md) or an empty **com_ptr** if not successful.
title: winrt::try_capture function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 06/16/2020
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, try_capture
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::try_capture function template (C++/WinRT)

A function template that calls a specified function or method (automatically calling [winrt::check_hresult](./error-handling/check-hresult.md) on it), captures the interface pointer that's output from the function or method, and returns it as a [winrt::com_ptr](./com-ptr.md) or an empty **com_ptr** if not successful.

Also see the [winrt::com_ptr::try_capture function](./com-ptr.md#com_ptrtry_capture-function).

## Syntax

```cppwinrt
template <typename T, typename F, typename...Args>
winrt::com_ptr<T> try_capture(F function, Args&& ...args);

template <typename T, typename O, typename M, typename...Args>
winrt::com_ptr<T> try_capture(com_ptr<O> const& object, M method, Args&& ...args);
```

### Template parameters

`typename T`
The type of the interface pointer that's output from the function or method.

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

`method`
A method (implemented by `O`) of type `M`.

`args`
Zero or more arguments of type `Args`.

### Remarks

- The `try_capture(F function, Args&&...args)` overload invokes the function object.
- The `try_capture(winrt::com_ptr<O> const& object, M method, Args&&...args)` overload invokes the method on the object.

Both overloads pass through (to the invokee) any additional arguments that you provide. Both overloads also pass the two additional arguments that such invokees require&mdash;specifically, a **REFIID** (the ID of the target of the **winrt::com_ptr**), and a **void\*\*** (The address of a pointer to the target of the **winrt::com_ptr**).

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 

* [winrt namespace](./winrt.md)
* [capture function template](./capture.md)
* [winrt::com_ptr struct template](./com-ptr.md)
* [winrt::com_ptr::try_capture function](./com-ptr.md#com_ptrtry_capture-function)