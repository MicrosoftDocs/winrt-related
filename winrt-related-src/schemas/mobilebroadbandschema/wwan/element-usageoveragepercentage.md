---
Description: Defines the percentage over the data limit a subscriber has consumed.
Search.Product: eADQiWindows 10XVcnh
title: UsageOveragePercentage
ms.assetid: d4cd6983-33f8-4646-ae2a-fb98b9203e98

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# UsageOveragePercentage


Defines the percentage over the data limit a subscriber has consumed.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-fields.md">&lt;Fields&gt;</a></dt>
<dd><b>&lt;UsageOveragePercentage&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<UsageOveragePercentage Group = positiveInteger />
```

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
<td><strong>Group</strong></td>
<td><p>Defines the group that contains the data limit. This must be a number formatted per the specified <a href="https://msdn.microsoft.com/library/windows/apps/hh868459"><strong>Locale</strong></a> .</p></td>
<td>positiveInteger</td>
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
<td><a href="element-fields.md">Fields</a> </td>
<td><p>Defines values that describe the subscriber's plan and data usage.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If the **UsageOveragePercentage** element is included in the schema, then the **UsageTimestamp** element must also be included.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



