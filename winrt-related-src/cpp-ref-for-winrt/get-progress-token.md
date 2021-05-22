---

description: In a coroutine, use the object returned by get_progress_token to report progress back to a progress handler.
title: winrt::get_progress_token function (C++/WinRT)
dev_langs: ["C++"]

ms.date: 09/28/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_progress_token function (C++/WinRT)

In a coroutine, you can use the object returned by **winrt::get_progress_token** to report progress back to a progress handler. For more info, and a code example, see [Reporting progress](/windows/uwp/cpp-and-winrt-apis/concurrency-2#reporting-progress).

## Syntax
```cppwinrt
inline winrt::get_progress_token_t get_progress_token() noexcept;
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also
* [winrt namespace](winrt.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)
