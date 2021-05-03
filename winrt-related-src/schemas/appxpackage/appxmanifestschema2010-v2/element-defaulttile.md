---
description: The default tile that represents the app on the Start screen.
Search.Product: eADQiWindows 10XVcnh
title: DefaultTile (extensions schema for Windows 8.1)
ms.assetid: 262b48ae-ca25-4fed-adad-df1bb8924c9d


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# DefaultTile (extensions schema for Windows 8.1)




The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd><b>&lt;DefaultTile&gt;</b></dd>
</dl>

## Syntax

``` syntax
<DefaultTile WideLogo?  = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
             ShortName? = A string between 1 and 40 characters in length.
             ShowName?  = "allLogos" | "noLogos" | "logoOnly" | "wideLogoOnly" />
```

### Key

`?`   optional (zero or one)

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
<td><p>A short name for the app that is displayed directly on the tile. This string is localizable; see Remarks for details.</p>
<div class="alert">
<strong>Note</strong>  As of Windows 8.1, this property is ignored and the display name declared in the manifest is used in its place.
</div>
<div>
 
</div></td>
<td>A string between 1 and 40 characters in length.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ShowName</strong></td>
<td><p>The tile sizes, as expressed by their logo size, that should display the app's display name.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>allLogos</li>
<li>noLogos</li>
<li>logoOnly</li>
<li>wideLogoOnly</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>WideLogo</strong></td>
<td><p>A wide version of the logo image. This image is displayed when the tile is displayed in its wide format. If this image is not provided, the tile can only display in the square format and cannot accept notifications based on <a href="/previous-versions/windows/apps/hh761491(v=win.10)">wide template types</a> . The user has the ultimate choice as to which format the tile uses, so it is a best practice to include a wide logo image. If a wide logo image is provided, the tile will be shown initially in its wide format. For more info about required logo dimensions, see <a href="/previous-versions/windows/apps/hh781198(v=win.10)">Tile sizes</a>.</p>
<p>For more info about how to specify the image in this attribute, see Remarks.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>No</td>
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
<td><a href="element-visualelements.md">VisualElements</a> </td>
<td><p>Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For more info on tile dimension requirements, see [Tile sizes](/previous-versions/windows/apps/hh781198(v=win.10)).

**WideLogo** image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. This feature also allows you to localize the **ShortName** attribute. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

Size requirements of a wide logo image are shown here:

Image attribute
Scale
Image size in pixels
Applications\\Application\\VisualElements\\DefaultTile\\@WideLogo
100
310x150
140
434x210
180
558x270
 

## See also


[Quickstart: Creating a default tile using the Visual Studio manifest editor](/previous-versions/windows/apps/hh465437(v=win.10))

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
