---
author: mcleanbyron
title: desktop6:MutablePackageDirectory
description: Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods).
ms.author: mcleans
ms.date: 03/05/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:MutablePackageDirectory

## Description

Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods). This element is currently intended to be used only by certain types desktop of PC games that are published by Microsoft and our partners.


## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-package-extension.md">&lt;desktop6:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-mutablepackagedirectories.md">&lt;desktop6:MutablePackageDirectories&gt;</a></dt>
<dd><b>&lt;desktop6:MutablePackageDirectory&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```xml
<desktop6:MutablePackageDirectory Target = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. />
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Target | The name of a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods). The folder name must be string valid for a folder name. Sub-folders in the folder name are not allowed (no / or \ characters). For more information, see [Package.MutableLocation](https://docs.microsoft.com/uwp/api/windows.applicationmodel.package.mutablelocation) and [Package.EffectiveLocation](https://docs.microsoft.com/uwp/api/windows.applicationmodel.package.effectivelocation).  | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [desktop6:MutablePackageDirectories)](element-desktop6-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |


## Remarks

This element requires the **modifiableApp** [restricted capability](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

```xml
<Package
  xmlns:desktop6="http://schemas.microsoft.com/appx/manifest/desktop/windows10/6"
  xmlns:rescap= 
"http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
  IgnorableNamespaces="rescap desktop6">
 
  <!-- ... -->
  <!-- Other entries omitted for brevity. -->
  <!-- ... -->
 
  <Extensions> 
    <Extension Category="windows.mutablePackageDirectories">
      <desktop6:MutablePackageDirectories>
        <desktop6:MutablePackageDirectory target="ContosoGame"/>
      </desktop6:MutablePackageDirectories>
    </Extension>
  </Extensions>
 
  <Capabilities>
    <!-- Include the required restricted capability. -->
    <rescap:Capability Name="modifiableApp"/>
  </Capabilities>
</Package>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/6</p></td>
</tr>
</tbody>
</table>
