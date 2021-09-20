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
<dd>
<dl>
<dt><a href="element-uap-shownameontiles.md">&lt;uap:ShowNameOnTiles&gt;</a></dt>
<dd><b>&lt;uap:ShowOn&gt;</b></dd>
</dl>
</dd>
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
<ShowOn Tile = "square150x150Logo" | "wide310x150Logo" | "square310x310Logo" />
```

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Tile</strong></td>
<td><p>The tile size.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>square150x150Logo</li>
<li>wide310x150Logo</li>
<li>square310x310Logo</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

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
<td><a href="element-uap-shownameontiles.md">uap:ShowNameOnTiles</a> </td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.</p></td>
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

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 



