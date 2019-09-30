---
Description: Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.
Search.Product: eADQiWindows 10XVcnh
title: uap:ShowNameOnTiles (Windows 10)
ms.assetid: 883c601d-00b2-4903-996d-6cbab8801acd
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


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
<td><a href="element-uap-showon.md">uap:ShowOn</a> </td>
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
<td><a href="element-uap-defaulttile.md">uap:DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This example shows how to use [**ShowNameOnTiles**](https://msdn.microsoft.com/library/windows/apps/dn391685):

``` syntax
          <uap:ShowNameOnTiles>
            <uap:ShowOn Tile="square150x150Logo"/> // Show app name on 150x150 logo
            <uap:ShowOn Tile="wide310x150Logo"/> // Show app name on 310x150 Logo
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

 

 



