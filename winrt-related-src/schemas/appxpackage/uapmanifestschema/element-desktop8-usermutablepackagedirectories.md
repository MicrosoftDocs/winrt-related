---
title: desktop8:UserMutablePackageDirectories
description: Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example to install mods).
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:UserMutablePackageDirectories

Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:UserMutablePackageDirectories\>**

## Syntax

```xml
<desktop8:UserMutablePackageDirectories>

  <!-- Child Elements -->
  desktop8:UserMutablePackageDirectory

</desktop8:UserMutablePackageDirectories>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop8:UserMutablePackageDirectory](element-desktop8-usermutablepackagedirectory.md) | Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods). |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Extension (in Package/Application)](element-1-extensions.md) | Declares an extensibility point for the application. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
