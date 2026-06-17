---
title: uap7:Properties
description: Properties of an application.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap7:Package, uap7:Applications, uap7:Application, uap7:Properties]
---

# uap7:Properties

Properties of an application.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Properties>`**  

## Syntax

```xml
<uap7:Properties>

  <!-- Child elements -->
  uap7:ImportRedirectionTable?
  uap7:ActiveCodePage?
  uap7:LanguagePreference?

</uap7:Properties>
```

### Key

`?` optional (zero or one)

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap7:ImportRedirectionTable](element-uap7-importredirectiontable.md) | Allows for a packaged app to declare API redirections. |
| **uap8:ActiveCodePage** | <!-- TODO: Add description --> |
| **uap10:LanguagePreference** | <!-- TODO: Add description --> |

## Parent elements

| Parent element | Description |
|-|-|
| [Application](element-f-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->