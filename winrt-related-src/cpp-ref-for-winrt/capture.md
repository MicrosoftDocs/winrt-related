---
description: A function template that calls a specified function or method, captures the resulting interface pointer, and returns it as a [winrt::com_ptr](./com-ptr.md).
title: winrt::capture function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 06/16/2020
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, capture
ms.workload: ["cplusplus"]
---

# winrt::capture function template (C++/WinRT)

A function template that calls a specified function or method (automatically calling [winrt::check_hresult](./error-handling/check-hresult.md) on it), captures the interface pointer that's output from the function or method, and returns it as the template parameter `typename T` if `T` derives from **Windows::Foundation::IUnknown**, otherwise, returns a [winrt::com_ptr](./com-ptr.md). Throws if not successful.

Also see the [winrt::com_ptr::capture function](./com-ptr.md#com_ptrcapture-function).

## Syntax

```cppwinrt
template <typename T, typename F, typename...Args>
impl::com_ref<T> capture(F function, Args&& ...args);

template <typename T, typename O, typename M, typename...Args>
impl::com_ref<T> capture(O* p, M method, Args&& ...args);

template <typename T, typename O, typename M, typename...Args>
impl::com_ref<T> capture(com_ptr<O> const& object, M method, Args&& ...args);
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

`p`
A pointer to an object of type `O`.

`object`
A **winrt::com_ptr** of type `O`.

`method`
A method (implemented by `O`) of type `M`.

`args`
Zero or more arguments of type `Args`.

### Return value

Returns `T` if `T` derives from **Windows::Foundation::IUnknown**, otherwise, returns [winrt::com_ptr](./com-ptr.md). Throws if not successful.

### Remarks

- The `capture(F function, Args&&...args)` overload invokes the function object.
- The `capture(O* p, M method, Args&& ...args)` overload invokes the method on the pointer.
- The `capture(winrt::com_ptr<O> const& object, M method, Args&&...args)` overload invokes the method on the object.

All overloads pass through (to the invokee) any additional arguments that you provide. All overloads also pass the two additional arguments that such invokees require&mdash;specifically, a **REFIID** (the ID of the target of the **winrt::com_ptr**), and a **void\*\*** (The address of a pointer to the target of the **winrt::com_ptr**).

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 

* [winrt namespace](./winrt.md)
* [try_capture function template](./try-capture.md)
* [winrt::com_ptr struct template](./com-ptr.md)
* [winrt::com_ptr::capture function](./com-ptr.md#com_ptrcapture-function)
