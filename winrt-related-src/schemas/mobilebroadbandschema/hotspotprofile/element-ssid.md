---
description: An additional SSID handled by this profile.
Search.Product: eADQiWindows 10XVcnh
title: SSID
ms.assetid: 0773526f-0046-4e2c-8972-53872dd76a83

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SSID


An additional SSID handled by this profile.

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-ssidconfig.md">&lt;SSIDConfig&gt;</a></dt>
<dd><b>&lt;SSID&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<SSID>

  <!-- Child elements -->
  ( hex
  | hexPrefix
  | name
  | namePrefix
  )

</SSID>
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
<td><a href="element-hex.md">hex</a> </td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="even">
<td><a href="element-hexprefix.md">hexPrefix</a> </td>
<td><p>Defines a class of wireless LANs whose SSIDs begin with the bytes provided.</p></td>
</tr>
<tr class="odd">
<td><a href="element-name.md">name</a> </td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
</tr>
<tr class="even">
<td><a href="element-nameprefix.md">namePrefix</a> </td>
<td><p>Defines a class of wireless LANs whose SSIDs begin with the characters provided.</p></td>
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
<td><a href="element-ssidconfig.md">SSIDConfig</a> </td>
<td><p>Contains a set of additional SSIDs that are handled by this profile to reduce the number of SSIDs in the WLAN profile store. Windows will not connect to these SSIDs until a user manually connects once. The newly-created profile will inherit the HotspotAuth settings from this profile.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1` |

 

 



