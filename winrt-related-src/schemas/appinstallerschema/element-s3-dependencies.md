---
title: s3:Dependencies
description: Defines the dependency packages that are required for successful deployment of the related set. This element is optional. (s3:Dependencies)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:Dependencies

## Description

Defines the dependency packages that are required for successful deployment of the related set. This element is optional. (s3:Dependencies)

## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s3:Dependencies&gt;

## Syntax

```syntax
<s3:Dependencies>
<!-- Child elements -->
  Package
  Bundle
</s3:Dependencies>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s3:Package](element-s3-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [s3:Bundle](element-s3-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:AppInstaller](element-s3-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Remarks
These packages will only be installed if they are not already available on the target device.

## Examples
The following example is taken from a sample appinstaller file. The Uri location doesn't exist.  

``` xml
<s3:Dependencies>
  <s3:Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x86" Uri="http://foobarbaz.com/fwkx86.appx" />
  <s3:Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x64" Uri="http://foobarbaz.com/fwkx64.appx" />
</s3:Dependencies>
```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s3=http://schemas.microsoft.com/appx/appinstaller/2018` | This namespace is required for features introduced in Windows 10, version 1809. |
| Minimum OS version | Windows 10 version 1809 |
