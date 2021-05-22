---

description: The return type for a fire-and-forget coroutine.
title: winrt::fire_and_forget struct (C++/WinRT)
dev_langs: ["C++"]

ms.date: 09/28/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::fire_and_forget struct (C++/WinRT)

To make your coroutine a fire-and-forget one, use **winrt::fire_and_forget** for its return type. For more info, and a code example, see [Fire and forget](/windows/uwp/cpp-and-winrt-apis/concurrency-2#fire-and-forget).

## Syntax
```cppwinrt
struct fire_and_forget;
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also
* [winrt namespace](winrt.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)
