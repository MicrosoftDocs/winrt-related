---
title: s4:RelatedPackages
description: Specifies the related packages. These packages won't be installed as part of the deployment operation. (s4:RelatedPackages)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:RelatedPackages

## Description

Specifies the related packages. These packages won't be installed as part of the deployment operation. (s4:RelatedPackages)

## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:RelatedPackages&gt;

## Syntax

```syntax
<s4:RelatedPackages>
<!-- Child elements -->
  ( Bundle{0,10000}
  | Package{0,10000}
  )
</s4:RelatedPackages>
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

The **RelatedPackages** element defines the app packages that are specified in the main app pacakge but will not be installed along with the main app. There can be more than one child element defined inside the **RelatedPackages** element. If the app is packaged as .appx then use the **Package**, and if the app is packaged as .appxbundle then use the **Bundle** element.

## Examples

The following example is taken from a sample appinstaller file. The Uri location doesn't exist. 

```xml
<s4:RelatedPackages>
    <s4:Bundle
        Name="Fabrikam.RelatedApp1"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/RelatedApp1.appxbundle" />

    <s4:Package
        Name="Fabrikam.RelatedApp2"
        Publisher="CN=Fabrikam"
        Version="10.34.54.23"
        ProcessorArchitecture="x64"
        Uri="http://mywebservice.azurewebsites.net/RelatedApp2.appx" />

</s4:RelatedPackages>

```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
