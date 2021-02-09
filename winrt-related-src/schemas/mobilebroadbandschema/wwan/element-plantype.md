---
description: Defines the type of plan currently in use by the subscriber.
Search.Product: eADQiWindows 10XVcnh
title: PlanType
ms.assetid: b5fa5a45-9931-4678-bffc-be68f6853199

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# PlanType


Defines the type of plan currently in use by the subscriber.

## Element hierarchy

<dl>
<dt><a href="element-messages.md">&lt;Messages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-message.md">&lt;Message&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-fields.md">&lt;Fields&gt;</a></dt>
<dd><b>&lt;PlanType&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PlanType Group?              = positiveInteger
          Default?            = PlanType
          UnrestrictedTokens? = XML token
          FixedTokens?        = XML token
          VariableTokens?     = XML token />
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
<td><strong>Default</strong></td>
<td><p>Defines the default data usage of the subscriber's connection:</p>
<strong>Unrestricted</strong> - the connection is unlimited and is considered to be unrestricted of usage charges and capacity constraints.
<strong>Fixed</strong> - the use of this connection is unrestricted up to a certain cap.
<strong>Variable</strong> - this connection is costed on a per byte basis.</td>
<td>PlanType</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>FixedTokens</strong></td>
<td><p>A token list of <strong>Fixed</strong> plan types.</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Group</strong></td>
<td><p>Defines the group which identifies the new plan type. The contents of this group are compared to the token lists for <strong>FixedTokens</strong>, <strong>UnrestrictedTokens</strong>, and <strong>VariableTokens</strong>. If no match is found, the value of <strong>Default</strong> is used.</p></td>
<td>positiveInteger</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>UnrestrictedTokens</strong></td>
<td><p>A token list of <strong>Unrestricted</strong> plan types.</p></td>
<td>XML token</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>VariableTokens</strong></td>
<td><p>A token list of <strong>Variable</strong> plan types.</p></td>
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
<td><a href="element-fields.md">Fields</a> </td>
<td><p>Defines values that describe the subscriber's plan and data usage.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/WWAN/v1` |

 

 



