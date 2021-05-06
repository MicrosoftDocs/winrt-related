---
description: Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time.
Search.Product: eADQiWindows 10XVcnh
title: UserSMSEnabled (Plans schema)
ms.assetid: 898c68cd-8d04-45f2-b5a8-d1e8923396bf

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# UserSMSEnabled (Plans schema)


Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time. If **true**, Windows will employ less aggressive power management on the Mobile Broadband interface to allow SMS messages to arrive more quickly. If **false**, the mobile broadband radio may be turned off during periods of inactivity. SMS messages will arrive when the PC is next active.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd><b>&lt;Usage&gt;</b></dd>
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
<td><a href="element-description.md">Description</a> </td>
<td><p>Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/Plans/v1` |

 

 



