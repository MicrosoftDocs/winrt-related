---
title: uap6:SpatialBoundingBox
description: Used to define the center point and the extents for a bounding volume.
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# uap6:SpatialBoundingBox

Used to define the center point and the extents for a bounding volume.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:DefaultTile\>](element-uap-defaulttile.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:MixedRealityModel\>](element-uap5-mixedrealitymodel.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap6:SpatialBoundingBox\>**

## Syntax

```xml
<uap6:SpatialBoundingBox
  Center = 'Vector coordinates in the form: "X, Y, Z". Vector values must be numeric and can contain decimal and negative values.'
  Extents = 'Either vector coordinates in the form: "X, Y, Z" (vector values must be numeric and can contain decimal and negative values) or the string: "Auto".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Center** | Vector coordinates of the center of the bounding box. | Vector coordinates in the form: `X, Y, Z`. Vector values must be numeric and can contain decimal and negative values. | Yes |  |
| **Extents** | Either vector coordinates or "Auto" sizing extent of a the bounding box. | Either vector coordinates in the form: `X, Y, Z` (vector values must be numeric and can contain decimal and negative values) or the string: `Auto`. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:MixedRealityModel](element-uap5-mixedrealitymodel.md) | An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
