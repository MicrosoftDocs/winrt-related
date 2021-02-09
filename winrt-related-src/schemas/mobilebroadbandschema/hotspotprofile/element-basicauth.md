---
description: Contains the user name and password required for WISPr authentication.
Search.Product: eADQiWindows 10XVcnh
title: BasicAuth
ms.assetid: bd926228-8384-42ee-9a4d-2d8c6fc8ff5a

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# BasicAuth


Contains the user name and password required for WISPr authentication. Using [**BasicAuth**](element-basicauth.md) allows a static set of credentials to be used; use [**ExtAuth**](element-extauth.md) to have an app generate credentials for WISPr authentication.

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd><b>&lt;BasicAuth&gt;</b></dd>
</dl>

## Syntax

``` syntax
<BasicAuth>

  <!-- Child elements -->
  UserName,
  Password

</BasicAuth>
```

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-password.md">Password</a> </td>
<td><p>Password to be used for WISPr authentication.</p></td>
</tr>
<tr class="even">
<td><a href="element-username.md">UserName</a> </td>
<td><p>User name to be used for WISPr authentication.</p></td>
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
<td><a href="element-hotspotprofile.md">HotspotProfile</a> </td>
<td><p>Defines the properties and login credentials for a Wi-Fi hotspot. <a href="element-hotspotprofile.md"><strong>HotspotProfile</strong></a>  is the unique root element of a Wi-Fi hotspot profile that uses the Wireless Internet Service Provider roaming (WISPr) protocol.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1` |

 

 



