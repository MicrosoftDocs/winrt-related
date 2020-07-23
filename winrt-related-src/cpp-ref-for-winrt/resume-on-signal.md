---
title: winrt::resume_on_signal function (C++/WinRT)
description: A function that you can use to suspend until a kernel event is signaled.
dev_langs: ["C++"]
ms.date: 07/22/2020
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::resume_on_signal function (C++/WinRT)

A function that you can use to suspend until a kernel event is signaled.

For more info, and code examples, see [Awaiting a kernel handle](/windows/uwp/cpp-and-winrt-apis/concurrency-2#awaiting-a-kernel-handle).

## Syntax
```cppwinrt
auto resume_on_signal(
    void* handle,
    winrt::Windows::Foundation::TimeSpan timeout = {}) noexcept
```

### Parameters
`handle`
A handle to the kernel event to wait on. You're responsible for ensuring that this handle remains valid until your `co_await` of the function completes.

`timeout`
An optional timeout value. If you pass a timeout of 0, that's treated as infinite. If you pass a negative timeout, **resume_on_signal** immediately times out.


### Return value 
An awaitable object (an object that can be passed to `co_await`). The result of the `co_await` is `true` if the handle is signaled, or `false` if the timeout elapsed.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [More advanced concurrency and asynchrony with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency-2)
