---
Description: Defines optional shared key information to be used by this profile to connect to a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: sharedKey
ms.assetid: e4a05934-b2a1-4237-93ab-2b1b5831906f
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# sharedKey


Defines optional shared key information to be used by this profile to connect to a WLAN.

## Element hierarchy

<dl>
<dt><a href="element-wlanprofile.md">&lt;WLANProfile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-msm.md">&lt;MSM&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-security.md">&lt;security&gt;</a></dt>
<dd><b>&lt;sharedKey&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<sharedKey>

  <!-- Child elements -->
  keyType,
  protected,
  keyMaterial,
  any element in a non-schema namespace*

</sharedKey>
```

### Key

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
<td>[keyMaterial](element-keymaterial.md)</td>
<td><p>Defines a network key or pass phrase. If [<strong>protected</strong>](element-protected.md) is <strong>true</strong>, then the key material is encrypted; otherwise, the key material is unencrypted. Encrypted key material is expressed in hexadecimal form.</p></td>
</tr>
<tr class="even">
<td>[keyType](element-keytype.md)</td>
<td><p>Defines whether the shared key will be a network key or a pass phrase.</p></td>
</tr>
<tr class="odd">
<td>[protected](element-protected.md)</td>
<td><p>If <strong>true</strong>, the shared key is encrypted. Otherwise, <strong>false</strong>.</p></td>
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
<td>[security](element-security.md)</td>
<td><p>Defines various security settings for this profile on a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This element is only required if [**authentication**](element-authentication.md) is **WEP**, or if [**encryption**](element-encryption.md) is **WPAPSK** or **WPA2PSK**.

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

 

 



