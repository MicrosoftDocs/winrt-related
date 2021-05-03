---
description: Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.
Search.Product: eADQiWindows 10XVcnh
title: Description (Plans schema)
ms.assetid: e113111a-1d9b-4d04-bd86-86beece204dd


keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Description (Plans schema)


Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd><b>&lt;Description&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Description PlanType = "Unrestricted" | "Fixed" | "Variable" >

  <!-- Child elements -->
  BillingCycle?,
  DataLimitInMegabytes?,
  InboundBandwidthInKbps?,
  OutboundBandwidthInKbps?,
  MaxTransferSizeInMegabytes?,
  SecurityUpdatesExempt?,
  DataUsageInMobileOperatorNotificationEnabled?,
  UserSMSEnabled?

</Description>
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
<td><a href="element-billingcycle.md">BillingCycle</a> </td>
<td><p>Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle. UWP apps can retrieve this information using the <a href="/uwp/api/Windows.Networking.Connectivity.DataPlanStatus"><strong>DataPlanStatus</strong></a>  class.</p></td>
</tr>
<tr class="even">
<td><a href="element-datalimitinmegabytes.md">DataLimitInMegabytes</a> </td>
<td><p>Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the <a href="/uwp/api/Windows.Networking.Connectivity.DataPlanStatus"><strong>DataPlanStatus</strong></a>  class.</p></td>
</tr>
<tr class="odd">
<td><a href="element-datausageinmobileoperatornotificationenabled.md">DataUsageInMobileOperatorNotificationEnabled</a> </td>
<td><p>Indicates whether the <a href="/uwp/api/Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger"><strong>NetworkOperatorNotificationTrigger</strong></a>  should include data usage notifications. If <strong>true</strong>, Windows raises this trigger when the data usage threshold is met.</p></td>
</tr>
<tr class="even">
<td><a href="element-inboundbandwidthinkbps.md">InboundBandwidthInKbps</a> </td>
<td><p>Defines a value representing the effective link speed of the subscriber’s inbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the <a href="/uwp/api/Windows.Networking.Connectivity.DataPlanStatus"><strong>DataPlanStatus</strong></a>  class.</p></td>
</tr>
<tr class="odd">
<td><a href="element-maxtransfersizeinmegabytes.md">MaxTransferSizeInMegabytes</a> </td>
<td><p>Defines the size of an individual download in MB which a compliant application should permit over a metered connection without explicit user approval of the connection being used. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the <a href="/uwp/api/Windows.Networking.Connectivity.DataPlanStatus"><strong>DataPlanStatus</strong></a>  class.</p></td>
</tr>
<tr class="even">
<td><a href="element-outboundbandwidthinkbps.md">OutboundBandwidthInKbps</a> </td>
<td><p>Defines a value representing the effective link speed of the subscriber’s outbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. UWP apps can retrieve this information using the <a href="/uwp/api/Windows.Networking.Connectivity.DataPlanStatus"><strong>DataPlanStatus</strong></a>  class.</p></td>
</tr>
<tr class="odd">
<td><a href="element-plan.md">SecurityUpdatesExempt</a> </td>
<td><p>If <strong>true</strong>, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td><a href="element-usersmsenabled.md">UserSMSEnabled</a> </td>
<td><p>Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time. If <strong>true</strong>, Windows will employ less aggressive power management on the Mobile Broadband interface to allow SMS messages to arrive more quickly. If <strong>false</strong>, the mobile broadband radio may be turned off during periods of inactivity. SMS messages will arrive when the PC is next active.</p></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-plan.md">Plan</a> </td>
<td><p>Defines a set of plan information that specifies the data usage options and state of a subscriber's connection to a Mobile Network Operator (MNO). <a href="element-plan.md"><strong>Plan</strong></a>  is the unique root element for plan information</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/Plans/v1` |

 

 
