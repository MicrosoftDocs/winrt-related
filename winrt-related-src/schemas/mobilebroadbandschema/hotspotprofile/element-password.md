---
Description: Password to be used for WISPr authentication.
Search.Product: eADQiWindows 10XVcnh
title: Password
ms.assetid: a7a63a7c-31d7-42bb-8e04-557306980baf

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Password


Password to be used for WISPr authentication.

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-basicauth.md">&lt;BasicAuth&gt;</a></dt>
<dd><b>&lt;Password&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Password>

  token

</Password>
```

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-basicauth.md">BasicAuth</a> </td>
<td><p>Contains the user name and password required for WISPr authentication. Using <a href="element-basicauth.md"><strong>BasicAuth</strong></a>  allows a static set of credentials to be used; use <a href="element-extauth.md"><strong>ExtAuth</strong></a> to have an app generate credentials for WISPr authentication.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/WLAN/HotspotProfile/v1</p></td>
</tr>
</tbody>
</table>

 

 



