---
Description: InboundBandwidthInKbps
MS-HAID: Plans.element\_InboundBandwidthInKbps
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: InboundBandwidthInKbps
ms.assetid: fbe04013-daa0-463a-a03f-3db7697717c1
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# InboundBandwidthInKbps


Defines a value representing the effective link speed of the subscriber’s inbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256) class.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-description.md">&lt;Description&gt;</a></dt>
<dd><b>&lt;InboundBandwidthInKbps&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<InboundBandwidthInKbps>

  nonNegativeInteger

</InboundBandwidthInKbps>
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
<td>[Description](element-description.md)</td>
<td><p>Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/CarrierControl/Plans/v1</p></td>
</tr>
</tbody>
</table>

 

 



