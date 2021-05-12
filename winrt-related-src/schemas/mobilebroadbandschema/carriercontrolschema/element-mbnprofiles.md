---
description: Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.
Search.Product: eADQiWindows 10XVcnh
title: MBNProfiles (CarrierControlSchema schema)
ms.assetid: 10f5eab7-7e8c-4162-95e5-f1b5b793e0d8

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MBNProfiles (CarrierControlSchema schema)


Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd><b>&lt;MBNProfiles&gt;</b></dd>
</dl>

## Syntax

``` syntax
<MBNProfiles>

  <!-- Child elements -->
  DefaultProfile?,
  PurchaseProfile?,
  Messages?,
  Branding?

</MBNProfiles>
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
<td><a href="element-branding.md">Branding</a> </td>
<td><p>Defines an instance of the <a href="/uwp/schemas/mobilebroadbandschema/wwan/element-branding"><strong>Branding</strong></a>  element from the <a href="/uwp/schemas/mobilebroadbandschema/wwan/schema-root"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="even">
<td><a href="element-defaultprofile.md">DefaultProfile</a> </td>
<td><p>Defines an instance of the <a href="/uwp/schemas/mobilebroadbandschema/wwan/element-defaultprofile"><strong>DefaultProfile</strong></a>  element from the <a href="/uwp/schemas/mobilebroadbandschema/wwan/schema-root"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="odd">
<td><a href="element-messages.md">Messages</a> </td>
<td><p>Defines an instance of the <a href="/uwp/schemas/mobilebroadbandschema/wwan/element-messages"><strong>Messages</strong></a>  element from the <a href="/uwp/schemas/mobilebroadbandschema/wwan/schema-root"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="even">
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Defines an instance of the <a href="/uwp/schemas/mobilebroadbandschema/wwan/element-purchaseprofile"><strong>PurchaseProfile</strong></a>  element from the <a href="/uwp/schemas/mobilebroadbandschema/wwan/schema-root"><strong>WWAN</strong></a> schema.</p></td>
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
<td><a href="element-carrierprovisioning.md">CarrierProvisioning</a> </td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. <a href="element-carrierprovisioning.md"><strong>CarrierProvisioning</strong></a>  is the unique root element of the provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 
