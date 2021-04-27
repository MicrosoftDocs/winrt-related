---


title: RelatedPackages
description: An optional element that is used to specify the other optional packages that are specified in the main app package. These packages will not be installed as part of the deployment operation.
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# RelatedPackages

An optional element that is used to specify the other optional packages that are specified in the main app package. These packages will not be installed as part of the deployment operation.  

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt>**RelatedPackages**</dt>
    </dl>
</dd>
</dl>

## Syntax
``` xml
<RelatedPackages>

  <!-- Child elements -->
  ( Bundle{0,10000}
  | Package{0,10000}
  )
</RelatedPackages>

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

The **RelatedPackages** element defines the app packages that are specified in the main app pacakge but will not be installed along with the main app. There can be more than one child element defined inside the **RelatedPackages** element. If the app is packaged as .appx then use the **Package**, and if the app is packaged as .appxbundle then use the **Bundle** element.

## Examples

The following example is taken from a sample appinstaller file. The Uri location doesn't exist. 

```xml
    <RelatedPackages>
        <Bundle
            Name="Fabrikam.RelatedApp1"
            Publisher="CN=Contoso"
            Version="2.23.12.43"
            Uri="http://mywebservice.azurewebsites.net/RelatedApp1.appxbundle" />

        <Package
            Name="Fabrikam.RelatedApp2"
            Publisher="CN=Fabrikam"
            Version="10.34.54.23"
            ProcessorArchitecture="x64"
            Uri="http://mywebservice.azurewebsites.net/RelatedApp2.appx" />

    </RelatedPackages>

```
## Requirements
|               |     Object                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/appinstaller/2017` |