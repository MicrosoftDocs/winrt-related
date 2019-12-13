---
Description: Defines optional setting for Windows on this connection.
Search.Product: eADQiWindows 10XVcnh
title: CarrierPolicy
ms.assetid: 36db68fb-6961-47c2-bc36-84aa5ec4a5c5

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierPolicy


Defines optional setting for Windows on this connection.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd><b>&lt;CarrierPolicy&gt;</b></dd>
</dl>

## Syntax

``` syntax
<CarrierPolicy>

  <!-- Child elements -->
  SecurityUpdatesExempt?,
  UserSMSEnabled?

</CarrierPolicy>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-securityupdatesexempt.md">SecurityUpdatesExempt</a> </td>
<td><p>If <strong>true</strong>, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td><a href="element-usersmsenabled.md">UserSMSEnabled</a> </td>
<td><p>Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time. If <strong>true</strong>, Windows will employ less aggressive power management on the Mobile Broadband interface to allow SMS messages to arrive more quickly. If <strong>false</strong>, SMS messages will arrive when the PC is next active.</p></td>
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
<td><a href="element-cost.md">Cost</a> </td>
<td><p>Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). <a href="element-cost.md"><strong>Cost</strong></a>  is the unique root element for DUSM cost information.</p></td>
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

 

 



