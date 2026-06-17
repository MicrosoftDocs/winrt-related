---
title: rescap4:PrimaryInteropAssemblies
description: Defines package assembly configuration.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, rescap4:Extension, rescap4:PrimaryInteropAssemblies]
---

# rescap4:PrimaryInteropAssemblies

Defines package assembly configuration.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:Extension>`](element-rescap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap4:PrimaryInteropAssemblies>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap4:Extension>`](element-rescap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap4:PrimaryInteropAssemblies>`**  

## Syntax

```xml
<rescap4:PrimaryInteropAssemblies
  AssemblyName = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  AssemblyVersion = 'A required version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4.'
  PublicKey = 'A required value. <!-- TODO: Add description for rescap4:ST_PublicKey -->'
  MachineType = 'A required string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".'
  TargetClrVersion = 'A required version string in duo or trio notation, e.g. 1.0 or 1.0.0.'
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' >

  <!-- Child elements -->
  rescap4:Redirect{0,100000000}

</rescap4:PrimaryInteropAssemblies>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AssemblyName** | The name of the assembly. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **AssemblyVersion** | The version of the assembly. | A version string in quad notation, major.minor.build.revision, e.g. 1.2.3.4. | Yes |  |
| **PublicKey** | The public key to access the assembly. | A value. <!-- TODO: Add data type for rescap4:ST_PublicKey --> | Yes |  |
| **MachineType** | The device architecture used for the assembly. | A string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *neutral*. | Yes |  |
| **TargetClrVersion** | The device target architecture used for the assembly. | A version string in duo or trio notation, e.g. 1.0 or 1.0.0. | Yes |  |
| **Path** | The path to the assembly. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [rescap4:Redirect](element-rescap4-redirect.md) | Specifies redirect information for an interop assembly. |

## Parent elements

| Parent element | Description |
|-|-|
| [rescap4:Extension](element-rescap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
