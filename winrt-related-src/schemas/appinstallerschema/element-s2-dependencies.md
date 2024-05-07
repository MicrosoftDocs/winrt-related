---
title: s2:Dependencies
description: efines the dependency packages that are required for successful deployment of the related set. This element is optional. (s2:Dependencies)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:Dependencies

## Description

Defines the dependency packages that are required for successful deployment of the related set. This element is optional. (s2:Dependencies)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:Dependencies&gt;

## Syntax

```syntax
<s2:Dependencies>
<!-- Child elements -->
  Package{0,1}
  Bundle{0,1}
</s2:Dependencies>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s2:Package](element-s2-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [s2:Bundle](element-s2-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri. |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:AppInstaller](element-s2-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Remarks
These packages will only be installed if they are not already available on the target device.

## Examples
The following example is taken from a sample appinstaller file. The Uri location doesn't exist.  

``` xml
<s2:Dependencies>
  <s2:Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x86" Uri="http://foobarbaz.com/fwkx86.appx" />
  <s2:Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x64" Uri="http://foobarbaz.com/fwkx64.appx" />
</s2:Dependencies>
```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s2=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| Minimum OS version | Windows 10 version 1803 build 17134 |
