---
title: uap13:AutoUpdate
description: Specifies automatic update configuration for the app.
keywords: windows 10, uwp, schema, manifest, extension
ms.date: 05/03/2022
ms.topic: reference
---

# uap13:AutoUpdate

Specifies automatic update configuration for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap13:AutoUpdate\>**

## Syntax

```xml
<uap13:AutoUpdate>

  <!-- Child Elements -->
  AppInstaller

</uap13:AutoUpdate>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [AppInstaller](element-uap13-appinstaller.md) | Specifies an `.appinstaller` file, which provides an update path that a Windows app can traverse searching for updates and repairs. |

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

### Remarks

An App Installer file, declared in the manifest with the [uap13:AppInstaller](element-uap13-autoupdate.md) element, specifies where your app is located and how to update it. Declaring an App Installer file in the package manifest enables auto-update scenarios that allow the app to be updated without user intervention. For more information on auto-update, see [Auto-update and repair apps](/windows/msix/app-installer/auto-update-and-repair--overview). For more information on App Installer files, see [App Installer file overview](/windows/msix/app-installer/app-installer-file-overview).

### Requirements

| Item | Value |
|-|-|
| **UAP13** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |
