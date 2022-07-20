---
title: desktop8:UserMutablePackageDirectory
description: Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods).
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:UserMutablePackageDirectory

## Description

Enables your desktop application to specify a folder where users can modify the installation files for your application (for example, to install mods).

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</dt>
<dd>
<dl>
<dt><a href="element-desktop8-extension.md">&lt;desktop8:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop8-usermutablepackagedirectories.md">&lt;desktop8:UserMutablePackageDirectories&gt;</a></dt>
<dd><strong>&lt;desktop8:UserMutablePackageDirectory&gt;</strong></dd>
</dd>
</dl>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:UserMutablePackageDirectory
          Target = An alphanumeric string that can also accept "/", "\", and/or "." characters representing the path to a file.
          >

</desktop8:UserMutablePackageDirectory>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Target | Specifies a path to the folder used to store the installation files. | An alphanumeric string that can also accept "/", "\\", and/or "." characters representing the path to a file. | Yes |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:MutablePackageDirectories](element-desktop8-usermutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |