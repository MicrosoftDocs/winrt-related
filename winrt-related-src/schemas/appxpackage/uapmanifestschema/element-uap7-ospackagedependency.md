---
title: uap7:OSPackageDependency
description: OS package dependency information.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest, driver dependency
no-loc: [Package, Extensions, uap7:Package, uap7:Dependencies, uap7:OSPackageDependency]
---

# uap7:OSPackageDependency

Defines a package dependency for a UWP app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:OSPackageDependency>`**  

## Syntax

```xml
<uap7:OSPackageDependency
  Name = 'An alphanumeric string that may contain periods and dashes.'
  Version = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the package dependency. | An alphanumeric string that may contain periods and dashes. | Yes |  |
| **Version** | The version of the package dependency. | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->