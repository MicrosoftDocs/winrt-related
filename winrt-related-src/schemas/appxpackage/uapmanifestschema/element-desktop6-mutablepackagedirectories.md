---
title: desktop6:MutablePackageDirectories
description: Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods).
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:MutablePackageDirectories

Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). 

> [!NOTE]
> This element is currently intended to be used only by certain types of desktop PC games that are published by Microsoft and our partners. It requires the **modifiableApp** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:Extension\>](element-desktop6-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop6:MutablePackageDirectories\>**

## Syntax

```xml
<desktop6:MutablePackageDirectories>

  <!-- Child elements -->
  desktop6:MutablePackageDirectory

</desktop6:MutablePackageDirectories>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [MutablePackageDirectory](element-desktop6-mutablepackagedirectory.md) | Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods). For more information, see [Package.MutableLocation](/uwp/api/windows.applicationmodel.package.mutablelocation) and [Package.EffectiveLocation](/uwp/api/windows.applicationmodel.package.effectivelocation). |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop6:Extension)](element-desktop6-package-extension.md) | Declares an extensibility point for the desktop application. |

## Remarks

This element requires the **modifiableApp** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

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
