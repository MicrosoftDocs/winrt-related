---
title: desktop8:MutablePackageDirectories
description: Enables your desktop application to specify one or more folders where you can modify the installation files for your application.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop8:Extension, desktop8:MutablePackageDirectories]
---

# desktop8:MutablePackageDirectories

Enables your desktop application to specify one or more folders where you can modify the installation files for your application.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:MutablePackageDirectories>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:MutablePackageDirectories>`**

## Syntax

```xml
<desktop8:MutablePackageDirectories>

  <!-- Child elements -->
  desktop8:MutablePackageDirectory

</desktop8:MutablePackageDirectories>
```

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop8:MutablePackageDirectory](element-desktop8-mutablepackagedirectory.md) | Enables your desktop application to specify a folder where you can modify the installation files for your application. |

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
