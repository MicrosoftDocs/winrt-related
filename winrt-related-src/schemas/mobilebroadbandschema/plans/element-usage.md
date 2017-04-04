---
Description: Defines the state of a subscriber's data usage on a connection to a Mobile Network Operator (MNO). 
Search.Product: eADQiWindows 10XVcnh
title: Usage
ms.assetid: 82d451f6-18be-4455-b62a-61296a8f8ad0
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Usage


Defines the state of a subscriber's data usage on a connection to a Mobile Network Operator (MNO). Windows Store apps can retrieve this information using the [**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256) class.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd><b>&lt;Usage&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Usage OverLimit?     = boolean
       Congested?     = boolean
       CurrentUsage   = nonNegativeInteger
       UsageTimestamp = dateTime />
```

### Key

`?`   optional (zero or one)

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
<td><strong>Congested</strong></td>
<td><p>If <strong>true</strong>, the network is experiencing unusually heavy load and requesting clients to defer transfers. Otherwise, <strong>false</strong>.</p></td>
<td>boolean</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>CurrentUsage</strong></td>
<td><p>Defines a value representing the data used to-date within the current billing cycle in MB. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
<td>nonNegativeInteger</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>OverLimit</strong></td>
<td><p>If <strong>true</strong>, the user has passed their allotted usage (if <strong>PlanType</strong> is Fixed). Otherwise, <strong>false</strong>.</p></td>
<td>boolean</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>UsageTimestamp</strong></td>
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
<td>[Plan](element-plan.md)</td>
<td><p>Defines a set of plan information that specifies the data usage options and state of a subscriber's connection to a Mobile Network Operator (MNO). [<strong>Plan</strong>](element-plan.md) is the unique root element for plan information</p></td>
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

 

 



