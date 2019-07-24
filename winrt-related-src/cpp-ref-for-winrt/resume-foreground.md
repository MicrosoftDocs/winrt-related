---
author: stevewhims
description: A helper function&mdash;for use within a coroutine&mdash;that you can `co_await` to switch execution to a specific foreground thread.
title: winrt::resume_foreground function (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/17/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::resume_foreground function (C++/WinRT)

A helper function&mdash;for use within a coroutine&mdash;that you can `co_await` to switch execution to a specific foreground thread. For more info, and a code example, see [Programming with thread affinity in mind](/windows/uwp/cpp-and-winrt-apis/concurrency-2#programming-with-thread-affinity-in-mind).

## Syntax
```cppwinrt
inline auto resume_foreground(
    Windows::UI::Core::CoreDispatcher const& dispatcher,
    Windows::UI::Core::CoreDispatcherPriority const priority = Windows::UI::Core::CoreDispatcherPriority::Normal) noexcept;
```

### Parameters
`dispatcher`
A **winrt::Windows::UI::Core::CoreDispatcher** whose foreground thread to switch execution to.

`priority`
Specifies the priority for event dispatch.

### Return value
An object that you can `co_await`.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\Windows.UI.Core.h (not included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::apartment_context function](apartment-context.md)
* [winrt::resume_background function](resume-background.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)