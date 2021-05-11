---
description: Defines whether the shared key will be a network key or a pass phrase.
Search.Product: eADQiWindows 10XVcnh
title: keyType
ms.assetid: aced51e9-d51a-449f-bd7e-23e6ce5cd8ea

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# keyType


Defines whether the shared key will be a network key or a pass phrase.

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
<dd><b>&lt;keyType&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<keyType>

  "networkKey" | "passPhrase"

</keyType>
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
<td><a href="element-sharedkey.md">sharedKey</a> </td>
<td><p>Defines optional shared key information to be used by this profile to connect to a WLAN.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When the [**encryption**](element-encryption.md) element has a value of **WEP**, **keyType** must be set to **networkKey**.

See the [**keyMaterial**](element-keymaterial.md) element for more information regarding shared keys.

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WLAN/v1` |

 

 



