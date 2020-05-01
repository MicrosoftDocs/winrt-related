---
Description: Contains any errors from processing the AdditionalPDPContexts element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: AdditionalPDPContexts
ms.assetid: 4f4a4b43-e475-4d21-b847-0de7282c4f08

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# AdditionalPDPContexts


Contains any errors from processing the [**AdditionalPDPContexts**](https://msdn.microsoft.com/library/windows/apps/dn393994) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;AdditionalPDPContexts&gt;</b></dd>
</dl>

## Syntax

``` syntax
<AdditionalPDPContexts errorCode = token >

  <!-- Child elements -->
  MultiplePDPContextPolicies,
  TetheringSettings

</AdditionalPDPContexts>
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
<td><a href="element-multiplepdpcontextpolicies.md">MultiplePDPContextPolicies</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394018"><strong>MultiplePDPContextPolicies</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-tetheringsettings.md">TetheringSettings</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394030"><strong>TetheringSettings</strong></a>  element from the last provisioning attempt.</p></td>
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
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868289"><strong>CarrierProvisioning</strong></a>  element from the last provisioning attempt. <a href="https://msdn.microsoft.com/library/windows/apps/hh868380"><strong>CarrierProvisioningResult</strong></a> is the unique root element for the provisioning results.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v2` |

 

 



