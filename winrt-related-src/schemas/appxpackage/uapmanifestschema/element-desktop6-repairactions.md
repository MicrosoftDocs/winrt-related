---
title: desktop6:RepairActions
description: Specifies installer files (.exe or .msi) that are run when the user selects the repair or reset options in the Settings page for your desktop application.
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:RepairActions

Specifies installer files (.exe or .msi) that are run when the user selects the repair or reset options in the Settings page for your desktop application.

> [!NOTE]
> This element is currently intended to be used only by desktop PC games that are packaged in an MSIXVC container. It requires the **customInstallActions** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:Extension\>](element-desktop6-package-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:CustomInstall\>](element-desktop6-custominstall.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop6:RepairActions\>**

## Syntax

```xml
<desktop6:RepairActions>

  <!-- Child elements -->
  desktop6:RepairAction{0,100}

</desktop6:RepairActions>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [RepairAction](element-desktop6-repairaction.md) | Specifies an installer file (.exe or .msi) that is run when the user selects the repair or reset options in the Settings page for your desktop application. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop6:CustomInstall](element-desktop6-custominstall.md) | Enables your desktop application to specify one or more additional installer files (.exe or .msi) that are installed with your desktop application.  |

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

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
