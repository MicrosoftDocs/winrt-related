---
Description: Defines a value representing the data limit in MB for a capped plan.
Search.Product: eADQiWindows 10XVcnh
title: DataLimitInMegabytes
ms.assetid: f780b511-6b64-40f4-83a5-c9f116f65351
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# DataLimitInMegabytes


Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd><b>&lt;DataLimitInMegabytes&gt;</b></dd>
</dl>

## Syntax

``` syntax
<DataLimitInMegabytes>

  positiveInteger

</DataLimitInMegabytes>
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
<td>[Cost](element-cost.md)</td>
<td><p>Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). [<strong>Cost</strong>](element-cost.md) is the unique root element for DUSM cost information.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/DUSM/v1</p></td>
</tr>
</tbody>
</table>

 

 



