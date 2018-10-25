---
Description: Defines a unique device identifier to which this provisioning attempt applies.
Search.Product: eADQiWindows 10XVcnh
title: DeviceId
ms.assetid: b7140563-a2c9-499a-aec3-464b2c4e5518
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DeviceId

Defines a unique device identifier to which this provisioning attempt applies. It must be formatted as **\\d{15,16}** or as **(\[a-fA-F0-9\]{2}:){5}\[a-fA-F0-9\]{2}**

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-global.md">&lt;Global&gt;</a></dt>
<dd><b>&lt;DeviceId&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DeviceId>

  token

</DeviceId>
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
<td>[Global](element-global.md)</td>
<td><p>Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.</p></td>
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

 

 



