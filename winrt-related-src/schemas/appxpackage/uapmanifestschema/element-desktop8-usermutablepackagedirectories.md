---
title: desktop8:UserMutablePackageDirectories
description: Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example to install mods).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop8:Extension, desktop8:UserMutablePackageDirectories]
---

# desktop8:UserMutablePackageDirectories

Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:UserMutablePackageDirectories>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:UserMutablePackageDirectories>`**

## Syntax

```xml
<desktop8:UserMutablePackageDirectories>

  <!-- Child elements -->
  desktop8:UserMutablePackageDirectory

</desktop8:UserMutablePackageDirectories>
```

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop8:UserMutablePackageDirectory](element-desktop8-usermutablepackagedirectory.md) | Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods). |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Extension](element-desktop8-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
