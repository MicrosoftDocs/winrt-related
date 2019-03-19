---
author: stevewhims
description: A helper function that returns control to the caller, and resumes execution on a thread pool thread.
title: winrt::resume_background function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/17/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::resume_background function (C++/WinRT)

A helper function&mdash;for use within a coroutine&mdash;that returns control to the caller, and then immediately resumes execution on a thread pool thread. For more info, and a code example, see [Offloading work onto the Windows thread pool](/windows/uwp/cpp-and-winrt-apis/concurrency#offloading-work-onto-the-windows-thread-pool).

## Syntax
```cppwinrt
inline auto resume_background();
```

### Return value
An object that you can `co_await`.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::apartment_context function](apartment-context.md)
* [winrt::resume_foreground function](resume-foreground.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)
