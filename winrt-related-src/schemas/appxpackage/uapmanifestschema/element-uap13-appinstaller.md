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

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap13-autoupdate.md">&lt;uap13:AutoUpdate</a></dt>
<dd><strong>&lt;uap13:AppInstaller&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` XML
<uap13:AppInstaller 
  file = An alphanumeric string between 1 and 255 characters that ends with the extension .appinstaller and cannot contain the following characters: <, >, :, ", |, ?, or *.
  >

</uap13:AppInstaller>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|:-:|
| File | The package-relative path to the App Installer file. | An alphanumeric string between 1 and 255 characters that ends with the extension .appinstaller and cannot contain the following characters: <, >, :, ", &#124;, ?, or *. | Yes |

### Child elements

**None.**

### Parent elements

| Parent element | Description |
|-|-|
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. |

### Remarks

An App Installer file specifies where your app is located and how to update it. Declaring an App Installer file in the package manifest enables auto-update scenarios that allow the app to be updated without user intervention. For more information on auto-update, see [Auto-update and repair apps](/windows/msix/app-installer/auto-update-and-repair--overview). For more information on App Installer files, see [](/windows/msix/app-installer/app-installer-file-overview).

### Requirements

| Namespace | Path |
|-|-|
| **UAP13** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |