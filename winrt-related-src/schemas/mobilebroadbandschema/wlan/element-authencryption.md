---
description: Defines the authentication and encryption pair to be used for this profile on a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: authEncryption
ms.assetid: f88296a8-9de1-43ec-a610-54562f8be53e

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# authEncryption


Defines the authentication and encryption pair to be used for this profile on a WLAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;authEncryption&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<authEncryption>

  <!-- Child elements -->
  authentication,
  encryption,
  useOneX?,
  any element in a non-schema namespace*

</authEncryption>
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
<td><a href="element-authentication.md">authentication</a> </td>
<td><p>Defines the authentication method to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="even">
<td><a href="element-encryption.md">encryption</a> </td>
<td><p>Defines the type of data encryption to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="odd">
<td><a href="element-useonex.md">useOneX</a> </td>
<td><p>If <strong>true</strong>, 802.1X authentication is to be used by this profile to connect to the WLAN. Otherwise, <strong>false</strong>.</p></td>
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
<td><a href="element-security.md">security</a> </td>
<td><p>Defines various security settings for this profile on a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



