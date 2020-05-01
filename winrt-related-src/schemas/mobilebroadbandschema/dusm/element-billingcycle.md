---
Description: Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle.
Search.Product: eADQiWindows 10XVcnh
title: BillingCycle
ms.assetid: 8be4cdc8-4b17-47c6-a810-7ab6c55a89e0

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# BillingCycle


Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd><b>&lt;BillingCycle&gt;</b></dd>
</dl>

## Syntax

``` syntax
<BillingCycle StartDate = dateTime
              Duration  = duration
              Resets?   = boolean : "true" />
```

### Key

`?`   optional (zero or one)
`:`   default value
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
<td><strong>Duration</strong></td>
<td><p>A value representing the plan's duration in UTC.</p></td>
<td>duration</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Resets</strong></td>
<td><p>If <strong>true</strong>, all connection usage and information for the subscriber are reset at the end of the billing cycle. Otherwise, <strong>false</strong>.</p></td>
<td>boolean</td>
<td>No</td>
<td>true</td>
</tr>
<tr class="odd">
<td><strong>StartDate</strong></td>
<td><p>A value representing the plan's starting date and time in UTC.</p></td>
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
<td><a href="element-cost.md">Cost</a> </td>
<td><p>Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). <a href="element-cost.md"><strong>Cost</strong></a>  is the unique root element for DUSM cost information.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This information can be used to understand when the next billing cycle begins for the given subscriber’s plan. It is specified in UTC and has at least one minute of precision.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/DUSM/v1` |

 

 



