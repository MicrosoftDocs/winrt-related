---
description: Declares a dependency on another package that is marked as a framework package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: PackageDependency (Windows 10)
ms.assetid: 7f0800a1-f1dd-48c2-aba0-3701dd27d383
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/10/2018
---

# PackageDependency (Windows 10)

Declares a dependency on another package that is marked as a framework package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Dependencies\>](element-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<PackageDependency\>**

## Syntax

```xml
<PackageDependency
  Name = 'A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters.'
  Publisher = 'A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name.'
  MinVersion = 'A version string in quad notation ("Major.Minor.Build.Revision"), where Major cannot be 0.'
  MaxMajorVersionTested = 'An optional number with a value between 0 and 512 characters in length.'
  uap6:Optional = 'An optional boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name as it appears in the *Name* attribute of the [Identity](element-identity.md) element of the dependency package. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters. | Yes |  |
| **Publisher** | The publisher as it appears in the *Publisher* attribute of the [Identity](element-identity.md)  element of the dependency package. | A string with a value between 1 and 8192 characters in length that fits the regular expression  of a distinguished name. | Yes |  |
| **MinVersion** | The minimum version of the dependency package. | A version string in quad notation (`Major.Minor.Build.Revision`), where `Major` cannot be `0`. | Yes |  |
| **MaxMajorVersionTested** | The maximum version of the dependency package tested against. Used to determine whether frameworks will be staged side-by-side, and what framework gets loaded into the package graph for the package. | An optional number with a value between 0 and 512 characters in length. | No |  |
| **uap6:Optional** | Indicates that a framework package dependency is optional for the app, meaning the app can be installed even if the optional framework dependencies are not installed. | An optional boolean value. | No | false |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Remarks

When working with package dependencies note the following:

- A package cannot have multiple dependency declarations that have the same **Name** attribute.
- If the **Publisher** attribute is not specified, then the dependency package must be unsigned. When a dependency package is unsigned it must also be marked as a framework package. See the [Framework](element-framework.md) element.
- The version of the dependency package must be greater than or equal to the minimum version specified by this attribute.

## Examples

```xml
<Dependencies>
  <PackageDependency Name="Microsoft.WinJS.1.0"
    Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
    MinVersion="1.0.0.0"/>    
</Dependencies>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
