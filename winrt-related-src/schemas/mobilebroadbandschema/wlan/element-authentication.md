---
Description: Defines the authentication method to be used by this profile to connect to a WLAN.
Search.Product: eADQiWindows 10XVcnh
title: authentication
ms.assetid: 34e5552a-98b3-4b2c-8dde-dce34578bc9a

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# authentication


Defines the authentication method to be used by this profile to connect to a WLAN.

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
<dd><b>&lt;authentication&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<authentication>

  "open" | "shared" | "WPA" | "WPAPSK" | "WPA2" | "WPA2PSK"

</authentication>
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

| Value   | Description                            |
|---------|----------------------------------------|
| open    | Open 802.11 authentication.            |
| shared  | Shared 802.11 authentication.          |
| WPA     | WPA-Enterprise 802.11 authentication.  |
| WPAPSK  | WPA-Personal 802.11 authentication.    |
| WPA2    | WPA2-Enterprise 802.11 authentication. |
| WPA2PSK | WPA2-Personal 802.11 authentication.   |

 

For more information about 802.11 authentication methods, see the [WPA](https://go.microsoft.com/fwlink/p/?linkid=391356), [802.1X](https://go.microsoft.com/fwlink/p/?linkid=89910), and [802.11i](https://go.microsoft.com/fwlink/p/?linkid=89906) specifications.

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

 

 



