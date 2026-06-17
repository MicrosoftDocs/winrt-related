---
title: PackageDependency
description: Declares a dependency on another package that is marked as a framework package (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Dependencies, PackageDependency]
---

# PackageDependency

Declares a dependency on another package that is marked as a framework package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<PackageDependency>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <PackageDependency
    Name = 'A required value. <!-- TODO: Add description for t:ST_PackageName -->'
    Publisher = 'A required value. <!-- TODO: Add description for t:ST_Publisher_2010_v2 -->'
    MinVersion = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.'
    MaxMajorVersionTested = 'An optional value. <!-- TODO: Add description for xs:unsignedShort -->'
    uap6:Optional = 'An optional boolean value.' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name as it appears in the *Name* attribute of the [Identity](element-f-identity.md) element of the dependency package. | A value. <!-- TODO: Add data type for t:ST_PackageName --> | Yes |  |
| **Publisher** | The publisher as it appears in the *Publisher* attribute of the [Identity](element-f-identity.md)  element of the dependency package. | A value. <!-- TODO: Add data type for t:ST_Publisher_2010_v2 --> | Yes |  |
| **MinVersion** | The minimum version of the dependency package. | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |
| **MaxMajorVersionTested** | The maximum version of the dependency package tested against. Used to determine whether frameworks will be staged side-by-side, and what framework gets loaded into the package graph for the package. | An optional value. <!-- TODO: Add data type for xs:unsignedShort --> | No |  |
| **uap6:Optional** | Indicates that a framework package dependency is optional for the app, meaning the app can be installed even if the optional framework dependencies are not installed. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap6** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

When working with package dependencies note the following:

- A package cannot have multiple dependency declarations that have the same **Name** attribute.
- If the **Publisher** attribute is not specified, then the dependency package must be unsigned. When a dependency package is unsigned it must also be marked as a framework package. See the [Framework](element-f-framework.md) element.
- The version of the dependency package must be greater than or equal to the minimum version specified by this attribute.

## Examples

```xml
<Dependencies>
  <PackageDependency Name="Microsoft.WinJS.1.0"
    Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
    MinVersion="1.0.0.0"/>    
</Dependencies>
```
