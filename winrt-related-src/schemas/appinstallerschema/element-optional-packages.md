---
author: laurenhughes
ms.author: lahugh
title: OptionalPackages
description: Defines the optional packages that will be installed along with the main package.
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# OptionalPackages

Defines the optional packages that will be installed along with the main package.  

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt>**OptionalPackages**</dt>
    </dl>
</dd>
</dl>

## Syntax
```syntax
<OptionalPackages>
  <!-- Child elements -->
  ( Bundle{0,10000}
  | Package{0,10000}
  )
</OptionalPackages>

```

### Key
`{}`   specific range of occurrences

## Attributes and Elements

### Attributes
None

### Child Elements

| Child Elements | Description |
|----------------|-------------|
| [Bundle](element-bundle.md)           | Element that includes information about the app bundle. The child elements of this element requires an exact match of the name, publisher and version from the identity element in the app package bundle manifest.            |
| [Package](element-package.md)           | Element that includes information about the  package. This elements requires an exact match of the name, publisher and version from the identity element in the app package manifest. ProcessorArchitecture is an optional element.            |

### Parent Elements

| Parent Elements | Description |
|-----------------|-------------|
| [AppInstaller](element-appinstaller.md)            | The root element of the appinstaller document.            |

## Remarks

The `<OptionalPackages>` element defines the app packages that will be installed along with the main app. There can be more than one child element defined inside the `<OptionalPackages>` element. If the optional app is packaged as .appx then use the `<Package>`, and if the optional app is packaged as .appxbundle then use the `<Bundle>` element.

## Examples
```xml
    <OptionalPackages>
        <Bundle
            Name="Contoso.OptionalApp1"
            Publisher="CN=Contoso"
            Version="2.23.12.43"
            Uri="http://mywebservice.azurewebsites.net/OptionalApp1.appxbundle" />

        <Bundle
            Name="Contoso.OptionalApp2"
            Publisher="CN=Contoso"
            Version="2.23.12.43"
            Uri="http://mywebservice.azurewebsites.net/OptionalApp2.appxbundle" />

        <Package
            Name="Fabrikam.OptionalApp3"
            Publisher="CN=Fabrikam"
            Version="10.34.54.23"
            ProcessorArchitecture="x64"
            Uri="http://mywebservice.azurewebsites.net/OptionalApp3.appx" />

    </OptionalPackages>

```
## Requirements
<table>
    <tbody>
        <tr>
            <td>Namespace</td>
            <td> http://schemas.microsoft.com/appx/appinstaller/2017 </td>
        </tr>
    </tbody>
</table>