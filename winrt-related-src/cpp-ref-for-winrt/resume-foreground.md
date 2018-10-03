---
author: stevewhims
description: TBD
title: winrt::resume_foreground struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/17/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::resume_foreground struct (C++/WinRT)

A struct&mdash;for use within a coroutine&mdash;that you can `co-await` to switch execution to a specific foreground thread. For more info, and a code example, see [Programming with thread affinity in mind](/windows/uwp/cpp-and-winrt-apis/concurrency#programming-with-thread-affinity-in-mind).

## Syntax
```cppwinrt
struct resume_foreground
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\Windows.UI.Core.h (not included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[resume_foreground::resume_foreground constructor](#resumeforegroundresumeforeground-constructor)|Initializes a new instance of the **resume_foreground** struct.|

## resume_foreground::resume_foreground constructor
Initializes a new instance of the **resume_foreground** struct.

### Syntax
```cppwinrt
explicit resume_foreground(winrt::Windows::UI::Core::CoreDispatcher&& dispatcher, winrt::Windows::UI::Core::CoreDispatcherPriority const priority = winrt::Windows::UI::Core::CoreDispatcherPriority::Normal);

explicit resume_foreground(winrt::Windows::UI::Core::CoreDispatcher const& dispatcher, winrt::Windows::UI::Core::CoreDispatcherPriority const priority = winrt::Windows::UI::Core::CoreDispatcherPriority::Normal);
```

### Parameters
`dispatcher`
A **winrt::Windows::UI::Core::CoreDispatcher** whose foreground thread to switch execution to.

`priority`
Specifies the priority for event dispatch.

## See also 
* [winrt namespace](winrt.md)
* [winrt::apartment_context function](apartment-context.md)
* [winrt::resume_background function](resume-background.md)
* [Concurrency and asynchronous operations with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/concurrency)