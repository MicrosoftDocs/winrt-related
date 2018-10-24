---
Description: Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.
Search.Product: eADQiWindows 10XVcnh
title: uap:ShowNameOnTiles (Windows 10)
ms.assetid: 883c601d-00b2-4903-996d-6cbab8801acd
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# uap:ShowNameOnTiles (Windows 10)


Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.

## Element hierarchy

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
<dt><a href="element-uap-visualelements.md">&lt;uap:VisualElements&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-defaulttile.md">&lt;uap:DefaultTile&gt;</a></dt>
<dd><b>&lt;uap:ShowNameOnTiles&gt;</b></dd>
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

``` syntax
<ShowNameOnTiles>

  <!-- Child elements -->
  uap:ShowOn{1,4}

</uap:ShowNameOnTiles>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

None.

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[uap:ShowOn](element-uap-showon.md)</td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile image that is shown on the Start screen.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[uap:DefaultTile](element-uap-defaulttile.md)</td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
</tbody>
</table>

 

## Examples

This example shows how to use the [**ShowNameOnTiles**](element-uap-shownameontiles.md) and [**ShowOn**](element-uap-showon.md) elements:

``` XML
<uap:ShowNameOnTiles>
    <uap:ShowOn Tile="square150x150Logo"/> <!-- Show app name on the 150x150 tile -->
    <uap:ShowOn Tile="wide310x150Logo"/> <!-- …and also on the 310x150 tile -->
</uap:ShowNameOnTiles>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



