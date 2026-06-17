---
title: uap:ShowNameOnTiles
description: Describes whether Windows overlays the app's name on top of the tile images that are shown on the Start screen (in Package/Applications).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Applications, uap:Application, uap:VisualElements, uap:DefaultTile, uap:ShowNameOnTiles]
---

# uap:ShowNameOnTiles

Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:VisualElements>`](element-uap-visualelements.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:DefaultTile>`](element-uap-defaulttile.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:ShowNameOnTiles>`**  

## Syntax

```xml
<uap:ShowNameOnTiles>

  <!-- Child elements -->
  uap:ShowOn{1,4}

</uap:ShowNameOnTiles>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:ShowOn](element-uap-showon.md) | Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:DefaultTile](element-uap-defaulttile.md) | The default tile that represents your app on the Start screen. The icons specified here are displayed when your app is not showing tile notifications. To dynamically change the appearance of your tile and display relevant live content, see [Send a local tile notification](/windows/uwp/controls-and-patterns/tiles-and-notifications-sending-a-local-tile-notification). |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

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
