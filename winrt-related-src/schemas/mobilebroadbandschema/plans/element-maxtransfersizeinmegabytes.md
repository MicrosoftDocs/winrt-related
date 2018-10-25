---
Description: Defines the size of an individual download in MB which a compliant application should permit over a metered connection without explicit user approval of the connection being used.
Search.Product: eADQiWindows 10XVcnh
title: MaxTransferSizeInMegabytes
ms.assetid: 950cd05a-2dd2-43b9-9568-fcf0e5b675c5
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MaxTransferSizeInMegabytes


Defines the size of an individual download in MB which a compliant application should permit over a metered connection without explicit user approval of the connection being used. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the [**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256) class.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-description.md">&lt;Description&gt;</a></dt>
<dd><b>&lt;MaxTransferSizeInMegabytes&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<MaxTransferSizeInMegabytes>

  positiveInteger

</MaxTransferSizeInMegabytes>
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

 

 



