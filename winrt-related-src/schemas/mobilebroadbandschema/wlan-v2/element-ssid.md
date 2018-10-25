---
Description: Contains the SSID for a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: SSID
ms.assetid: 0773526f-0046-4e2c-8972-53872dd76a83
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SSID


Contains the SSID for a WLAN.

## Element hierarchy

**&lt;SSID&gt;**

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
<td>[hex (in SSID)](element-hex.md)</td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="even">
<td>[name (in SSID)](element-name.md)</td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

Although the [**hex**](element-hex.md) and [**name**](element-name.md) elements are optional, at least one **hex** or **name** element must appear as a child of the **SSID** element. If both are present, the **hex** SSID takes precedence over the **name** SSID.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/WLAN/v2</p></td>
</tr>
</tbody>
</table>

 

 



