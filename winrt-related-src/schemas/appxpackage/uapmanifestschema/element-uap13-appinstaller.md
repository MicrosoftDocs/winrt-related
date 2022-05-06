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

[ < Package > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Extensions > ](element-extensions.md)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< uap13:AppInstaller >**

## Syntax

``` XML
<uap13:AutoUpdate>

  <!-- Child Elements -->
  AppInstaller

</uap13:AutoUpdate>
```

## Attributes & Elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|:-:|
| File | Specifies the file which should be used to configure auto update settings. |

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