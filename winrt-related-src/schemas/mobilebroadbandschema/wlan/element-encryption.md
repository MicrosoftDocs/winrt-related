---
description: Defines the type of data encryption to be used by this profile to connect to a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: encryption
ms.assetid: 9d00087e-32e9-49ae-8bf6-b4c62819e800

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# encryption


Defines the type of data encryption to be used by this profile to connect to a WLAN.

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
<dd><b>&lt;encryption&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<encryption>

  "none" | "WEP" | "TKIP" | "AES"

</encryption>
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
<td><a href="element-authencryption.md">authEncryption</a> </td>
<td><p>Defines the authentication and encryption pair to be used for this profile on a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

| Value | Description                     |
|-------|---------------------------------|
| none  | No encryption.                  |
| WEP   | Wired Equivalent Privacy        |
| TKIP  | Temporal Key Integrity Protocol |
| AES   | Advanced Encryption Standard    |

 

When the **encryption** element has a value of **WEP**, [**keyType**](element-keytype.md) must be set to **networkKey**.

For more information about encryption methods, see the [WEP](https://ieeexplore.ieee.org/servlet/opac?punumber=5258), [TKIP](https://standards.ieee.org/getieee802/download/802.11i-2004.pdf), and [AES](https://csrc.nist.gov/publications/fips/fips197/fips-197.pdf) specifications.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



