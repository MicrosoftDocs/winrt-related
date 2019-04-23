---
Description: Tile schema elements used to define a tile update, and specify the template, images, and text that are used to customize the tile, branding specifics, and language information.
Search.Product: eADQiWindows 10XVcnh
title: Tile schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, tiles


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-binding.md">binding</a> </td>
<td><p>Specifies the tile template. Every notification should include one binding element for each supported tile size.</p></td>
</tr>
<tr class="even">
<td><a href="element-image.md">image</a> </td>
<td><p>Specifies an image used in the tile template. The supplied image should match the size and shape requirements for the specific template or image within that template.</p></td>
</tr>
<tr class="odd">
<td><a href="element-text.md">text</a> </td>
<td><p>Specifies text used in the tile template.</p></td>
</tr>
<tr class="even">
<td><a href="element-tile.md">tile</a> </td>
<td><p>Base tile element, which contains a single <a href="https://msdn.microsoft.com/library/windows/apps/br230847"><strong>visual</strong></a>  element.</p></td>
</tr>
<tr class="odd">
<td><a href="element-visual.md">visual</a> </td>
<td><p>Contains multiple <a href="element-binding.md"><strong>binding</strong></a>  child elements, each of which defines a tile.</p></td>
</tr>
</tbody>
</table>

 

 

 



