---
title: s2:RelatedPackages
description: Specifies the related packages. These packages won't be installed as part of the deployment operation. (s2:RelatedPackages)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:RelatedPackages

## Description

Specifies the related packages. These packages won't be installed as part of the deployment operation. (s2:RelatedPackages)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:RelatedPackages&gt;

## Syntax

```syntax
<s2:RelatedPackages>
<!-- Child elements -->
  Package{0,1}
  Bundle{0,1}
</s2:RelatedPackages>
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

The **RelatedPackages** element defines the app packages that are specified in the main app pacakge but will not be installed along with the main app. There can be more than one child element defined inside the **RelatedPackages** element. If the app is packaged as .appx then use the **Package**, and if the app is packaged as .appxbundle then use the **Bundle** element.

## Examples

The following example is taken from a sample appinstaller file. The Uri location doesn't exist. 

```xml
<s2:RelatedPackages>
    <s2:Bundle
        Name="Fabrikam.RelatedApp1"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/RelatedApp1.appxbundle" />

    <s2:Package
        Name="Fabrikam.RelatedApp2"
        Publisher="CN=Fabrikam"
        Version="10.34.54.23"
        ProcessorArchitecture="x64"
        Uri="http://mywebservice.azurewebsites.net/RelatedApp2.appx" />

</s2:RelatedPackages>

```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s2=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| Minimum OS version | Windows 10 version 1803 build 17134 |
