---
author: stevewhims
description: A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type.
title: winrt::implements struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/26/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, implement, interface
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::implements struct template (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type. See [Interfaces; how to implement them in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/implement-an-interface).

## Syntax
```cppwinrt
template <typename D, typename... I>
struct implements : impl::producer<D, impl::uncloak_t<I>>..., impl::base_implements<D, I...>::type
```

### Template parameters
`typename D`
Your derived type name.

`typename... I`
Any number of interfaces to implement.

### Example
```cppwinrt
// App.cpp
...
struct App : implements<App, IFrameworkViewSource>
{
	IFrameworkView CreateView()
	{
		return ...
	}
}
...
```

## Requirements
**Minimum supported SDK:** Windows SDK for Windows 10, version 1803

**Namespace:** winrt

**Header** %ProgramFiles(x86)%\Windows Kits\10\Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
[winrt namespace (C++/WinRT)](winrt.md)
