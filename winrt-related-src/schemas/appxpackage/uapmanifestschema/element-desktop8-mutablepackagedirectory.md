---
title: desktop8:MutablePackageDirectory
description: Enables your desktop application to specify a folder where you can modify the installation files for your application.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/01/2023
ms.topic: reference
---

# desktop8:MutablePackageDirectory

## Description

Enables your desktop application to specify a folder where you can modify the installation files for your application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:MutablePackageDirectories\>](element-desktop8-mutablepackagedirectories.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:MutablePackageDirectory\>**

## Syntax

```xml
<desktop8:MutablePackageDirectory
  Target = 'A string that must be in the form of "$(string)\subpath" where the string is semantically validated and interpreted by calling code, and subpath is a directory subpath.'
  Shared = 'A boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Target** | Specifies a path to the folder (which will be created, and is external to `%ProgramFiles%\WindowsApps`) used to store the installation files. | A string of the form `$(string)\subpath`, where `$(string)` can be either `$(package.volumeRoot)` or `$(package.mutableroot)`, and *subpath* is a directory subpath. `$(package.volumeRoot)` denotes that *subpath* is relative to the volume root of the package; and `$(package.mutableroot)` denotes that *subpath* is relative to the mutable root (`%ProgramFiles%\ModifiableWindowsApps`). | Yes |  |
| **Shared** | Specifies whether or not the folder is a shared. | A boolean value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:MutablePackageDirectories](element-desktop8-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where you can modify the installation files for your application. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| Minimum OS Version | Windows 11 version 21H2 (Build 22000) |
