---
Description: SSID
MS-HAID: WLAN.element\_SSID
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: SSID
ms.assetid: 0773526f-0046-4e2c-8972-53872dd76a83
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# SSID


Contains the SSID for a WLAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
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
  | name
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
<td>[name (in SSID)](element-1-name.md)</td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
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
<td><p>Defines one or more service set identifiers (SSID) for a wireless LAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Although the [**hex**](element-hex.md) and [**name**](element-1-name.md) elements are optional, at least one **hex** or **name** element must appear as a child of the **SSID** element. If both are present, the **hex** SSID takes precedence over the **name** SSID.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WLAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



