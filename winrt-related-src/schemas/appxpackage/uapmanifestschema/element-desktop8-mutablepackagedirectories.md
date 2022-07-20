---
title: desktop8:MutablePackageDirectories
description: Enables your desktop application to specify one or more folders where you can modify the installation files for your application.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:MutablePackageDirectories

## Description

Enables your desktop application to specify one or more folders where you can modify the installation files for your application.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</dt>
<dd>
<dl>
<dt><a href="element-desktop8-extension.md">&lt;desktop8:Extension&gt;</a></dt>
<dd><strong>&lt;desktop8:MutablePackageDirectories&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:MutablePackageDirectories>

  <!-- Child Elements -->
  desktop8:MutablePackageDirectory

</desktop8:MutablePackageDirectories>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:MutablePackageDirectory](element-desktop8-mutablepackagedirectory.md) | Enables your desktop application to specify a folder where you can modify the installation files for your application. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:Extension (in Package/Application)](element-1-extensions.md) | Declares an extensibility point for the application. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |