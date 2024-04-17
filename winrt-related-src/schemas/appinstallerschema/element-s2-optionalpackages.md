---
title: s2:OptionalPackages
description: Specifies the optional packages that will be installed along with the main package. (s2:OptionalPackages)
ms.date: 02/06/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s2:OptionalPackages



## Description

Specifies the optional packages that will be installed along with the main package. (s2:OptionalPackages)

## Element Hierarchy

[s2:AppInstaller](element-s2-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s2:OptionalPackages&gt;

## Syntax
```syntax
<s2:OptionalPackages>
<!-- Child elements -->
  s2:Package{0,1}
  s2:Bundle{0,1}
</s2:OptionalPackages>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [s2:Package](element-s2-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [s2:Bundle](element-s2-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri.  |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s2:AppInstaller](element-s2-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Remarks

The `<OptionalPackages>` element defines the app packages that will be installed along with the main app. There can be more than one child element defined inside the `<OptionalPackages>` element. If the optional app is packaged as .appx then use the `<Package>`, and if the optional app is packaged as .appxbundle then use the `<Bundle>` element.

## Examples

```xml
<s2:OptionalPackages>
    <s2:Bundle
        Name="Contoso.OptionalApp1"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp1.appxbundle" />

    <s2:Bundle
        Name="Contoso.OptionalApp2"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp2.appxbundle" />

    <s2:Package
        Name="Fabrikam.OptionalApp3"
        Publisher="CN=Fabrikam"
        Version="10.34.54.23"
        ProcessorArchitecture="x64"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp3.appx" />

</s2:OptionalPackages>

```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s2=http://schemas.microsoft.com/appx/appinstaller/2017/2` | This namespace is required for features introduced in Windows 10, version 1803. |
| Minimum OS version | Windows 10 version 1803 build 17134 |
