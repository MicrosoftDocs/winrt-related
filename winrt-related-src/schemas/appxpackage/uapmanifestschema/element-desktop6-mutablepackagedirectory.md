---
title: desktop6:MutablePackageDirectory
description: Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods).
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:MutablePackageDirectory

Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods).

> [!NOTE]
> This element is currently intended to be used only by certain types of desktop PC games that are published by Microsoft and our partners. It requires the **modifiableApp** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:Extension\>](element-desktop6-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:MutablePackageDirectories\>](element-desktop6-mutablepackagedirectories.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<MutablePackageDirectory\>**

## Syntax

```xml
<desktop6:MutablePackageDirectory
  Target = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' />
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Target** | The name of a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods). The folder name must be string valid for a folder name. Sub-folders in the folder name are not allowed (no / or \ characters). For more information, see [Package.MutableLocation](/uwp/api/windows.applicationmodel.package.mutablelocation) and [Package.EffectiveLocation](/uwp/api/windows.applicationmodel.package.effectivelocation).  | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|-|-|
| [desktop6:MutablePackageDirectories](element-desktop6-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |

## Remarks

This element requires the **modifiableApp** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

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
    <desktop6:Extension Category="windows.mutablePackageDirectories">
      <desktop6:MutablePackageDirectories>
        <desktop6:MutablePackageDirectory Target="ContosoGame"/>
      </desktop6:MutablePackageDirectories>
    </desktop6:Extension>
  </Extensions>
 
  <Capabilities>
    <!-- Include the required restricted capability. -->
    <rescap:Capability Name="modifiableApp"/>
  </Capabilities>
</Package>
```

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |
