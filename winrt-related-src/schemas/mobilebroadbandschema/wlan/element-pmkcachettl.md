---
Description: Defines the length of time, in minutes, that a Pairwise Master Key (PMK) cache will be kept.
Search.Product: eADQiWindows 10XVcnh
title: PMKCacheTTL
ms.assetid: 0c8bfb08-dda7-482f-b442-d2aaff667d00
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# PMKCacheTTL


Defines the length of time, in minutes, that a Pairwise Master Key (PMK) cache will be kept. Must be a value between 5 and 1440 inclusive.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;PMKCacheTTL&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PMKCacheTTL>

  integer

</PMKCacheTTL>
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

**PMKCacheTTL** is valid only for WPA2-defined networks with [**PMKCacheMode**](element-pmkcachemode.md) set to **enabled**. The default value is 720 minutes.

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

 

 



