---
description: Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen (in Package/Applications).
Search.Product: eADQiWindows 10XVcnh
title: uap:ShowOn (Windows 10)
ms.assetid: ef9ad3df-5179-4dee-bf54-4f5de545b1ed
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:ShowOn (Windows 10)

Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:DefaultTitle\>](element-uap-defaulttile.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:ShowNameOnTiles\>](element-uap-shownameontiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:ShowOn\>**

## Syntax

```xml
<uap:ShowOn
    Tile = 'A string that can have one of the following values: "square150x150Logo", "wide310x150Logo", or "square310x310Logo".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Tile** | The size of the tile. | A string that can have one of the following values: *square150x150Logo*, *wide310x150Logo*, or *square310x310Logo*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:ShowNameOnTiles](element-uap-shownameontiles.md) | Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
