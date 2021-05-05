---
description: Contains any errors from processing the Provisioning element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: Provisioning (ResultsSchema_v2 schema)
ms.assetid: a6e7f546-9036-4796-b57d-0d45b591f3d6

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Provisioning (ResultsSchema_v2 schema)


Contains any errors from processing the [**Provisioning**](../carriercontrolschema/element-provisioning.md) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;Provisioning&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Provisioning errorCode? = token >

  <!-- Child elements -->
  RefreshParameters?,
  TrustedCertificate?

</Provisioning>
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
<td><strong>errorCode</strong></td>
<td><p>S_OK if schema processed successfully. Otherwise, the HRESULT returned during the provisioning attempt formatted as eight hexadecimal characters [0-9a-f].</p></td>
<td>token</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-refreshparameters"><strong>RefreshParameters</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-trustedcertificate.md">TrustedCertificate</a> </td>
<td><p>Contains errors from processing any of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-trustedcertificate"><strong>TrustedCertificate</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-carrierprovisioningresult.md">CarrierProvisioningResult</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-carrierprovisioning"><strong>CarrierProvisioning</strong></a>  element from the last provisioning attempt. <a href="/uwp/schemas/mobilebroadbandschema/resultsschema/element-carrierprovisioningresult"><strong>CarrierProvisioningResult</strong></a> is the unique root element for the provisioning results.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v2` |

 

 
