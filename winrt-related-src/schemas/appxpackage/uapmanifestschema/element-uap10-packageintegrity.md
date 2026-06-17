---
title: uap10:PackageIntegrity
description: Indicates whether Windows will enforce runtime package integrity checks on the package.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap10:Package, uap10:Properties, uap10:PackageIntegrity]
---

# uap10:PackageIntegrity

Specifies the level of run time package integrity checks and remediation for the package. If enabled, Windows will perform runtime checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:PackageIntegrity>`**  

## Syntax

```xml
<uap10:PackageIntegrity>

  <!-- Child elements -->
  uap10:Content?

</uap10:PackageIntegrity>
```

### Key

`?` optional (zero or one)

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap10:Content](element-uap10-content.md) | Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. If enabled, Windows will perform run time checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package. |

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

If you include a **uap10:PackageIntegrity** element without a child [uap10:Content](element-uap10-content.md) element, Windows will not enforce runtime package integrity checks.

## Examples

<!-- Author content goes here -->
