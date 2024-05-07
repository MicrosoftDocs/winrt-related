---
title: s4:OptionalPackages
description: Specifies the optional packages that will be installed along with the main package. (s4:OptionalPackages)
ms.date: 01/30/2024
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, package 
---

# s4:OptionalPackages

## Description

Specifies the optional packages that will be installed along with the main package. (s4:OptionalPackages)


## Element Hierarchy

[s4:AppInstaller](element-s4-appinstaller.md)

&nbsp;&nbsp;&nbsp;&nbsp; &lt;s4:OptionalPackages&gt;

## Syntax

```syntax
<s4:OptionalPackages>
<!-- Child elements -->
  ( Bundle{0,10000}
  | Package{0,10000}
  )
</s4:OptionalPackages>
```

### Key

`{}`   specific range of occurrences


## Child Elements

| Element | Description |
| -----------| -------------|
| [Package](element-s4-package.md) | Specifies the information about a package, including name, publisher, version and uri. |
| [Bundle](element-s4-bundle.md) | Specifies the information about a bundle, including name, publisher, version and uri.  |

## Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [s4:AppInstaller](element-s4-optionalpackages.md) | Defines the root element of an AppInstaller file. |

## Remarks

The `<OptionalPackages>` element defines the app packages that will be installed along with the main app. There can be more than one child element defined inside the `<OptionalPackages>` element. If the optional app is packaged as .appx then use the `<Package>`, and if the optional app is packaged as .appxbundle then use the `<Bundle>` element.

## Examples

```xml
<s4:OptionalPackages>
    <s4:Bundle
        Name="Contoso.OptionalApp1"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp1.appxbundle" />

    <s4:Bundle
        Name="Contoso.OptionalApp2"
        Publisher="CN=Contoso"
        Version="2.23.12.43"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp2.appxbundle" />

    <s4:Package
        Name="Fabrikam.OptionalApp3"
        Publisher="CN=Fabrikam"
        Version="10.34.54.23"
        ProcessorArchitecture="x64"
        Uri="http://mywebservice.azurewebsites.net/OptionalApp3.appx" />

</s4:OptionalPackages>

```

## Requirements

| Requirement | Value |
| ---------------| -------------------------------------------------------------|
| `xmlns:s4=http://schemas.microsoft.com/appx/appinstaller/2021` | This namespace is required for features introduced in Windows version 21H2 build 22000 |
| Minimum OS version | Windows version 21H2 build 22000 |
