---

title: desktop6:UninstallAction
description: Specifies an installer file (.exe or .msi) that is run when the user selects the repair or reset options in the Settings page for your desktop application.

ms.date: 01/22/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:UninstallAction


## Description
Specifies an installer file (.exe or .msi) that is run when the user uninstalls your desktop application. This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container.

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
<dd>
<dl>
<dt><a href="element-desktop6-uninstallactions.md">&lt;desktop6:UninstallActions&gt;</a></dt>
<dd><b>&lt;desktop6:UninstallAction&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop6:UninstallAction   File       = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                            Name       = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                            Arguments  = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. />
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| File | The name of the file to execute (.exe or .msi). This file must exist in your package. You can specify a path that is relative to the *Folder* attribute of the [desktop6.CustomInstall](element-desktop6-custominstall.md) element. You cannot specify an absolute path, and the relative path must not start with a ```\``` character. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |
| Name | The name for the uninstall action. This name is used to identify the uninstall action, and the OS uses this name to track which actions have been successfully executed. Make sure that this value matches the `Name` attribute for the corresponding [desktop6:InstallAction](element-desktop6-installaction.md) and [desktop6:RepairAction](element-desktop6-repairaction.md) elements that you want to run as part of the same sequence. This name must be unique in the parent [desktop6:UninstallActions](element-desktop6-uninstallactions.md) element, but it can be shared by other actions under the [desktop6:InstallActions](element-desktop6-installactions.md) and [desktop6:RepairActions](element-desktop6-repairactions.md) elements. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| Arguments | Optional arguments to pass to the installer file. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

### Child Elements

None

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [desktop6:UninstallActions](element-desktop6-uninstallactions.md) | Specifies installer files (.exe or .msi) that are run when the user uninstalls your desktop application.  |

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
