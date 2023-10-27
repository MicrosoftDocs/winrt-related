---
description: Specifies which pages in the web context have access to the system's geolocation devices and access to the clipboard (Windows 10; uap:ApplicationContentUriRules).
Search.Product: eADQiWindows 10XVcnh
title: uap:ApplicationContentUriRules (Windows 10)
ms.assetid: ae619bfa-0087-46ac-90e3-934a7bae85ba
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:ApplicationContentUriRules (Windows 10)

Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:ApplicationContentUriRules\>**

## Syntax

```xml
<uap:ApplicationContentUriRules>

  <!-- Child elements -->
  uap:Rule{1,100}

</uap:ApplicationContentUriRules>
```

### Key

`{}`  specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:Rule](element-uap-rule.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |

### Parent elements

| Parent element | Description |
|-|-|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
