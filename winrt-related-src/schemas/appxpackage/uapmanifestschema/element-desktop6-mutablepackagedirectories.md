---

title: desktop6:MutablePackageDirectories
description: Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods).

ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:MutablePackageDirectories

## Description

Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). 

> [!NOTE]
> This element is currently intended to be used only by certain types of desktop PC games that are published by Microsoft and our partners. It requires the **modifiableApp** [restricted capability](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-package-extension.md">&lt;desktop6:Extension&gt;</a></dt>
<dd><b>&lt;desktop6:MutablePackageDirectories&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```xml
<desktop6:MutablePackageDirectories>

  <!-- Child elements -->
  desktop6:MutablePackageDirectory

</desktop6:MutablePackageDirectories>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [MutablePackageDirectory](element-desktop6-mutablepackagedirectory.md) | Specifies a folder under the %ProgramFiles%\ModifiableWindowsApps path where the contents of your desktop application's install folder are projected so that users can modify the installation files (for example, to install mods). For more information, see [Package.MutableLocation](https://docs.microsoft.com/uwp/api/windows.applicationmodel.package.mutablelocation) and [Package.EffectiveLocation](https://docs.microsoft.com/uwp/api/windows.applicationmodel.package.effectivelocation). |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [desktop6:Extension)](element-desktop6-package-extension.md) | Declares an extensibility point for the desktop application. |

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

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
