---
title: desktop6:UninstallAction
description: Specifies an installer file (.exe or .msi) that is run when the user selects the repair or reset options in the Settings page for your desktop application (desktop6:UninstallAction).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop6:Extension, desktop6:CustomInstall, desktop6:UninstallActions, desktop6:UninstallAction]
---

# desktop6:UninstallAction

Specifies an installer file (`.exe` or `.msi`) that is run when the user uninstalls your desktop application.

> [!NOTE]
> This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container. It requires the **customInstallActions** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:CustomInstall>`](element-desktop6-custominstall.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:UninstallActions>`](element-desktop6-uninstallactions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:UninstallAction>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:CustomInstall>`](element-desktop6-custominstall.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:UninstallActions>`](element-desktop6-uninstallactions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:UninstallAction>`**

## Syntax

```xml
<desktop6:UninstallAction
  File = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  Name = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Arguments = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The name of the file to execute (.exe or .msi). This file must exist in your package. You can specify a path that is relative to the *Folder* attribute of the [desktop6.CustomInstall](element-desktop6-custominstall.md) element. You cannot specify an absolute path, and the relative path must not start with a `\` character. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
| **Name** | The name for the uninstall action. This name is used to identify the uninstall action, and the OS uses this name to track which actions have been successfully executed. Make sure that this value matches the `Name` attribute for the corresponding [desktop6:InstallAction](element-desktop6-installaction.md) and [desktop6:RepairAction](element-desktop6-repairaction.md) elements that you want to run as part of the same sequence. This name must be unique in the parent [desktop6:UninstallActions](element-desktop6-uninstallactions.md) element, but it can be shared by other actions under the [desktop6:InstallActions](element-desktop6-installactions.md) and [desktop6:RepairActions](element-desktop6-repairactions.md) elements. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Arguments** | Optional arguments to pass to the installer file. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:UninstallActions](element-desktop6-uninstallactions.md) | Specifies installer files (`.exe` or `.msi`) that are run when the user uninstalls your desktop application. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |

## Remarks

This element requires the **customInstallActions** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

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
