---
title: uap10:Content
description: Represents...
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap10:Package, uap10:Properties, uap10:PackageIntegrity, uap10:Content]
---

# uap10:Content

Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. If enabled, Windows will perform run time checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:PackageIntegrity>`](element-uap10-packageintegrity.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:Content>`**  

## Syntax

```xml
<uap10:Content
  Enforcement = 'A required string that can have one of the following values: "default", "on", or "off".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Enforcement** | Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. | A string that can have one of the following values: *default*, *on*, *off*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap10:PackageIntegrity](element-uap10-packageintegrity.md) | Specifies the level of run time package integrity checks and remediation for the package. If enabled, Windows will perform runtime checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
