---
description: The default tile that represents the app on the Start screen (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:DefaultTile (Windows 10)
ms.assetid: 0ee61279-efa8-4bd9-b713-1f5f9ec526f7
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:DefaultTile (Windows 10)

The default tile that represents your app on the Start screen. The icons specified here are displayed when your app is not showing tile notifications. To dynamically change the appearance of your tile and display relevant live content, see [Send a local tile notification](/windows/uwp/controls-and-patterns/tiles-and-notifications-sending-a-local-tile-notification).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:VisualElements\>](element-uap-visualelements.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:DefaultTitle\>**

## Syntax

```xml
<uap:DefaultTile
  Wide310x150Logo = 'An optional string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. Additionally, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.'
  Square310x310Logo = 'An optional string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.'
  Square71x71Logo = 'An optional string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.'
  ShortName = 'An optional string with a value between 1 and 40 characters in length.' >

  <!-- Child elements -->
  uap:TileUpdate?
  & uap:ShowNameOnTiles?
  & uap5:MixedRealityModel?

</uap:DefaultTile>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ShortName** | A short name for the app that is displayed directly on the tile. This string is localizable; for more info, see Remarks. | An optional string with a value between 1 and 40 characters in length. | No |  |
| **Wide310x150Logo** | The 310x150 wide version of the logo image. This image is displayed when the tile is displayed in its wide format. If this image is not provided, the tile can only display in the square format and can't accept notifications based on [wide template types](/previous-versions/windows/apps/hh761491(v=win.10)). The user has the ultimate choice as to which format the tile uses, so it is a best practice to include a wide logo image. If a wide logo image is provided, the tile will be shown initially in its wide format. For more info about required logo dimensions, see [Tile sizes](/previous-versions/windows/apps/hh781198(v=win.10)). | An optional string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Additionally, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |
| **Square310x310Logo** | The 310x310 square version of the logo image. | An optional string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Additionally, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |
| **Square71x71Logo** | The 71x71 square version of the logo image. | An optional string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Additionally, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap:ShowNameOnTiles](element-uap-shownameontiles.md) | Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen. |
| [uap:TileUpdate](element-uap-tileupdate.md) | Describes how the app tile receives update notifications. |
| [uap5:MixedRealityModel](element-uap5-MixedRealityModel.md) | An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |

## Remarks

For the **Wide310x150Logo**, **Square310x310Logo**, **Square71x71Logo**, and **Tall150x310Logo** images, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **ShortName** attribute. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
