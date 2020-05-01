---
Description: Defines whether pre-authentication will be used by the client.
Search.Product: eADQiWindows 10XVcnh
title: preAuthMode
ms.assetid: 4ec7ff00-a0b8-453b-9b7b-80782a116900

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# preAuthMode


Defines whether pre-authentication will be used by the client.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;preAuthMode&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<preAuthMode>

  string

</preAuthMode>
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

Pre-authentication is necessary for WPA2 secure fast roaming. **preAuthMode** is valid only for WPA2-defined networks with [**PMKCacheMode**](element-pmkcachemode.md) set to **enabled**. If **preAuthMode** is **enabled**, and this element is absent, the default value is **enabled**.

PMK caching is defined in the [802.11i specification](https://standards.ieee.org/getieee802/download/802.11i-2004.pdf).

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



