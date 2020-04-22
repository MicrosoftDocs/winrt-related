---
Description: Advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan. 
Search.Product: eADQiWindows 10XVcnh
title: SecurityUpdatesExempt
ms.assetid: 332b9140-c78a-45e2-ad4c-b0ab1be52ada

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SecurityUpdatesExempt


If **true**, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when **false**.

## Element hierarchy

<dl>
<dt><a href="element-plan.md">&lt;Plan&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-description.md">&lt;Description&gt;</a></dt>
<dd><b>&lt;SecurityUpdatesExempt&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<SecurityUpdatesExempt>

  boolean : "false"

</SecurityUpdatesExempt>
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

 

 



