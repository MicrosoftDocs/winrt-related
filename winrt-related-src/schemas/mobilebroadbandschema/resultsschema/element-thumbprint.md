---
Description: Contains the SignatureValue element of the Signature from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: Thumbprint
ms.assetid: 846b806e-25e7-4db8-85c9-895f729474e0

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Thumbprint


Contains the [**SignatureValue**](../carriercontrolsignatureschema/element-signaturevalue.md) element of the [**Signature**](../carriercontrolsignatureschema/element-signature.md) from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd><b>&lt;Thumbprint&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Thumbprint>

  base64Binary

</Thumbprint>
```

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-signature.md">Signature</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868330"><strong>Signature</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v1` |

 

 