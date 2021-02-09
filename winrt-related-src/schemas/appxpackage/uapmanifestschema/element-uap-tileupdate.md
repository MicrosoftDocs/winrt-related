---
description: Describes how the app tile receives update notifications.
Search.Product: eADQiWindows 10XVcnh
title: uap:TileUpdate (Windows 10)
ms.assetid: cf529081-b711-4c35-b50c-da0f95ebf3c1


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:TileUpdate (Windows 10)


Describes how the app tile receives update notifications.

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
<dd><b>&lt;uap:TileUpdate&gt;</b></dd>
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
<td><a href="element-uap-defaulttile.md">uap:DefaultTile</a> </td>
<td><p>The default tile that represents the app on the Start screen. This tile is displayed when the app is first installed, before it has received any update notifications. When a tile has no notifications to show, the tile reverts to this default.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **UriTemplate** attribute must be a value URI per RFC 3986. It must be an absolute URI with only [schemes](/windows/uwp/launch-resume/launch-maps-app) of unsecure "http:" sites and secure "https:" sites permitted.

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 
