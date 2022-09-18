---
description: Describes whether Windows overlays the app's name on top of the tile images that are shown on the Start screen (in Package/Applications).
Search.Product: eADQiWindows 10XVcnh
title: uap:ShowNameOnTiles (Windows 10)
ms.assetid: 883c601d-00b2-4903-996d-6cbab8801acd
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:ShowNameOnTiles (Windows 10)

Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:DefaultTitle\>](element-uap-defaulttile.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:ShowNameOnTiles\>**

## Syntax

```xml
<ShowNameOnTiles>

  <!-- Child elements -->
  uap:ShowOn{1,4}

</uap:ShowNameOnTiles>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:ShowOn](element-uap-showon.md) | Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:DefaultTile](element-uap-defaulttile.md) | The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default. |

## Examples

This example shows how to use the [ShowNameOnTiles](element-uap-shownameontiles.md) and [ShowOn](element-uap-showon.md) elements:

``` XML
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
