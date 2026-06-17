---
title: uap:ShowOn
description: Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen (in Package/Applications).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:VisualElements, uap:DefaultTile, uap:ShowNameOnTiles, uap:ShowOn]
---

# uap:ShowOn

Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:VisualElements>`](element-uap-visualelements.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:DefaultTile>`](element-uap-defaulttile.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:ShowNameOnTiles>`](element-uap-shownameontiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:ShowOn>`**  

## Syntax

```xml
<uap:ShowOn
  Tile = 'A required string that can have one of the following values: "square150x150Logo", "wide310x150Logo", or "square310x310Logo".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Tile** | The size of the tile. | A string that can have one of the following values: *square150x150Logo*, *wide310x150Logo*, *square310x310Logo*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:ShowNameOnTiles](element-uap-shownameontiles.md) | Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

This example shows how to use the [ShowNameOnTiles](element-uap-shownameontiles.md) and [ShowOn](element-uap-showon.md) elements:

```xml
<uap:ShowNameOnTiles>
    <uap:ShowOn
        Tile="square150x150Logo"/> <!-- Show app name on the 150x150 tile -->
    <uap:ShowOn
        Tile="wide310x150Logo"/> <!-- …and also on the 310x150 tile -->
</uap:ShowNameOnTiles>
```
