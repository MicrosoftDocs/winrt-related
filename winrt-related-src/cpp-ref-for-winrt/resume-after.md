---
description: A helper function that returns control to the caller, and then resumes execution on a thread pool thread after a delay.
title: winrt::resume_after function (C++/WinRT)
dev_langs: ["C++"]
ms.date: 01/04/2021
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.workload: ["cplusplus"]
---

# winrt::resume_after function (C++/WinRT)

A helper function&mdash;for use within a coroutine&mdash;that returns control to the caller, and then resumes execution on a thread pool thread after a delay. 

For more info, see [Concurrency and asynchronous operations](/windows/uwp/cpp-and-winrt-apis/concurrency).

## Syntax
```cppwinrt
inline auto resume_after(winrt::Windows::Foundation::TimeSpan duration) noexcept;
```

### Parameters

`duration`

The duration of the delay.

### Return value 

An object that you can `co_await`.

### Remarks

You can use the functions and operators in the **std::chrono** and **std::literals::chrono_literals** namespaces to create **TimeSpan** values conveniently. 

```cppwinrt
co_await winrt::resume_after(std::chrono::milliseconds(250));
```

```cppwinrt
using namespace std::literals::chrono_literals;
co_await winrt::resume_after(250ms);
```

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)
