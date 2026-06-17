---
title: uap13:HostRuntimeDependency
description: Declares publisher information for the app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Extensions, uap13:Package, uap13:Dependencies, uap13:HostRuntimeDependency]
---

# uap13:HostRuntimeDependency

Declares publisher information for the app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap13:HostRuntimeDependency>`**  

## Syntax

```xml
<uap13:HostRuntimeDependency
  Name = 'A required value. <!-- TODO: Add description for t:ST_AsciiIdentifier -->'
  Publisher = 'A required value. <!-- TODO: Add description for t:ST_Publisher_2010_v2 -->'
  MinVersion = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the application. | A value. <!-- TODO: Add data type for t:ST_AsciiIdentifier --> | Yes |  |
| **Publisher** | The publisher of the application | A value. <!-- TODO: Add data type for t:ST_Publisher_2010_v2 --> | Yes |  |
| **MinVersion** | The minimum Windows version required to install the application. | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/13` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
