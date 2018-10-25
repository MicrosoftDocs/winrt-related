---
Description: Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.
Search.Product: eADQiWindows 10XVcnh
title: MBNProfiles
ms.assetid: 10f5eab7-7e8c-4162-95e5-f1b5b793e0d8
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MBNProfiles


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
<td>[Branding](element-branding.md)</td>
<td><p>Defines an instance of the [<strong>Branding</strong>](https://msdn.microsoft.com/library/windows/apps/hh868446) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="even">
<td>[DefaultProfile](element-defaultprofile.md)</td>
<td><p>Defines an instance of the [<strong>DefaultProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868453) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="odd">
<td>[Messages](element-messages.md)</td>
<td><p>Defines an instance of the [<strong>Messages</strong>](https://msdn.microsoft.com/library/windows/apps/hh868462) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="even">
<td>[PurchaseProfile](element-purchaseprofile.md)</td>
<td><p>Defines an instance of the [<strong>PurchaseProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868470) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
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
<td>[CarrierProvisioning](element-carrierprovisioning.md)</td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. [<strong>CarrierProvisioning</strong>](element-carrierprovisioning.md) is the unique root element of the provisioning file.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v1</p></td>
</tr>
</tbody>
</table>

 

 



