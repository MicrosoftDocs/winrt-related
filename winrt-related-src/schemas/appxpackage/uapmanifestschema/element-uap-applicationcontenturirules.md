---
title: uap:ApplicationContentUriRules
description: Specifies which pages in the web context have access to the system's geolocation devices and access to the clipboard (Windows 10; uap:ApplicationContentUriRules).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:ApplicationContentUriRules]
---

# uap:ApplicationContentUriRules

Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:ApplicationContentUriRules>`**  

## Syntax

```xml
<uap:ApplicationContentUriRules>

  <!-- Child elements -->
  uap:Rule{1,100}

</uap:ApplicationContentUriRules>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:Rule](element-uap-rule.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |

## Parent elements

| Parent element | Description |
|-|-|
| [Application](element-f-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
