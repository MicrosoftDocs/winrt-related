---
description: Contains any errors from processing the Signature element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: Signature (ResultsSchema schema)
ms.assetid: 58a2b918-192d-41ee-879c-b739b498bff0

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Signature (ResultsSchema schema)


Contains any errors from processing the [**Signature**](../carriercontrolsignatureschema/element-signature.md) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;Signature&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Signature errorCode = token >

  <!-- Child elements -->
  Subject,
  Thumbprint

</Signature>
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
<td><a href="element-subject.md">Subject</a> </td>
<td><p>Contains the X.509 certificate subject field of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signature"><strong>Signature</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-thumbprint.md">Thumbprint</a> </td>
<td><p>Contains the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signaturevalue"><strong>SignatureValue</strong></a>  element of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signature"><strong>Signature</strong></a> from the last provisioning attempt.</p></td>
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
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-carrierprovisioning"><strong>CarrierProvisioning</strong></a>  element from the last provisioning attempt. <a href="element-carrierprovisioningresult.md"><strong>CarrierProvisioningResult</strong></a> is the unique root element for the provisioning results.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v1` |

 

 
