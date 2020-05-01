---
Description: Defines a value representing the effective link speed of the subscriber’s outbound connection specified in Kbps. 
Search.Product: eADQiWindows 10XVcnh
title: OutboundBandwidthInKbps
ms.assetid: 28dc6113-16f2-413d-9c69-8330395f03ee

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# OutboundBandwidthInKbps


Defines a value representing the effective link speed of the subscriber’s outbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the [**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256) class.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-description.md">&lt;Description&gt;</a></dt>
<dd><b>&lt;OutboundBandwidthInKbps&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<OutboundBandwidthInKbps>

  nonNegativeInteger

</OutboundBandwidthInKbps>
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
<td><a href="element-description.md">Description</a> </td>
<td><p>Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/Plans/v1` |

 

 



