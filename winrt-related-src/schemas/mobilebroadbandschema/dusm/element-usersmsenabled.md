---
Description: Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time.
Search.Product: eADQiWindows 10XVcnh
title: UserSMSEnabled
ms.assetid: 898c68cd-8d04-45f2-b5a8-d1e8923396bf

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# UserSMSEnabled


Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time. If **true**, Windows will employ less aggressive power management on the Mobile Broadband interface to allow SMS messages to arrive more quickly. If **false**, SMS messages will arrive when the PC is next active.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carrierpolicy.md">&lt;CarrierPolicy&gt;</a></dt>
<dd><b>&lt;UserSMSEnabled&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<UserSMSEnabled>

  boolean : "true"

</UserSMSEnabled>
```

### Key

`:`   default value
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
<td><a href="element-carrierpolicy.md">CarrierPolicy</a> </td>
<td><p>Defines optional setting for Windows on this connection.</p></td>
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

 

 



