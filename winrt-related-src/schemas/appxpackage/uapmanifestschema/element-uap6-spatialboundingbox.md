---
title: uap6:SpatialBoundingBox
description: Used to define the center point and the extents for a bounding volume.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Extensions, uap6:Package, uap6:Applications, uap6:Application, uap6:VisualElements, uap6:DefaultTile, uap6:MixedRealityModel, uap6:SpatialBoundingBox]
---

# uap6:SpatialBoundingBox

Used to define the center point and the extents for a bounding volume.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:VisualElements>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:DefaultTile>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:MixedRealityModel>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap6:SpatialBoundingBox>`**  

## Syntax

```xml
<uap6:SpatialBoundingBox
  Center = 'Vector coordinates in the form: "X, Y, Z". Vector values must be numeric and can contain decimal and negative values.'
  Extents = 'Either vector coordinates in the form: "X, Y, Z" (vector values must be numeric and can contain decimal and negative values) or the string: "Auto".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Center** | Vector coordinates of the center of the bounding box. | Vector coordinates in the form: `X, Y, Z`. Vector values must be numeric and can contain decimal and negative values. | Yes |  |
| **Extents** | Either vector coordinates or "Auto" sizing extent of a the bounding box. | Either vector coordinates in the form: `X, Y, Z` (vector values must be numeric and can contain decimal and negative values) or the string: `Auto`. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:MixedRealityModel](element-uap5-mixedrealitymodel.md) | An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->