---
Description: Global
MS-HAID: CarrierControlSchema.element\_Global
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Global
ms.assetid: e6dd93a0-2535-4df3-8f3e-32186e7ce122
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Global


Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd><b>&lt;Global&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Global>

  <!-- Child elements -->
  CarrierId,
  SubscriberId,
  DeviceId?,
  any element in a non-schema namespace*

</Global>
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
<td>[CarrierId](element-carrierid.md)</td>
<td><p>Defines a unique GUID that identifies the Mobile Network Operator (MNO). If the MNO participates in MBAE, this should be their MBAE Carrier ID. Non-MBAE MNOs may generate a GUID as part of their initial configuration.</p></td>
</tr>
<tr class="even">
<td>[DeviceId](element-deviceid.md)</td>
<td><p>Defines a unique device identifier to which this provisioning attempt applies. It must be formatted as <strong>\d{15,16}</strong> or as <strong>([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}</strong></p></td>
</tr>
<tr class="odd">
<td>[SubscriberId](element-subscriberid.md)</td>
<td><p>Defines a unique subscriber account identifier to which this provisioning attempt applies.</p></td>
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

 

 



