---
Description: Describes how the app tile receives update notifications.
Search.Product: eADQiWindows 10XVcnh
title: TileUpdate
ms.assetid: 2f97e602-d999-455b-907e-83558991c614
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# TileUpdate

Describes how the app tile receives update notifications.

## Element hierarchy

<dl>
<dt><a href="element-visualelements.md">&lt;VisualElements&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-defaulttile.md">&lt;DefaultTile&gt;</a></dt>
<dd><b>&lt;TileUpdate&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TileUpdate Recurrence  = "halfHour" | "hour" | "sixHours" | "twelveHours" | "daily"
            UriTemplate = A string between 1 and 2084 characters in length. />
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
<td><strong>Recurrence</strong></td>
<td><p>The recurrence interval for tile update notifications.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>halfHour</li>
<li>hour</li>
<li>sixHours</li>
<li>twelveHours</li>
<li>daily</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>UriTemplate</strong></td>
<td><p>The URI template for tile update notifications.</p></td>
<td>A string between 1 and 2084 characters in length.</td>
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
<td><a href="element-defaulttile.md">DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **UriTemplate** attribute must be a value URI per RFC 3986. It must be an absolute URI with only [schemes](https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-maps-app) of unsecure "http:" sites and secure "https:" sites permitted.

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

 

 



