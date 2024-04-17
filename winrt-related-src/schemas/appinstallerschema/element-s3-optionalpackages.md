---
title: s3:OptionalPackages
description: Specifies the optional packages that will be installed along with the main package. (s3:OptionalPackages)
ms.date: 02/05/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s3:OptionalPackages

## Description

Specifies the optional packages that will be installed along with the main package. (s3:OptionalPackages)


## Element Hierarchy

[s3:AppInstaller](element-s3-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s3:OptionalPackages&gt;

## Syntax

```syntax
<s3:OptionalPackages>
<!-- Child elements -->
  Package
  Bundle
</s3:OptionalPackages>
```

## Child Elements

| Element | Description |
| -----------| -------------|
| [Package](element-s3-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [Bundle](element-s3-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri.  |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s3:AppInstaller](element-s3-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Remarks

The `<OptionalPackages>` element defines the app packages that will be installed along with the main app. There can be more than one child element defined inside the `<OptionalPackages>` element. If the optional app is packaged as .appx then use the `<Package>`, and if the optional app is packaged as .appxbundle then use the `<Bundle>` element.

## Examples

```xml
<s3:OptionalPackages>
    <s3:Bundle
        Name="Contoso.OptionalApp1"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp1.appxbundle" />

    <s3:Bundle
        Name="Contoso.OptionalApp2"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp2.appxbundle" />

    <s3:Package
        Name="Fabrikam.OptionalApp3"
        Publisher="CN=Fabrikam"
        Version="10.34.54.23"
        ProcessorArchitecture="x64"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp3.appx" />

</s3:OptionalPackages>

```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s3=http://schemas.microsoft.com/appx/appinstaller/2018` | This namespace is required for features introduced in Windows 10, version 1809. |
| Minimum OS version | Windows 10 version 1809 |
