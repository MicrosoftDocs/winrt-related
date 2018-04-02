---
author: stevewhims
description: A helper function that retrieves a pointer to a C++/WinRT object's underlying IUnknown interface.
title: winrt::get_abi function template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/20/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, IUnknown
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_abi function template (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A helper function that retrieves a pointer to a C++/WinRT object's underlying [IUnknown interface](https://msdn.microsoft.com/library/windows/desktop/ms680509).

## Syntax
```cppwinrt
template <typename T, typename = std::enable_if_t<!std::is_base_of_v<Windows::Foundation::IUnknown, T>>>
auto get_abi(T const& object) noexcept

inline void* get_abi(Windows::Foundation::IUnknown const& object) noexcept
```

### Parameters
`object`
The C++/WinRT object whose **IUnknown** interface pointer to retrieve.

### Return value 
A pointer to **IUnknown**.

## Requirements
**Minimum supported SDK:** Windows SDK for Windows 10, version 1803

**Namespace:** winrt

**Header** %ProgramFiles(x86)%\Windows Kits\10\Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)
