---
description: Allows for a packaged app to declare API redirections.
title: uap7:ImportRedirectionTable
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/03/2018
---

# uap7:ImportRedirectionTable

Allows for a packaged app to declare API redirections. API redirection allows apps to consume legacy binaries that link against unsupported APIs (e.g., CreateFile) and transparently replace them with supported APIs (e.g., CreateFileFromApp) at module load time.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap7:Properties\>](element-uap7-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap7:ImportRedirectionTable\>**

## Syntax

```xml
<uap7:ImportRedirectionTable>
  A string that represnets the name of a DLL file.
</uap7:ImportRedirectionTable>
```

## Attributes and Elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap7:Properties](element-uap7-properties.md) | Properties of an application. |

## Remarks

The DLL file is passed to *CreateProcess* to influence how the loader resolves imports.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
