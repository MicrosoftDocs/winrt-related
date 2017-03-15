---
Description: SSID
MS-HAID: HotSpotProfile.element\_SSID
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: SSID
ms.assetid: 0773526f-0046-4e2c-8972-53872dd76a83
author: mcleblanc
ms.author: markl
keywords: windows 10
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
<td>[hex](element-hex.md)</td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="even">
<td>[hexPrefix](element-hexprefix.md)</td>
<td><p>Defines a class of wireless LANs whose SSIDs begin with the bytes provided.</p></td>
</tr>
<tr class="odd">
<td>[name](element-name.md)</td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
</tr>
<tr class="even">
<td>[namePrefix](element-nameprefix.md)</td>
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
<td>[SSIDConfig](element-ssidconfig.md)</td>
<td><p>Contains a set of additional SSIDs that are handled by this profile to reduce the number of SSIDs in the WLAN profile store. Windows will not connect to these SSIDs until a user manually connects once. The newly-created profile will inherit the HotspotAuth settings from this profile.</p></td>
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

 

 



