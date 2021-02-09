---
description: Defines the number of pre-authentication attempts to try on neighboring access points (AP).
Search.Product: eADQiWindows 10XVcnh
title: preAuthThrottle
ms.assetid: f0836b86-12da-4329-a190-5c8d5132e145

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# preAuthThrottle


Defines the number of pre-authentication attempts to try on neighboring access points (AP). Must be a value between 1 and 16 inclusive.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;preAuthThrottle&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<preAuthThrottle>

  integer

</preAuthThrottle>
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
<td><a href="element-security.md">security</a> </td>
<td><p>Defines various security settings for this profile on a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

**preAuthThrottle** is valid only for WPA2-defined networks with [**PMKCacheMode**](element-pmkcachemode.md) set to **enabled**. If **preAuthThrottle** is **enabled**, and this element is absent, the number defaults to 3.

PMK caching is defined in the [802.11i specification](https://standards.ieee.org/getieee802/download/802.11i-2004.pdf).

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



