---
description: Indicates whether Windows will enforce runtime package integrity checks on the package.
title: uap10:PackageIntegrity
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 02/06/2020
---

# uap10:PackageIntegrity

Specifies the level of run time package integrity checks and remediation for the package. If enabled, Windows will perform runtime checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:PackageIntegrity\>**

## Syntax

```xml
<uap10:PackageIntegrity>

  <!-- Child elements -->
  uap10:Content?

</uap10:PackageIntegrity>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap10:Content](element-uap10-content.md) | Indicates whether Windows will enforce runtime package integrity checks on the entire contents of the package. |

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package behaves. |

## Remarks

If you include a **uap10:PackageIntegrity** element without a child [uap10:Content](element-uap10-content.md) element, Windows will not enforce runtime package integrity checks.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
