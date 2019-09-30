---
Description: Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.
Search.Product: eADQiWindows 10XVcnh
title: ShowNameOnTiles
ms.assetid: 2d46af6c-742f-42e5-9db2-b706fd690bb1
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ShowNameOnTiles

Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-defaulttile.md">&lt;DefaultTile&gt;</a></dt>
<dd><b>&lt;ShowNameOnTiles&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ShowNameOnTiles>

  <!-- Child elements -->
  ShowOn{1,3}

</ShowNameOnTiles>
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
<td><a href="element-showon.md">ShowOn</a> </td>
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
<td><a href="element-defaulttile.md">DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This example shows how to use **ShowNameOnTiles**:

``` syntax
          <m2:ShowNameOnTiles>
            <m2:ShowOn Tile="square150x150Logo"/> // Show app name on 150x150 logo
            <m2:ShowOn Tile="wide310x150Logo"/> // Show app name on 310x150 Logo
          </m2:ShowNameOnTiles>
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
<td><p>http://schemas.microsoft.com/appx/2013/manifest</p></td>
</tr>
</tbody>
</table>

 

 



