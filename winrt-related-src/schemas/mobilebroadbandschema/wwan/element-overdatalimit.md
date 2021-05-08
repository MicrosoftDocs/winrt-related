---
description: Defines whether a subscriber has consumed more bytes than the data limit for their plan.
Search.Product: eADQiWindows 10XVcnh
title: OverDataLimit
ms.assetid: effb2b5e-e571-42cf-9a5a-72b0b7b3d437

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# OverDataLimit


Defines whether a subscriber has consumed more bytes than the data limit for their plan.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-fields.md">&lt;Fields&gt;</a></dt>
<dd><b>&lt;OverDataLimit&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<OverDataLimit TrueToken?  = token
               FalseToken? = token
               Default?    = boolean : "false"
               Group?      = positiveInteger />
```

### Key

`?`   optional (zero or one)
`:`   default value
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
<td><strong>Default</strong></td>
<td><p>Defines the default value. Possible values are <strong>true</strong> and <strong>false</strong>.</p></td>
<td>boolean</td>
<td>No</td>
<td>false</td>
</tr>
<tr class="even">
<td><strong>FalseToken</strong></td>
<td><p>A token list of <strong>true</strong> Booleans.</p></td>
<td>token</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Group</strong></td>
<td><p>Defines the group that will be compared against the <strong>TrueToken</strong> and <strong>FalseToken</strong> lists. If no match is found in either list, the value in <strong>Default</strong> will be used.</p></td>
<td>positiveInteger</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>TrueToken</strong></td>
<td><p>A token list of <strong>true</strong> Booleans.</p></td>
<td>token</td>
<td>No</td>
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

 

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



