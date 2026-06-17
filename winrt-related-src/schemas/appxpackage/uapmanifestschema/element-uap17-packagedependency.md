---
title: uap17:PackageDependency
description: Declares other packages that a package depends on. This dependency can be specified as required for both install time and runtime or just install time but not runtime.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Extensions, uap17:Package, uap17:Dependencies, uap17:PackageDependency]
---

# uap17:PackageDependency

Declares other packages that a package depends on. This dependency can be specified as required for both install time and runtime or just install time but not runtime.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<PackageDependency>`**  

## Syntax

```xml
<uap17:PackageDependency
  Type = 'An optional string that can have one of the following values: "install", or "installAndRuntime".'
  Name = 'A required value. <!-- TODO: Add description for t:ST_PackageName -->'
  Publisher = 'A required value. <!-- TODO: Add description for t:ST_Publisher_2010_v2 -->'
  MinVersion = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.'
  MaxMajorVersionTested = 'An optional value. <!-- TODO: Add description for xs:unsignedShort -->'
  uap6:Optional = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *install*, *installAndRuntime*. | No |  |
| **Name** | <!-- TODO: Add description --> | A value. <!-- TODO: Add data type for t:ST_PackageName --> | Yes |  |
| **Publisher** | <!-- TODO: Add description --> | A value. <!-- TODO: Add data type for t:ST_Publisher_2010_v2 --> | Yes |  |
| **MinVersion** | <!-- TODO: Add description --> | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |
| **MaxMajorVersionTested** | <!-- TODO: Add description --> | An optional value. <!-- TODO: Add data type for xs:unsignedShort --> | No |  |
| **uap6:Optional** | <!-- TODO: Add description --> | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| **uap6** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
