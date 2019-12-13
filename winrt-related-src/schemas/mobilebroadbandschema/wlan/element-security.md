---
Description: Defines various security settings for this profile on a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: security
ms.assetid: 4e3338c2-345b-45a5-b3cf-c23b71531a1c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# security


Defines various security settings for this profile on a WLAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd><b>&lt;security&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<security>

  <!-- Child elements -->
  authEncryption,
  sharedKey?,
  keyIndex?,
  PMKCacheMode?,
  PMKCacheTTL?,
  PMKCacheSize?,
  preAuthMode?,
  preAuthThrottle?,
  any element in a non-schema namespace*

</security>
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
<td><a href="element-pmkcachemode.md">PMKCacheMode</a> </td>
<td><p>Defines whether Pairwise Master Key (PMK) caching is to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="even">
<td><a href="element-pmkcachesize.md">PMKCacheSize</a> </td>
<td><p>Defines the number of entries in the Pairwise Master Key (PMK) cache on the client. Must be a value between 1 and 255 inclusive.</p></td>
</tr>
<tr class="odd">
<td><a href="element-pmkcachettl.md">PMKCacheTTL</a> </td>
<td><p>Defines the length of time, in minutes, that a Pairwise Master Key (PMK) cache will be kept. Must be a value between 5 and 1440 inclusive.</p></td>
</tr>
<tr class="even">
<td><a href="element-authencryption.md">authEncryption</a> </td>
<td><p>Defines the authentication and encryption pair to be used for this profile on a WLAN.</p></td>
</tr>
<tr class="odd">
<td><a href="element-keyindex.md">keyIndex</a> </td>
<td><p>Defines which key index should be used to encrypt wireless traffic. <a href="element-keyindex.md"><strong>keyIndex</strong></a>  is only used when <a href="element-keytype.md"><strong>keyType</strong></a> is <strong>networkKey</strong>. The default value is 0 when <a href="element-sharedkey.md"><strong>sharedKey</strong></a> is present. Must be a value between 0 and 3 inclusive.</p></td>
</tr>
<tr class="even">
<td><a href="element-preauthmode.md">preAuthMode</a> </td>
<td><p>Defines whether pre-authentication will be used by the client.</p></td>
</tr>
<tr class="odd">
<td><a href="element-preauththrottle.md">preAuthThrottle</a> </td>
<td><p>Defines the number of pre-authentication attempts to try on neighboring access points (AP). Must be a value between 1 and 16 inclusive.</p></td>
</tr>
<tr class="even">
<td><a href="element-sharedkey.md">sharedKey</a> </td>
<td><p>Defines optional shared key information to be used by this profile to connect to a WLAN.</p></td>
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
<td><a href="element-msm.md">MSM</a> </td>
<td><p>Defines various media-specific module (MSM) settings for this profile on a WLAN.</p></td>
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

 

 



