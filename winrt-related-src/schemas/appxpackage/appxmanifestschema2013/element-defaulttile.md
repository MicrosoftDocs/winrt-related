---
Description: The default tile that represents the app on the Start screen. 
Search.Product: eADQiWindows 10XVcnh
title: DefaultTile
ms.assetid: 262b48ae-ca25-4fed-adad-df1bb8924c9d
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# DefaultTile




The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd><b>&lt;DefaultTile&gt;</b></dd>
</dl>

## Syntax

``` syntax
<DefaultTile Wide310x150Logo?   = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
             Square310x310Logo? = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
             Square70x70Logo?   = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
             ShortName?         = A string between 1 and 40 characters in length.
             DefaultSize?       = "square150x150Logo" | "wide310x150Logo" >

  <!-- Child elements -->
  ( TileUpdate?
  & ShowNameOnTiles?
  )

</DefaultTile>
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
<td><strong>DefaultSize</strong></td>
<td><p>The default size of the logo image. This value is ignored on Windows Phone 8.1.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>square150x150Logo</li>
<li>wide310x150Logo</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ShortName</strong></td>
<td><p>A short name for the app that is displayed directly on the tile. This string is localizable; for more info, see Remarks.</p>
<div class="alert">
<strong>Note</strong>  As of Windows 8.1, this property is ignored and the display name declared in the manifest is used in its place.
</div>
<div>
 
</div></td>
<td>A string between 1 and 40 characters in length.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Square310x310Logo</strong></td>
<td><p>The 310x310 square version of the logo image.</p>
<p>For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Square70x70Logo</strong></td>
<td><p>The 70x70 square version of the logo image.</p>
<p>For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
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
<td><a href="element-shownameontiles.md">ShowNameOnTiles</a> </td>
<td><p>Describes whether Windows overlays the app’s name on top of the tile images that are shown on the Start screen.</p></td>
</tr>
<tr class="even">
<td><a href="element-tileupdate.md">TileUpdate</a> </td>
<td><p>Describes how the app tile receives update notifications.</p></td>
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
<td><a href="element-visualelements.md">VisualElements</a> </td>
<td><p>Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

**Wide310x150Logo**, **Square310x310Logo**, and **Square70x70Logo** images can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply localized images to match different UI languages. This feature also allows you to localize the **ShortName** attribute. For more info, see the [Globalization](https://msdn.microsoft.com/library/windows/apps/hh831183) topic.

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

 

 



