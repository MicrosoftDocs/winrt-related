---
Description: Contains any errors from processing a Plan element from the last provisioning attempt.

Search.Product: eADQiWindows 10XVcnh
title: Plan
ms.assetid: 880ae12d-cd46-4b3b-9b24-3b1f92a64fd0
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Plan


Contains any errors from processing a [**Plan**](https://msdn.microsoft.com/library/windows/apps/hh868298) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-plans.md">&lt;Plans&gt;</a></dt>
<dd><b>&lt;Plan&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Plan errorCode = token
      name      = string />
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
<td><strong>errorCode</strong></td>
<td><p>S_OK if schema processed successfully. Otherwise, the HRESULT returned during the provisioning attempt formatted as eight hexadecimal characters [0-9a-f].</p></td>
<td>token</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>name</strong></td>
<td><p>The name of the plan.</p></td>
<td>string</td>
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
<td>[Plans](element-plans.md)</td>
<td><p>Contains any errors from processing the [<strong>Plans</strong>](https://msdn.microsoft.com/library/windows/apps/hh868299) element from the last provisioning attempt.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControlResults/v2</p></td>
</tr>
</tbody>
</table>

 

 



