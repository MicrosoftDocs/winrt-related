---
Description: Defines how to interpret the unit fields corresponding to each number field. 
Search.Product: eADQiWindows 10XVcnh
title: Units
ms.assetid: 4e4be814-8934-48ae-902a-dd5f5a2dd4cb
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Units


Defines how to interpret the unit fields corresponding to each number field. Carriers may specify a whitespace-delimited list of tokens corresponding to each of the supported multipliers.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd><b>&lt;Units&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Units K?  = XML token
       M?  = XML token
       G?  = XML token
       T?  = XML token
       Ki? = XML token
       Mi? = XML token
       Gi? = XML token
       Ti? = XML token />
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
<td><strong>G</strong></td>
<td><p>Multiplier is a power of 1,000,000,000</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Gi</strong></td>
<td><p>Multiplier is a power of 1,073,741,824</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>K</strong></td>
<td><p>Multiplier is a power of 1,000</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Ki</strong></td>
<td><p>Multiplier is a power of 1,024</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>M</strong></td>
<td><p>Multiplier is a power of 1,000,000</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Mi</strong></td>
<td><p>Multiplier is a power of 1,048,576</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>T</strong></td>
<td><p>Multiplier is a power of 1,000,000,000,000</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Ti</strong></td>
<td><p>Multiplier is a power of 1,099,511,627,776</p></td>
<td>XML token</td>
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
<td><a href="element-message.md">Message</a> </td>
<td><p>Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.</p></td>
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

 

 



