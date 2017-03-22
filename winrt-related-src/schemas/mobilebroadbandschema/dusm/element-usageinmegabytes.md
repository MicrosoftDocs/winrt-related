---
Description: Defines a value representing the data used to-date within the current billing cycle in MB. 
Search.Product: eADQiWindows 10XVcnh
title: UsageInMegabytes
ms.assetid: 761f569a-22cb-499d-9174-c871ace98031
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# UsageInMegabytes


Defines a value representing the data used to-date within the current billing cycle in MB. Must be a value from 0 to 2<sup>32nd</sup>.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd><b>&lt;UsageInMegabytes&gt;</b></dd>
</dl>

## Syntax

``` syntax
<UsageInMegabytes Timestamp = dateTime >

  nonNegativeInteger

</UsageInMegabytes>
```

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Timestamp</strong></td>
<td><p>A value representing the date and time in UTC the data usage profile data was last updated by the MNO.</p></td>
<td>dateTime</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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

 

 



