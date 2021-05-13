---
description: Contains the SSID for a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: SSID (WLAN schema)
ms.assetid: 0773526f-0046-4e2c-8972-53872dd76a83

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SSID (WLAN schema)


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
<td><a href="element-hex.md">hex</a> </td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-name.md">name (in SSID)</a> </td>
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
<td><a href="element-ssidconfig.md">SSIDConfig</a> </td>
<td><p>Defines one or more service set identifiers (SSID) for a wireless LAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Although the [**hex**](element-hex.md) and [**name**](element-1-name.md) elements are optional, at least one **hex** or **name** element must appear as a child of the **SSID** element. If both are present, the **hex** SSID takes precedence over the **name** SSID.

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



