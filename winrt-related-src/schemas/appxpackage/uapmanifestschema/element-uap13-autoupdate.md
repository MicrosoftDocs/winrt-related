---
title: uap13:AutoUpdate
description: Specifies automatic update configuration for the app.
keywords: windows 10, uwp, schema, manifest, extension

ms.date: 05/03/2022
ms.topic: reference
---

# uap13:AutoUpdate

## Description

Specifies automatic update configuration for the app.

## Element Hierarchy

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

## Attributes & Elements

### Attributes

**None.**

### Child Elements

| Child Element | Description |
|-|-|
| AppInstaller | Specifies a directory containing the installation files for the app. |

### Parent Elements

| Parent Element | Description |
|-|-|
| [Extension (in Package/Applications)](element-extension.md) | Declares an extensibility point for the app. |

### Requirements

| Namespace | Path |
|-|-|
| **UAP13** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |