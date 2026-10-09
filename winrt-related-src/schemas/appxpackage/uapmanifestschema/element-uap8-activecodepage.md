---
description: Sets the process active code page to UTF-8.
title: uap8:ActiveCodePage
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/09/2026
no-loc: [Package, Applications, Application, uap7:Properties, uap8:ActiveCodePage]
---

# uap8:ActiveCodePage

Sets the process active code page to UTF-8.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Properties>`](element-uap7-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap8:ActiveCodePage>`**

## Syntax

```xml
<uap8:ActiveCodePage>UTF-8</uap8:ActiveCodePage>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap7:Properties](element-uap7-properties.md) | Properties of an application. |

## Remarks

This sets the process active code page to UTF-8, so ANSI APIs in the process that rely on the active code page use UTF-8. It does not set the console input or output code pages.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |
