---
description: OS package dependency information.
title: uap7:OSPackageDependency
keywords: windows 10, uwp, schema, package manifest, driver dependency
ms.topic: reference
ms.date: 10/03/2018
---

# uap7:OSPackageDependency

Defines a package dependency for a UWP app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Dependencies\>](element-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap7:OSPackageDependency\>**

## Syntax

```xml
<uap7:OSPackageDependency
  Name = 'An alphanumeric string that may contain periods and dashes.'
  Version = 'A version string in quad notation ("Major.Minor.Build.Revision"), where "Major" cannot be "0".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the package dependency. | An alphanumeric string that may contain periods and dashes. | Yes |  |
| **Version** | The version of the package dependency. | A version string in quad notation (`Major.Minor.Build.Revision`), where `Major` cannot be `0`. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
