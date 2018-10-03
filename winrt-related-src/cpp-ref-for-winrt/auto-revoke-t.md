---
author: stevewhims
description: A marker type used to request an event revoker when registering a delegate to handle an event.
title: winrt::auto_revoke_t marker struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/24/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, marker, type
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::auto_revoke_t marker struct (C++/WinRT)
A marker type used to request an event revoker when registering a delegate to handle an event. For more details, and code examples, see [Revoke a registered delegate](/windows/uwp/cpp-and-winrt-apis/handle-events#revoke-a-registered-delegate).

## Syntax
```cppwinrt
struct auto_revoke_t
constexpr auto_revoke_t auto_revoke{};
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events)
