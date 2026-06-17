---
title: uap7:ImportRedirectionTable
description: Allows for a packaged app to declare API redirections.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap7:Package, uap7:Applications, uap7:Application, uap7:Properties, uap7:ImportRedirectionTable]
---

# uap7:ImportRedirectionTable

Allows for a packaged app to declare API redirections. API redirection allows apps to consume legacy binaries that link against unsupported APIs (e.g., CreateFile) and transparently replace them with supported APIs (e.g., CreateFileFromApp) at module load time.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:ImportRedirectionTable>`**  

## Syntax

```xml
<uap7:ImportRedirectionTable>
  A string that represnets the name of a DLL file.
</uap7:ImportRedirectionTable>
```

## Value

A string that represnets the name of a DLL file.

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap7:Properties](element-uap7-properties.md) | Properties of an application. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

The DLL file is passed to *CreateProcess* to influence how the loader resolves imports.

## Examples

<!-- Author content goes here -->