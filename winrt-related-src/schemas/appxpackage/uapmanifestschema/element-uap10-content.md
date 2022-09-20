---
description: Represents...
title: uap10:Content
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 02/06/2020
---

# uap10:Content

Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. If enabled, Windows will perform run time checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:PackageIntegrity\>](element-uap10-packageintegrity.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap10:Content\>**

## Syntax

```xml
<uap10:PackageIntegrity>

  <!-- Child elements -->
  <uap10:Content
    Enforcement = 'A string that can have one of the following values: "on", "off", or "default". The value "default" currently has the same behavior as "off".' />

</uap10:PackageIntegrity>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Enforcement** | Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. | A string that can have one of the following values: *on*, *off*, or *default*. The value *default* currently has the same behavior as *off*. | Yes | *off* |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap10:PackageIntegrity](element-uap10-packageintegrity.md) | Specifies the level of run time package integrity checks and remediation for the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
