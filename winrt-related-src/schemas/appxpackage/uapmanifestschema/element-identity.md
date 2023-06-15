---
description: Defines a globally unique identifier for a package Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Identity (Windows 10)
ms.assetid: 45524773-3b61-44ac-a417-cfaac92af0a0
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 03/09/2017
---

# Identity (Windows 10)

Defines a globally unique identifier for a package. A package identity is represented as a tuple of attributes of the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Identity\>**

## Syntax

```xml
<Identity
  Name = 'A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters. Additionally, it cannot be any of the folllowing string values: "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", or "LPT9".'
  ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".'
  Publisher = 'A string with a value between 1 and 8192 characters in length that fits the regular expression of a distinguished name.'
  Version = 'A version string in quad notation, "Major.Minor.Build.Revision" where Major cannot be "0".' 
  ResourceId = 'An optional ASCII string with a value between 1 and 30 characters in length. Additionally, it cannot be any of the folllowing string values: "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", or "LPT9".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | Describes the contents of the package. The *Name* attribute is case-sensitive. Use the [DisplayName](element-displayname.md) attribute to display a package name to users. | A string with a value between 3 and 50 characters in length that consists of alpha-numeric, period, and dash characters. Additionally, it cannot be any of the folllowing string values: *CON*, *PRN*, *AUX*, *NUL*, *COM1*, *COM2*, *COM3*, *COM4*, *COM5*, *COM6*, *COM7*, *COM8*, *COM9*, *LPT1*, *LPT2*, *LPT3*, *LPT4*, *LPT5*, *LPT6*, *LPT7*, *LPT8*, or *LPT9*. | Yes |  |
| **ProcessorArchitecture** | Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. | An optional string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, or *neutral*. | No | *neutral* |
| **Publisher** | Describes the publisher information. The *Publisher* attribute must match the publisher subject information of the certificate used to sign a package. For more information see [Packaging apps](/windows/uwp/packaging/index). | A string with a value between 1 and 8192 characters in length that fits the regular expression of a distinguished name. | Yes |  |
| **ResourceId** | Describes the type of UI resources contained in the package. The *ResourceId* is a publisher-specified string. | An optional ASCII string with a value between 1 and 30 characters in length. Additionally, it cannot be any of the folllowing string values: *CON*, *PRN*, *AUX*, *NUL*, *COM1*, *COM2*, *COM3*, *COM4*, *COM5*, *COM6*, *COM7*, *COM8*, *COM9*, *LPT1*, *LPT2*, *LPT3*, *LPT4*, *LPT5*, *LPT6*, *LPT7*, *LPT8*, or *LPT9*. | No |  |
| **Version** | The *version* number of the package. | A version string in quad notation, `Major.Minor.Build.Revision` where `Major` cannot be `0`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

### Example

This example is from the app manifest file of the [App package information](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/Package) sample on GitHub.

```xml
<Identity
  Name="Microsoft.SDKSamples.PackageSample.CS" 
  Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" 
  Version="1.0.1.0" />
```

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
