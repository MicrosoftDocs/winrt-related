---
title: Identity
description: Defines a globally unique identifier for a package Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Identity]
---

# Identity

Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Identity>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Identity
    Name = 'A required value. <!-- TODO: Add description for t:ST_PackageName -->'
    ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", "x86a64", or "neutral".'
    Publisher = 'A required value. <!-- TODO: Add description for t:ST_Publisher_2010_v2 -->'
    Version = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.'
    ResourceId = 'An optional value. <!-- TODO: Add description for t:ST_ResourceId -->' />
</Package>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | Describes the contents of the package. The *Name* attribute is case-sensitive. Use the [DisplayName](element-f-displayname.md) attribute to display a package name to users. | A value. <!-- TODO: Add data type for t:ST_PackageName --> | Yes |  |
| **ProcessorArchitecture** | Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. | An optional string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *x86a64*, *neutral*. | No |  |
| **Publisher** | Describes the publisher information. The *Publisher* attribute must match the publisher subject information of the certificate used to sign a package. For more information see [Packaging apps](/windows/uwp/packaging/index). | A value. <!-- TODO: Add data type for t:ST_Publisher_2010_v2 --> | Yes |  |
| **Version** | The *version* number of the package. | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |
| **ResourceId** | Describes the type of UI resources contained in the package. The *ResourceId* is a publisher-specified string. | An optional value. <!-- TODO: Add data type for t:ST_ResourceId --> | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

This example is from the app manifest file of the [App package information](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/Package) sample on GitHub.

```xml
<Identity
  Name="Microsoft.SDKSamples.PackageSample.CS" 
  Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" 
  Version="1.0.1.0" />
```
