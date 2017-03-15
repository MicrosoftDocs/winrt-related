---
Description: Tile schema
MS-HAID: tile.Schema\_Root
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Tile schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# Tile schema


These elements are used to define a tile update, and specify the template, images, and text that are used to customize the tile, branding specifics, and language information.

These elements and their attributes are manipulated through Document Object Model (DOM) functions to customize the tile content.

To define the initial content for a non-default tile, use [**TileUpdateManager.getTemplateContent**](https://msdn.microsoft.com/library/windows/apps/br208627) to get template content that can be modified.

To define the content for an update to an existing non-default tile, you can use [**TileNotification.content**](https://msdn.microsoft.com/library/windows/apps/br208617) to get the existing tile content that can then be modified.

These elements can also be assigned through use of the [NotificationsExtensions](https://msdn.microsoft.com/library/windows/apps/hh969156) library helper functions.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[binding](element-binding.md)</td>
<td><p>Specifies the tile template. Every notification should include one binding element for each supported tile size.</p></td>
</tr>
<tr class="even">
<td>[image](element-image.md)</td>
<td><p>Specifies an image used in the tile template. The supplied image should match the size and shape requirements for the specific template or image within that template.</p></td>
</tr>
<tr class="odd">
<td>[text](element-text.md)</td>
<td><p>Specifies text used in the tile template.</p></td>
</tr>
<tr class="even">
<td>[tile](element-tile.md)</td>
<td><p>Base tile element, which contains a single [<strong>visual</strong>](https://msdn.microsoft.com/library/windows/apps/br230847) element.</p></td>
</tr>
<tr class="odd">
<td>[visual](element-visual.md)</td>
<td><p>Contains multiple [<strong>binding</strong>](element-binding.md) child elements, each of which defines a tile.</p></td>
</tr>
</tbody>
</table>

 

 

 



