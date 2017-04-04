---
Description: Defines if the subscriber's connection is in a state of congestion. 
Search.Product: eADQiWindows 10XVcnh
title: Congested
ms.assetid: 4807217f-0145-4a7d-9d5f-a8fdd2017b85
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Congested


If **true**, the subscriber's connection is in a state of congestion. Otherwise, it is either not supported by the MNO or **false**.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-fields.md">&lt;Fields&gt;</a></dt>
<dd><b>&lt;Congested&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Congested TrueToken?  = token
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
<td>[Fields](element-fields.md)</td>
<td><p>Defines values that describe the subscriber's plan and data usage.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/WWAN/v1</p></td>
</tr>
</tbody>
</table>

 

 



