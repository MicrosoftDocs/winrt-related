---
Description: Contains any errors from processing the CarrierPolicy schema from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: Policy
ms.assetid: 4cabf792-57b6-42b1-94bc-1f4138d09534

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Policy


Contains any errors from processing the [**CarrierPolicy**](../dusm/element-carrierpolicy.md) schema from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd><b>&lt;Policy&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Policy errorCode = token />
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
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-provisioning"><strong>Provisioning</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v1` |

 

 