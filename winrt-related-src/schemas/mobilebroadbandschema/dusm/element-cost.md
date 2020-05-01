---
Description: Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). 
Search.Product: eADQiWindows 10XVcnh
title: Cost
ms.assetid: d562df54-f0a6-4fbd-bddc-26411f381372

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Cost


Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). [**Cost**](element-cost.md) is the unique root element for DUSM cost information.

## Element hierarchy

**&lt;Cost&gt;**

## Syntax

``` syntax
<Cost OverDataLimit? = boolean
      Congested?     = boolean
      PlanType       = "Unrestricted" | "Fixed" | "Variable" >

  <!-- Child elements -->
  UsageInMegabytes?,
  DataLimitInMegabytes?,
  BillingCycle?,
  BandwidthInKbps?,
  MaxDownloadFileSizeInMegabytes?,
  CarrierPolicy?

</Cost>
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
<td><p>If <strong>true</strong>, the subscriber's connection is in a state of congestion. Otherwise, it is either not supported by the MNO or <strong>false</strong>.</p></td>
<td>boolean</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>OverDataLimit</strong></td>
<td><p>If <strong>true</strong>, the subscriber's connection is in an <strong>Over The Data Limit</strong> state. Otherwise, it is either not supported by the MNO or <strong>false</strong>.</p></td>
<td>boolean</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>PlanType</strong></td>
<td><p>Defines the data usage of the subscriber's connection:</p>
<strong>Unrestricted</strong> - the connection is unlimited and is considered to be unrestricted of usage charges and capacity constraints.
<strong>Fixed</strong> - the use of this connection is unrestricted up to a certain cap.
<strong>Variable</strong> - this connection is costed on a per byte basis.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>Unrestricted</li>
<li>Fixed</li>
<li>Variable</li>
</ul></td>
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
<td><a href="element-bandwidthinkbps.md">BandwidthInKbps</a> </td>
<td><p>Defines a value representing the effective link speed of the subscriber’s connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="even">
<td><a href="element-billingcycle.md">BillingCycle</a> </td>
<td><p>Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle.</p></td>
</tr>
<tr class="odd">
<td><a href="element-carrierpolicy.md">CarrierPolicy</a> </td>
<td><p>Defines optional setting for Windows on this connection.</p></td>
</tr>
<tr class="even">
<td><a href="element-datalimitinmegabytes.md">DataLimitInMegabytes</a> </td>
<td><p>Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-maxdownloadfilesizeinmegabytes.md">MaxDownloadFileSizeInMegabytes</a> </td>
<td><p>Defines a value representing the maximum suggested download size in MB of the subscriber's connection. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="even">
<td><a href="element-usageinmegabytes.md">UsageInMegabytes</a> </td>
<td><p>Defines a value representing the data used to-date within the current billing cycle in MB. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/DUSM/v1` |

 

 



