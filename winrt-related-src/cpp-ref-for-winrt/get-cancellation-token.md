---
author: stevewhims
description: In a coroutine, use the object returned by get_cancellation_token to poll for, or to respond to, cancellation.
title: winrt::get_cancellation_token function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 09/28/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_cancellation_token function (C++/WinRT)

In a coroutine, you can use the object returned by **winrt::get_cancellation_token** to poll for, or to respond to, cancellation. For more info, and code examples, see [Canceling an asychronous operation, and cancellation callbacks](/windows/uwp/cpp-and-winrt-apis/concurrency#canceling-an-asychronous-operation-and-cancellation-callbacks).

## Syntax
```cppwinrt
inline winrt::get_cancellation_token_t get_cancellation_token() noexcept;
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also
* [winrt namespace](winrt.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)
