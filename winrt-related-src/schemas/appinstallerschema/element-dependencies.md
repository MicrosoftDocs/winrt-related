---
author: laurenhughes
ms.author: lahugh
title: Dependencies
description: Defines the dependency packages that are required for successful deployment of the related set. This element is optional.
ms.topic: reference
ms.date: 10/10/2017


keywords: windows 10, uwp, app installer, AppInstaller, sideload, related set, optional packages
---

# Dependencies

Defines the dependency packages that are required for successful deployment of the related set. This element is optional. 

## Element hierarchy

<dl>
<dt><a href="element-appinstaller.md">&lt;AppInstaller&gt;</a></dt>
<dd>
    <dl>
        <dt>**Dependencies**</dt>
    </dl>
</dd>
</dl>

## Syntax
```syntax
<Dependencies>
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
These packages will only be installed if they are not already available on the target device. 

## Examples
The following example is taken from a sample appinstaller file. The Uri location doesn't exist.  

``` xml
  <Dependencies>
    <Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x86" Uri="http://foobarbaz.com/fwkx86.appx" />
    <Package Name="Microsoft.VCLibs.140.00" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="14.0.24605.0" ProcessorArchitecture="x64" Uri="http://foobarbaz.com/fwkx64.appx" />
  </Dependencies>

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