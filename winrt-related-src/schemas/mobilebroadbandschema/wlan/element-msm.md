---
Description: Defines various media-specific module (MSM) settings for this profile on a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: MSM
ms.assetid: 2ba7013a-b9fd-4b38-bd62-c6c3db8f5362

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MSM


Defines various media-specific module (MSM) settings for this profile on a WLAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd><b>&lt;MSM&gt;</b></dd>
</dl>

## Syntax

``` syntax
<MSM>

  <!-- Child elements -->
  security?,
  any element in a non-schema namespace*

</MSM>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td><a href="element-security.md">security</a> </td>
<td><p>Defines various security settings for this profile on a WLAN.</p></td>
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
<td><a href="element-wlanprofile.md">WLANProfile</a> </td>
<td><p>Defines the properties and security settings of a subscriber's WLAN connection profile. <a href="element-wlanprofile.md"><strong>WLANProfile</strong></a>  is the unique root element of a wireless profile.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



