---
Description: Defines a set of plan information that specifies the data usage options and state of a subscriber's connection to a Mobile Network Operator (MNO).
Search.Product: eADQiWindows 10XVcnh
title: Plan
ms.assetid: 880ae12d-cd46-4b3b-9b24-3b1f92a64fd0

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Plan


Defines a set of plan information that specifies the data usage options and state of a subscriber's connection to a Mobile Network Operator (MNO). [**Plan**](element-plan.md) is the unique root element for plan information

## Element hierarchy

**&lt;Plan&gt;**

## Syntax

``` syntax
<Plan Name = string >

  <!-- Child elements -->
  ( ( Description,
      Usage?
    )
  | Usage
  )

</Plan>
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
<td><strong>Name</strong></td>
<td><p>Defines the name of a subscriber's connection to a MNO.</p></td>
<td>string</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-description.md">Description</a> </td>
<td><p>Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.</p></td>
</tr>
<tr class="even">
<td><a href="element-usage.md">Usage</a> </td>
<td><p>Defines the state of a subscriber's data usage on a connection to a Mobile Network Operator (MNO). UWP apps can retrieve this information using the <a href="/uwp/api/Windows.Networking.Connectivity.DataPlanStatus"><strong>DataPlanStatus</strong></a>  class.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/Plans/v1` |

 

 