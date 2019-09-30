---
Description: Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.
Search.Product: eADQiWindows 10XVcnh
title: LockScreen
ms.assetid: 4b73231f-9cf8-4dc6-ad82-70dc2bdb7745
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# LockScreen


Defines the badge and notifications that represent the app on the lock screen, which is shown when the system is locked.

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
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd><b>&lt;LockScreen&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<LockScreen Notification = "badge" | "badgeAndTileText"
            BadgeLogo    = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, %, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both. />
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
<td><strong>BadgeLogo</strong></td>
<td><p>A logo image that is shown next to the badge to identify the app. This image must be monochromatic, of type .png, and measure 24 x 24 pixels.</p></td>
<td>A string between 1 and 256 characters in length that ends with &quot;.jpg&quot;, &quot;.png&quot;, or &quot;.jpeg&quot; that can't contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Notification</strong></td>
<td><p>The type of tile that can be shown for an app on the lock screen. This can either be simply a badge which displays either a number or a glyph to communicate status, or both a badge and text, which can display detailed status. If LockScreen Notification type 'badgeAndTileText' is selected, then the optional WideLogo must be specified, since only the WideLogo template provides the right information to display with tile text. If this image is not provided, the tile can only display in the square format and cannot accept notifications based on <a href="https://msdn.microsoft.com/library/windows/apps/hh761491">wide template types</a> . This rule is semantically enforced through the manifest API.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>badge</li>
<li>badgeAndTileText</li>
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
<td><a href="element-visualelements.md">VisualElements</a> </td>
<td><p>Describes the visual aspects of the UWP app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

For an app to have a presence on the lock screen, it must also register to handle background tasks. For more information, see the [Lock screen overview](https://msdn.microsoft.com/library/windows/apps/hh779720) and the [**BackgroundTasks**](element-backgroundtasks.md) element.

The **BadgeLogo** image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](https://msdn.microsoft.com/library/windows/apps/hh831183) topic.

Size requirements of a badge logo image are shown here:

Image attribute
Scale
Image size in pixels
Applications\\Application\\VisualElements\\LockScreen\\@BadgeLogo
100
24x24
140
33x33
180
43x43
 

## See also


[Lock screen overview](https://msdn.microsoft.com/library/windows/apps/br241847)

[How to show notifications on the lock screen](https://msdn.microsoft.com/library/windows/apps/hh700416)

[Lock screen apps sample](https://go.microsoft.com/fwlink/p/?linkid=239970)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



