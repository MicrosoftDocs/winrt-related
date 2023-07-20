---
title: uap13:AppInstaller
description: Specifies an App Installer file, which provides an update path that a Windows app can traverse searching for updates, and repairs.
keywords: windows 10, uwp, schema, manifest, extension
ms.date: 05/03/2022
ms.topic: reference
---

# uap13:AppInstaller

Specifies an App Installer file, which provides an update path that a Windows app can traverse searching for updates, and repairs.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;[\<uap13:AutoUpdate\>](element-uap13-autoupdate.md)

 &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap13:AppInstaller\>**

## Syntax

``` XML
<uap13:AppInstaller 
  file = 'An alphanumeric string with a value between 1 and 255 characters that ends with the extension ".appinstaller". The string cannot contain the following characters: <, >, :, ", |, ?, or *.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The package-relative path to the App Installer file. | An alphanumeric string with a value between 1 and 255 characters that ends with the extension `.appinstaller`. The string cannot contain the following characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. |

### Remarks

An App Installer file specifies where your app is located and how to update it. Declaring an App Installer file in the package manifest enables auto-update scenarios that allow the app to be updated without user intervention. For more information on auto-update, see [Auto-update and repair apps](/windows/msix/app-installer/auto-update-and-repair--overview). For more information on App Installer files, see [App Installer file overview](/windows/msix/app-installer/app-installer-file-overview).

### Requirements

| Item | Value |
|-|-|
| **UAP13** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |
