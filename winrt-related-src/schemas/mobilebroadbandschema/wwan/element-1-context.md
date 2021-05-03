---
description: Defines the parameters required to setup a data connection.
Search.Product: eADQiWindows 10XVcnh
title: Context (WWAN schema, child of PurchaseProfile)
ms.assetid: bb7c7c66-bd2c-40ca-87e4-c984f8c3911a

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Context (WWAN schema, child of PurchaseProfile)


Defines the parameters required to setup a data connection.

## Element hierarchy

<dl>
<dt><a href="element-purchaseprofile.md">&lt;PurchaseProfile&gt;</a></dt>
<dd><b>&lt;Context&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Context>

  <!-- Child elements -->
  AccessString?,
  UserLogonCred?,
  Compression?,
  AuthProtocol?

</Context>
```

### Key

`?`   optional (zero or one)

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
<td><a href="element-1-accessstring.md">AccessString</a> </td>
<td><p>Defines the Access Point Name (APN) or dial string to be used to establish a data connection. Must be less than 100 characters.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-authprotocol.md">AuthProtocol</a> </td>
<td><p>Defines the authentication protocol to be used for activating a Packet Data Protocol (PDP) context:</p>
<p></p>
<ul>
<li><strong>NONE</strong> - No authentication protocol.</li>
<li><strong>PAP</strong> - Unencrypted password authentication.</li>
<li><strong>CHAP</strong> - Challenge Handshake Authentication Protocol(CHAP).</li>
<li><strong>MsCHAPv2</strong> - Microsoft’s Challenge Handshake Authentication Protocol(CHAP) v2.0.</li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="element-1-compression.md">Compression</a> </td>
<td><p>If <strong>ENABLE</strong>, the packet header and data transferred over the connection is compressed. Otherwise, <strong>DISABLE</strong>.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-userlogoncred.md">UserLogonCred</a> </td>
<td><p>Defines logon credentials for a connection.</p></td>
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
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Defines a purchase connection profile used by a subscriber to connect to a MNO.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



