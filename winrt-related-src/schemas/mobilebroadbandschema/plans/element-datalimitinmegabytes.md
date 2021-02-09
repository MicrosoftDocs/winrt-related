---
description: Defines a value representing the data limit in MB for a capped plan.
Search.Product: eADQiWindows 10XVcnh
title: DataLimitInMegabytes
ms.assetid: f780b511-6b64-40f4-83a5-c9f116f65351

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DataLimitInMegabytes


Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the [**DataPlanStatus**](/uwp/api/Windows.Networking.Connectivity.DataPlanStatus) class.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-description.md">&lt;Description&gt;</a></dt>
<dd><b>&lt;DataLimitInMegabytes&gt;</b></dd>
</dl>
</dd>
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
<td><a href="element-description.md">Description</a> </td>
<td><p>Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**DataPlanStatus**](/uwp/api/Windows.Networking.Connectivity.DataPlanStatus)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/Plans/v1` |

 

 
