---
Description: Defines a network key or pass phrase. 
Search.Product: eADQiWindows 10XVcnh
title: keyMaterial
ms.assetid: 9079ea77-b72a-43fc-afca-871d9533186b
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# keyMaterial


Defines a network key or pass phrase. If [**protected**](element-protected.md) is **true**, then the key material is encrypted; otherwise, the key material is unencrypted. Encrypted key material is expressed in hexadecimal form.

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
<dt><a href="element-sharedkey.md">&lt;sharedKey&gt;</a></dt>
<dd><b>&lt;keyMaterial&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<keyMaterial>

  string

</keyMaterial>
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
<td>[sharedKey](element-sharedkey.md)</td>
<td><p>Defines optional shared key information to be used by this profile to connect to a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The range of valid values for the **keyMaterial** element varies by the type of authentication and encryption used, as specified by the [**authentication**](element-authentication.md) and [**encryption**](element-encryption.md) elements. It also varies by [**keyType**](element-keytype.md).

The following table shows valid **keyMaterial** values for some authentication and encryption pairs:

| [**authentication**](element-authentication.md) value | [**encryption**](element-encryption.md) value | [**keyType**](element-keytype.md) value | Valid keyMaterial values                                                                                                                                                                        |
|--------------------------------------------------------|------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| open or shared                                         | WEP                                            | networkKey                               | This element contains a WEP key of 5 or 13 ANSI characters, or of 10 or 26 hexadecimal characters.                                                                                              |
| WPAPSK or WPA2PSK                                      | TKIP or AES                                    | passPhrase                               | This element contains a pass phrase of 8 to 63 ASCII characters, that is, 8 to 63 ANSI characters in the range of 32 to 126. Key values must comply with the requirements specified by 802.11i. |
| WPAPSK or WPA2PSK                                      | TKIP or AES                                    | networkKey                               | This element contains a key of 64 hexadecimal characters.                                                                                                                                       |

 

Unicode characters may be entered where ANSI or ASCII characters are specified above. However, if the supplied Unicode characters cannot be mapped to ANSI or ASCII characters, then the supplied key material is rejected.

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

 

 



