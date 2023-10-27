---
title: desktop8:UserMutablePackageDirectory
description: Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods).
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:UserMutablePackageDirectory

Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:UserMutablePackageDirectories\>](element-desktop8-usermutablepackagedirectories.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<deesktop8:UserMutablePackageDirectory\>**

## Syntax

```xml
<desktop8:UserMutablePackageDirectory
  Target = 'An alphanumeric string value that also accepts "/", "\", and "." characters, representing the path to a file.' />
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Target** | Specifies a path to the folder used to store the installation files. | An alphanumeric string value that also accepts "/", "\", and "." characters, representing the path to a file. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:MutablePackageDirectories](element-desktop8-usermutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| Minimum OS Version | Windows 11 version 21H2 (Build 22000) |
