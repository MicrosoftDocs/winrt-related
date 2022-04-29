---
title: desktop8:UserMutablePackageDirectories
description: Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods).
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:UserMutablePackageDirectories

## Description

Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods).

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</dt>
<dd>
<dl>
<dt><a href="element-desktop8-extension.md">&lt;desktop8:Extension&gt;</a></dt>
<dd><strong>&lt;desktop8:UserMutablePackageDirectories&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:UserMutablePackageDirectories>

  <!-- Child Elements -->
  desktop8:UserMutablePackageDirectory

</desktop8:UserMutablePackageDirectories>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:UserMutablePackageDirectory](element-desktop8-usermutablepackagedirectory.md) | Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods). |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Extension (in Package/Application)](element-1-extensions.md) | Declares an extensibility point for the application. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |