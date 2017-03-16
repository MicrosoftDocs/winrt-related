---
Description: PMKCacheMode
MS-HAID: WLAN.element\_PMKCacheMode
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: PMKCacheMode
ms.assetid: 3bfb39c1-8bc1-4eec-b954-7b6ba7a95d24
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# PMKCacheMode


Defines whether Pairwise Master Key (PMK) caching is to be used by this profile to connect to a WLAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;PMKCacheMode&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PMKCacheMode>

  string

</PMKCacheMode>
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

For WPA2-defined networks, **PMKCacheMode** is **enabled**. Otherwise, **disabled**.

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

 

 



