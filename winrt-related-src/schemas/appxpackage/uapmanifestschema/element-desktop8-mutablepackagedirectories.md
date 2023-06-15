---
title: desktop8:MutablePackageDirectories
description: Enables your desktop application to specify one or more folders where you can modify the installation files for your application.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:MutablePackageDirectories

Enables your desktop application to specify one or more folders where you can modify the installation files for your application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:MutablePackageDirectories\>**

## Syntax

```xml
<desktop8:MutablePackageDirectories>

  <!-- Child Elements -->
  desktop8:MutablePackageDirectory

</desktop8:MutablePackageDirectories>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop8:MutablePackageDirectory](element-desktop8-mutablepackagedirectory.md) | Enables your desktop application to specify a folder where you can modify the installation files for your application. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Extension (in Package/Application)](element-1-extensions.md) | Declares an extensibility point for the application. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
