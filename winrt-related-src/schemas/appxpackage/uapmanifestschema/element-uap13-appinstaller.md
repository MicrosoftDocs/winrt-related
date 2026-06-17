---
title: uap13:AppInstaller
description: Specifies an App Installer file, which provides an update path that a Windows app can traverse searching for updates, and repairs.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Extensions, uap13:Package, uap13:Properties, uap13:AutoUpdate, uap13:AppInstaller]
---

# uap13:AppInstaller

Specifies an App Installer file, which provides an update path that a Windows app can traverse searching for updates, and repairs.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap13:AutoUpdate>`](element-uap13-autoupdate.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap13:AppInstaller>`**  

## Syntax

```xml
<uap13:AppInstaller
  File = 'A required value. <!-- TODO: Add description for uap13:ST_AppInstallerFilePath -->' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The package-relative path to the App Installer file. | A value. <!-- TODO: Add data type for uap13:ST_AppInstallerFilePath --> | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/13` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

An App Installer file specifies where your app is located and how to update it. Declaring an App Installer file in the package manifest enables auto-update scenarios that allow the app to be updated without user intervention. For more information on auto-update, see [Auto-update and repair apps](/windows/msix/app-installer/auto-update-and-repair--overview). For more information on App Installer files, see [App Installer file overview](/windows/msix/app-installer/app-installer-file-overview).

## Examples

<!-- Author content goes here -->
