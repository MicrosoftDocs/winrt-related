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
<dd><strong>&lt;uap13:AutoUpdate&gt;</strong></dd>
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
<uap13:AutoUpdate>

  <!-- Child Elements -->
  AppInstaller

</uap13:AutoUpdate>
```

## Attributes  and elements

### Attributes

**None.**

### Child elements

| Child Element | Description |
|-|-|
| [AppInstaller](element-uap13-autoupdate.md) | Specifies an App Installer file, which provides an update path that a Windows app can traverse searching for updates, and repairs. |

### Parent elements

| Parent Element | Description |
|-|-|
| [Extension (in Package/Applications)](element-extension.md) | Declares an extensibility point for the app. |

### Remarks

An App Installer file, declared in the manifest with the [uap13:AppInstaller](element-uap13-autoupdate.md) element, specifies where your app is located and how to update it. Declaring an App Installer file in the package manifest enables auto-update scenarios that allow the app to be updated without user intervention. For more information on auto-update, see [Auto-update and repair apps](/windows/msix/app-installer/auto-update-and-repair--overview). For more information on App Installer files, see [App Installer file overview](/windows/msix/app-installer/app-installer-file-overview).

### Requirements

| Namespace | Path |
|-|-|
| **UAP13** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |