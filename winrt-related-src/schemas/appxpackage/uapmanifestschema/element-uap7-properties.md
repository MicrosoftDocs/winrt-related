---
description: Properties of an application.
title: uap7:Properties
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/03/2018
no-loc: [Package, Applications, Application, uap7:Properties]
---

# uap7:Properties

Properties of an application.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:Properties>`**  

## Syntax

```xml
<uap7:Properties>

  <!-- Child elements -->
  uap7:ImportRedirectionTable
  uap8:ActiveCodePage
  uap10:LanguagePreference

</uap7:Properties>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap7:ImportRedirectionTable](element-uap7-importredirectiontable.md) | Allows for a packaged app to declare API redirections.|
| [uap8:ActiveCodePage](element-uap8-activecodepage.md) | Sets the process active code page to UTF-8. |
| [uap10:LanguagePreference](element-uap10-languagepreference.md) | Specifies which Windows language setting an app uses as its language preference. |

### Parent elements

| Parent element | Description |
|-|-|
| [Application](element-f-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |
