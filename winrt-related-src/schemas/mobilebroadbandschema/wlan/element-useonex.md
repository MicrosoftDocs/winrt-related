---
Description: Define if 802.1X authentication is to be used by this profile to connect to the WLAN. 
Search.Product: eADQiWindows 10XVcnh
title: useOneX
ms.assetid: c50a8dd5-460f-4f4e-bb00-392c2b39fd0e
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# useOneX


If **true**, 802.1X authentication is to be used by this profile to connect to the WLAN. Otherwise, **false**.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-authencryption.md">&lt;authEncryption&gt;</a></dt>
<dd><b>&lt;useOneX&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<useOneX>

  boolean

</useOneX>
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
<td>[authEncryption](element-authencryption.md)</td>
<td><p>Defines the authentication and encryption pair to be used for this profile on a WLAN.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/WLAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



