---
title: uap5:MixedRealityModel
description: An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:MixedRealityModel

An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:DefaultTile\>](element-uap-defaulttile.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:MixedRealityMode\>**

## Syntax

```xml
<uap5:MixedRealityModel
  Path = 'A string with a value between 1 and 256 characters in length that ends with ".glb" and cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.' >

  <!-- Child elements -->
  uap6:SpatialBoundingBox?

</uap5:MixedRealityModel>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The path to the 3D asset to be used. | A string with a value between 1 and 256 characters in length that ends with `.glb` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [SpatialBoundingBox](element-uap6-spatialboundingbox.md) | Used to define the center point and the extents for a bounding volume. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:](element-uap-extension.md) |  |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
