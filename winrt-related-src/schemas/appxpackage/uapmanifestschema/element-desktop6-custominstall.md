---

title: desktop6:CustomInstall
description: Enables your desktop application to specify one or more additional installer files (.exe or .msi) that are installed with your app.

ms.date: 01/22/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:CustomInstall

## Description

Enables your desktop application to specify one or more additional installer files (.exe or .msi) that are installed with your desktop application. For example, this is useful for apps that bundle a 3rd party redistributable component. 

> [!NOTE]
> This element is currently intended to be used only by certain types of desktop PC games that are published by Microsoft and our partners. It requires the **customInstallActions** [restricted capability](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-package-extension.md">&lt;desktop6:Extension&gt;</a></dt>
<dd><b>&lt;desktop6:CustomInstall&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```xml
<desktop6:CustomInstall  Folder = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >

  <!-- Child elements -->
  ( desktop6:InstallActions
  | desktop6:RepairActions
  | desktop6:UninstallActions )?

</desktop6:CustomInstall>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Folder | The name of the package folder that contains all the files requires for all custom actions. This folder may contain subfolders. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", \|, ?, or *. | Yes |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [InstallActions](element-desktop6-installactions.md) | Specifies installer files that are run before the first launch of your desktop application.  |
| [RepairActions](element-desktop6-repairactions.md) | Specifies installer files that are run when the user selects the repair or reset options in the Settings page for your desktop application. |
| [UninstallActions](element-desktop6-uninstallactions.md) | Specifies installer files that are run when the user uninstalls your desktop application.  |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [desktop6:Extension](element-desktop6-package-extension.md) | Declares an extensibility point for the desktop application. |

## Remarks

This element requires the **customInstallActions** [restricted capability](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

The OS uses the `Name` attribute of the [desktop6:InstallAction](element-desktop6-installaction.md), [desktop6:RepairAction](element-desktop6-repairaction.md), and [desktop6:UninstallAction](element-desktop6-uninstallaction.md) elements to identify a related set of install, repair, and uninstall actions. To specify a related set of actions that should be executed in conjunction with each other, make sure they have the same value for the `Name` attribute. The OS will run an uninstall action only if the corresponding install or repair action has been run.

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

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
