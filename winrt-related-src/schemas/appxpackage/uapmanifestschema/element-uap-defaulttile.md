---
Description: The default tile that represents the app on the Start screen.
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
<dd><b>&lt;uap:DefaultTile&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DefaultTile Wide310x150Logo?   = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                 Square310x310Logo? = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                 Square71x71Logo?   = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
                 ShortName?         = A string between 1 and 40 characters in length. >

  <!-- Child elements -->
  ( uap:TileUpdate?
  & uap:ShowNameOnTiles?
  & uap5:MixedRealityModel?
  )

</uap:DefaultTile>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

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
<td><strong>ShortName</strong></td>
<td><p>A short name for the app that is displayed directly on the tile. This string is localizable; for more info, see Remarks.</p></td>
<td>A string between 1 and 40 characters in length.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Square310x310Logo</strong></td>
<td><p>The 310x310 square version of the logo image.</p>
<p>For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Square71x71Logo</strong></td>
<td><p>The 71x71 square version of the logo image.</p>
<p>For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Wide310x150Logo</strong></td>
<td><p>The 310x150 wide version of the logo image. This image is displayed when the tile is displayed in its wide format. If this image is not provided, the tile can only display in the square format and can't accept notifications based on <a href="https://msdn.microsoft.com/library/windows/apps/hh761491">wide template types</a> . The user has the ultimate choice as to which format the tile uses, so it is a best practice to include a wide logo image. If a wide logo image is provided, the tile will be shown initially in its wide format. For more info about required logo dimensions, see <a href="https://msdn.microsoft.com/library/windows/apps/hh781198">Tile sizes</a>.</p>
<p>For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-uap-shownameontiles.md">uap:ShowNameOnTiles</a> </td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-tileupdate.md">uap:TileUpdate</a> </td>
<td><p>Describes how the app tile receives update notifications.</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap5-MixedRealityModel.md">uap5:MixedRealityModel</a> </td>
<td><p>An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting.</p></td>
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
<td><a href="element-uap-visualelements.md">uap:VisualElements</a> </td>
<td><p>Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For the **Wide310x150Logo**, **Square310x310Logo**, **Square71x71Logo**, and **Tall150x310Logo** images, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **ShortName** attribute. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 