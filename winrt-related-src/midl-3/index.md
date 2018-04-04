---
author: stevewhims
description: Microsoft Interface Definition Language 3.0 reference content.
title: Microsoft Interface Definition Language 3.0 reference
ms.author: stwhi
manager: "markl"
ms.date: 03/29/2018
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0
ms.localizationpriority: medium
---

# Microsoft Interface Definition Language 3.0 reference
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Microsoft Interface Definition Language (MIDL) 3.0 is a simplified, modern, familiar syntax for declaring Windows Runtime types inside Interface Definition Language (`.idl`) files.

```idl
// booksku.idl
import "Windows.Foundation.idl";
namespace Bookstore
{
	runtimeclass BookSku
	{
		String Title;
	}
}
```

As of Windows 10, version 1803, the Windows SDK includes command-line support for MIDL 3.0 (`midl.exe` version 8.01.0622 or later, which internally calls `midlrt.exe` version 10.00.0215 or later).

## Use cases for MIDL 3.0
The original [MIDL 1.0](https://msdn.microsoft.com/library/windows/desktop/aa367091) was designed for declaring COM interfaces and coclasses. An updated 2.0 syntax was used internally to declare Windows Runtime APIs for the Windows platform. MIDL 3.0 is a much simpler and more modern way of declaring Windows Runtime APIs, and you can use it in your projects, particularly to declare [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index) runtime classes.

| Topic | Description |
| - | - |
| [Troubleshooting MIDL 3.0 issues](troubleshooting.md) | A table of troubleshooting symptoms and remedies. |
| [Introduction to MIDL 3.0](intro.md) | An introduction to Microsoft Interface Definition Language 3.0. |
| [Synthesizing interfaces (MIDL 3.0)](synthesizing-interfaces.md) | This topic describes how the MIDL 3.0 compiler synthesizes and adds interfaces, as necessary. |
| [Predefined attributes (MIDL 3.0)](predefined-attributes.md) | There are a number of pre-defined custom attributes that allow you to control the name and IID for compiler-synthesized interfaces. |
