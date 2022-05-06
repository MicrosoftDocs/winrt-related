---
title: uap13:AppInstaller
description: Specifies a directory containing the installation files for the app.
keywords: windows 10, uwp, schema, manifest, extension

ms.date: 05/03/2022
ms.topic: reference
---

# uap13:AppInstaller

## Description

Specifies a directory containing the installation files for the app.

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
  file = An alphanumeric string between 1 and 255 characters that cannot contain the following characters: <, >, :, ", |, ?, or *.
  >

</uap13:AppInstaller>
```

## Attributes & Elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|:-:|
| File | Specifies the file which should be used to configure auto update settings. | An alphanumeric string between 1 and 255 characters that cannot contain the following characters: <, >, :, ", &#124;, ?, or *. | Yes |

### Child Elements

**None.**

### Parent Elements

| Parent Element | Description |
|-|-|
| [uap13:AutoUpdate](element-uap13-autoupdate.md) | Specifies automatic update configuration for the app. | Should match the value "AppInstaller". The value is NOT case sensitive. | Yes |

### Requirements

| Namespace | Path |
|-|-|
| **UAP13** | `http://schemas.microsoft.com/appx/manifest/uap/windows/10/13` |