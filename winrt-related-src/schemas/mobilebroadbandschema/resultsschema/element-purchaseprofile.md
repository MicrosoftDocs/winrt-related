---
description: Contains any errors from processing the PurchaseProfile element from the last provisioning attempt (ResultsSchema schema).
Search.Product: eADQiWindows 10XVcnh
title: PurchaseProfile (ResultsSchema schema)
ms.assetid: 66b0d844-5469-4e94-b364-72638ac4212a

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# PurchaseProfile (ResultsSchema schema)


Contains any errors from processing the [**PurchaseProfile**](../wwan/element-purchaseprofile.md) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-mbnprofiles.md">&lt;MBNProfiles&gt;</a></dt>
<dd><b>&lt;PurchaseProfile&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PurchaseProfile errorCode = token />
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
<td><a href="element-mbnprofiles.md">MBNProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-mbnprofiles"><strong>MBNProfiles</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v1` |

 

 
