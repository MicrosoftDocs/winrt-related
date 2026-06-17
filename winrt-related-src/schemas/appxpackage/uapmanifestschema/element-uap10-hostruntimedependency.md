---
title: uap10:HostRuntimeDependency
description: Defines a dependency on a host app package for the current app package.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest, host app, hosted app
no-loc: [Package, Extensions, uap10:Package, uap10:Dependencies, uap10:HostRuntimeDependency]
---

# uap10:HostRuntimeDependency

Defines a dependency on a host app for the current app. For more information, see [Create hosted apps](/windows/uwp/launch-resume/hosted-apps).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:HostRuntimeDependency>`**  

## Syntax

```xml
<uap10:HostRuntimeDependency
  Name = 'A required value. <!-- TODO: Add description for t:ST_AsciiIdentifier -->'
  Publisher = 'A required value. <!-- TODO: Add description for t:ST_Publisher_2010_v2 -->'
  MinVersion = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the host app. | A value. <!-- TODO: Add data type for t:ST_AsciiIdentifier --> | Yes |  |
| **Publisher** | The publisher of the host app. | A value. <!-- TODO: Add data type for t:ST_Publisher_2010_v2 --> | Yes |  |
| **MinVersion** | The minimum version of the host app that the current app depends on. | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
