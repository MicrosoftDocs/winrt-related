---
title: uap13:AutoUpdate
description: Specifies automatic update configuration for the app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Extensions, uap13:Package, uap13:Properties, uap13:AutoUpdate]
---

# uap13:AutoUpdate

Specifies automatic update configuration for the app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap13:AutoUpdate>`**  

## Syntax

```xml
<uap13:AutoUpdate>

  <!-- Child elements -->
  uap13:AppInstaller

</uap13:AutoUpdate>
```

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap13:AppInstaller](element-uap13-appinstaller.md) | Specifies an App Installer file, which provides an update path that a Windows app can traverse searching for updates, and repairs. |

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/13` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

An App Installer file, declared in the manifest with the [uap13:AppInstaller](element-uap13-autoupdate.md) element, specifies where your app is located and how to update it. Declaring an App Installer file in the package manifest enables auto-update scenarios that allow the app to be updated without user intervention. For more information on auto-update, see [Auto-update and repair apps](/windows/msix/app-installer/auto-update-and-repair--overview). For more information on App Installer files, see [App Installer file overview](/windows/msix/app-installer/app-installer-file-overview).

## Examples

<!-- Author content goes here -->
