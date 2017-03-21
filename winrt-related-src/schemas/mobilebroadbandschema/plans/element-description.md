---
Description: Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.
Search.Product: eADQiWindows 10XVcnh
title: Description
ms.assetid: e113111a-1d9b-4d04-bd86-86beece204dd
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Description


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
<td>[BillingCycle](element-billingcycle.md)</td>
<td><p>Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="even">
<td>[DataLimitInMegabytes](element-datalimitinmegabytes.md)</td>
<td><p>Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="odd">
<td>[DataUsageInMobileOperatorNotificationEnabled](element-datausageinmobileoperatornotificationenabled.md)</td>
<td><p>Indicates whether the [<strong>NetworkOperatorNotificationTrigger</strong>](https://msdn.microsoft.com/library/windows/apps/br224831) should include data usage notifications. If <strong>true</strong>, Windows raises this trigger when the data usage threshold is met.</p></td>
</tr>
<tr class="even">
<td>[InboundBandwidthInKbps](element-inboundbandwidthinkbps.md)</td>
<td><p>Defines a value representing the effective link speed of the subscriber’s inbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="odd">
<td>[MaxTransferSizeInMegabytes](element-maxtransfersizeinmegabytes.md)</td>
<td><p>Defines the size of an individual download in MB which a compliant application should permit over a metered connection without explicit user approval of the connection being used. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="even">
<td>[OutboundBandwidthInKbps](element-outboundbandwidthinkbps.md)</td>
<td><p>Defines a value representing the effective link speed of the subscriber’s outbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="odd">
<td>[SecurityUpdatesExempt](element-plan.md)</td>
<td><p>If <strong>true</strong>, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td>[UserSMSEnabled](element-usersmsenabled.md)</td>
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
<td>[Plan](element-plan.md)</td>
<td><p>Defines a set of plan information that specifies the data usage options and state of a subscriber's connection to a Mobile Network Operator (MNO). [<strong>Plan</strong>](element-plan.md) is the unique root element for plan information</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/Plans/v1</p></td>
</tr>
</tbody>
</table>

 

 



