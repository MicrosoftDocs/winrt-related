---
author: mcleanbyron
title: desktop6:InstallActions
description: Specifies installer files (.exe or .msi) that are run before the first launch of your desktop application.
ms.author: mcleans
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:InstallActions

## Description

Specifies installer files (.exe or .msi) that are run before the first launch of your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container.


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
<dt><a href="element-desktop6-custominstall.md">&lt;desktop6:CustomInstall&gt;</a></dt>
<dd><b>&lt;desktop6:InstallActions&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```xml
<desktop6:InstallActions>

  <!-- Child elements -->
  desktop6:InstallAction{0,100}

</desktop6:InstallActions>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [InstallAction](element-desktop6-installaction.md) | Specifies an installer file that is run before the first launch of your desktop application. |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [desktop6:CustomInstall](element-desktop6-custominstall.md) | Enables your desktop application to specify one or more additional installer files that are installed with your desktop application.  |


## Remarks

This element requires the **customInstallActions** [restricted capability](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

```xml
<Package
  xmlns:desktop6="http://schemas.microsoft.com/appx/manifest/desktop/windows10/6"
  xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
  IgnorableNamespaces="rescap desktop6">

  <!-- ... -->
  <!-- Other entries omitted for brevity. -->
  <!-- ... -->

  <Extensions>
    <desktop6:Extension Category="windows.customInstall">
      <desktop6:CustomInstall Folder="MyInstallers">
        <desktop6:InstallActions>
          <desktop6:InstallAction File="Setup_AntiCheat.exe" Name="AC_1" Arguments="/add /silent" />
        </desktop6:InstallActions>
        <desktop6:RepairActions>
          <desktop6:RepairAction File="Setup_AntiCheat.exe" Name="AC_1" Arguments="/add /silent /force" />
        </desktop6:RepairActions>
        <desktop6:UninstallActions>
          <desktop6:UninstallAction File="Setup_AntiCheat.exe" Name="AC_1" Arguments="/remove /silent" />
        </desktop6:UninstallActions>
      </desktop6:CustomInstall>
    </desktop6:Extension>
  </Extensions>

  <Capabilities>
    <rescap:Capability Name="customInstallActions"/>
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
