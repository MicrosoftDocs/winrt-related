---
description: Contains a set of additional SSIDs that are handled by this profile to reduce the number of SSIDs in the WLAN profile store.
Search.Product: eADQiWindows 10XVcnh
title: SSIDConfig (HotspotProfile schema)
ms.assetid: a58e4178-4a15-46c0-951d-93aef9fec5e6

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SSIDConfig (HotspotProfile schema)


Contains a set of additional SSIDs that are handled by this profile to reduce the number of SSIDs in the WLAN profile store. Windows will not connect to these SSIDs until a user manually connects once. The newly-created profile will inherit the HotspotAuth settings from this profile.

## Element hierarchy

<dl>
<dt><a href="element-hotspotprofile.md">&lt;HotspotProfile&gt;</a></dt>
<dd><b>&lt;SSIDConfig&gt;</b></dd>
</dl>

## Syntax

``` syntax
<SSIDConfig>

  <!-- Child elements -->
  SSID{1,250}

</SSIDConfig>
```

### Key

`{}`   specific range of occurrences
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
<td><a href="element-ssid.md">SSID</a> </td>
<td><p>An additional SSID handled by this profile.</p></td>
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

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/WLAN/HotspotProfile/v1` |

 

 



