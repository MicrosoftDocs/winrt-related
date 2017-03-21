---
Description: Defines the context of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: Context
ms.assetid: bb7c7c66-bd2c-40ca-87e4-c984f8c3911a
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Context


Defines the context of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.

## Element hierarchy

<dl>
<dt><a href="element-extensions-v2.md">&lt;Extensions_v2&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-additionalpdpcontexts.md">&lt;AdditionalPDPContexts&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-multiplepdpcontextpolicies.md">&lt;MultiplePDPContextPolicies&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-pdpcontextpolicy.md">&lt;PDPContextPolicy&gt;</a></dt>
<dd><b>&lt;Context&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-tetheringsettings.md">&lt;TetheringSettings&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-tetheringprofile.md">&lt;TetheringProfile&gt;</a></dt>
<dd><b>&lt;Context&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
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
<td>[AccessString](element-1-accessstring.md)</td>
<td><p>Defines the access string for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="even">
<td>[AuthProtocol](element-1-authprotocol.md)</td>
<td><p>Defines the authentication protocol to use for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="odd">
<td>[Compression](element-1-compression.md)</td>
<td><p>Defines whether compression is enabled for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="even">
<td>[UserLogonCred](element-1-userlogoncred.md)</td>
<td><p>Defines the user login credentials for a context in the Packet Data Protocol (PDP) context policy.</p></td>
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
<td>[PDPContextPolicy](element-pdpcontextpolicy.md)</td>
<td><p>Defines a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[TetheringProfile](element-tetheringprofile.md)</td>
<td><p>Defines the tethering profile in a subscriber's carrier provisioning file.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v2</p></td>
</tr>
</tbody>
</table>

 

 



