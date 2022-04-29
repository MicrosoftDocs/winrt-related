---
title: desktop8:MutablePackageDirectory
description: Enables your desktop application to specify a folder where you can modify the installation files for your application.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:MutablePackageDirectory

## Description

Enables your desktop application to specify a folder where you can modify the installation files for your application.

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
<dt><a href="element-desktop8-mutablepackagedirectories.md">&lt;desktop8:MutablePackageDirectories&gt;</a></dt>
<dd><strong>&lt;desktop8:MutablePackageDirectory&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:MutablePackageDirectory
          Target = A string that must be in the form of $(string)\subpath where the string is semantically validated and interpreted by calling code, and subpath is a directory subpath.
          Shared = A boolean value.
          >

</desktop8:MutablePackageDirectory>
```

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Target | Specifies a path to the folder used to store the installation files. | A string that must be in the form of $(string)\subpath where the string is semantically validated and interpreted by calling code, and subpath is a directory subpath. | Yes |
| Shared | Specifies whether or not the folder is a shared. | A boolean value. | No |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [desktop8:MutablePackageDirectories](element-desktop8-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where you can modify the installation files for your application. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |