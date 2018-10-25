---
Description: Defines the number of entries in the Pairwise Master Key (PMK) cache on the client.
Search.Product: eADQiWindows 10XVcnh
title: PMKCacheSize
ms.assetid: b8b7c9b7-af01-484a-aeef-ff7ef2a3f728
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# PMKCacheSize


Defines the number of entries in the Pairwise Master Key (PMK) cache on the client. Must be a value between 1 and 255 inclusive.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;PMKCacheSize&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>*

## Syntax

``` syntax
<PMKCacheSize>

  integer

</PMKCacheSize>
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
<td>[security](element-security.md)</td>
<td><p>Defines various security settings for this profile on a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

**PMKCacheSize** is valid only for WPA2-defined networks with [**PMKCacheMode**](element-pmkcachemode.md) set to **enabled**. If **PMKCacheSize** is **enabled**, and this element is absent, the cache size defaults to 128 entries.

PMK caching is defined in the [802.11i specification](http://standards.ieee.org/getieee802/download/802.11i-2004.pdf).

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

 

 



