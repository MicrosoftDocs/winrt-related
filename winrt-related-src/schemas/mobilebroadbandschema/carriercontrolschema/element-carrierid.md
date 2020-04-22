---
Description: Defines a unique GUID that identifies the Mobile Network Operator (MNO). 
Search.Product: eADQiWindows 10XVcnh
title: CarrierId
ms.assetid: 60cee169-cd12-41c1-9f2f-70236dced515

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierId


Defines a unique GUID that identifies the Mobile Network Operator (MNO). If the MNO participates in MBAE, this should be their MBAE Carrier ID. Non-MBAE MNOs may generate a GUID as part of their initial configuration.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-global.md">&lt;Global&gt;</a></dt>
<dd><b>&lt;CarrierId&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<CarrierId>

  GUID

</CarrierId>
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
<td><a href="element-global.md">Global</a> </td>
<td><p>Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 



