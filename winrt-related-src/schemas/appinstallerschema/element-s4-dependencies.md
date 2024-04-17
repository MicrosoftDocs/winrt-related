---
title: s4:Dependencies
description: Defines the dependency packages that are required for successful deployment of the related set. This element is optional. (s4:Dependencies)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:Dependencies

## Description

Defines the dependency packages that are required for successful deployment of the related set. This element is optional. (s4:Dependencies)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:Dependencies&gt;

## Syntax

```syntax
<s4:Dependencies>
<!-- Child elements -->
  ( Bundle{0,10000}
  | Package{0,10000}
  )
</s4:Dependencies>
```

### Key

`{}`   specific range of occurrences


## Child Elements

| Element | Description |
| -----------| -------------|
| [s4:Package](element-s4-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [s4:Bundle](element-s4-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:AppInstaller](element-s4-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Remarks
These packages will only be installed if they are not already available on the target device.

## Examples
The following example is taken from a sample appinstaller file. The Uri location doesn't exist.  

``` xml
<s4:Dependencies>
  <s4:Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x86" Uri="http://foobarbaz.com/fwkx86.appx" />
  <s4:Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x64" Uri="http://foobarbaz.com/fwkx64.appx" />
</s4:Dependencies>
```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| Namespace (s4) | `http://schemas.microsoft.com/appx/appinstaller/2021` |
| Minimum OS version | Windows version 21H2 build 22000 |

