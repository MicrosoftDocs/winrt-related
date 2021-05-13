---
description: Advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan.
Search.Product: eADQiWindows 10XVcnh
title: SecurityUpdatesExempt
ms.assetid: a59108e9-4bf0-41e9-92ce-99256d578928

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SecurityUpdatesExempt


If **true**, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when **false**.

## Element hierarchy

<dl>
<dt><a href="element-cost.md">&lt;Cost&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carrierpolicy.md">&lt;CarrierPolicy&gt;</a></dt>
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
<td><a href="element-carrierpolicy.md">CarrierPolicy</a> </td>
<td><p>Defines optional setting for Windows on this connection.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/DUSM/v1` |

 

 



