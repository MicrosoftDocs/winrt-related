---
author: stevewhims
description: Microsoft Interface Definition Language 3.0 reference content.
title: Microsoft Interface Definition Language 3.0 reference
ms.author: stwhi
ms.date: 04/23/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0, 3, midl3
ms.localizationpriority: medium
---

# Microsoft Interface Definition Language 3.0 reference
Microsoft Interface Definition Language (MIDL) 3.0 is a simplified, modern, familiar syntax for defining Windows Runtime types inside Interface Definition Language (`.idl`) files.

```idl
// BookSku.idl
namespace Bookstore
{
    runtimeclass BookSku
    {
        String Title;
    }
}
```

As of version 10.0.17134.0 (Windows 10, version 1803), the Windows SDK includes command-line support for MIDL 3.0 (`midl.exe` version 8.01.0622 or later, used with the `/winrt` switch).

| Topic | Description |
| - | - |
| [Introduction to MIDL 3.0](intro.md) | An introduction to Microsoft Interface Definition Language 3.0. |
| [Synthesizing interfaces (MIDL 3.0)](synthesizing-interfaces.md) | This topic describes how the MIDL 3.0 compiler synthesizes and adds interfaces, as necessary. |
| [Predefined attributes (MIDL 3.0)](predefined-attributes.md) | There are a number of pre-defined custom attributes that allow you to control the name and IID for compiler-synthesized interfaces. |
| [Reserved keywords (MIDL 3.0)](reserved-keywords.md) | This topic lists the reserved keywords in MIDL 3.0. You may not use these keywords in the names of your runtime classes and members. |
| [Troubleshooting MIDL 3.0 issues](troubleshooting.md) | A table of troubleshooting symptoms and remedies. |
