---
Description: Contains any errors from processing the AdditionalPDPContexts element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: AdditionalPDPContexts
ms.assetid: 4f4a4b43-e475-4d21-b847-0de7282c4f08
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
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
<td>[MultiplePDPContextPolicies](element-multiplepdpcontextpolicies.md)</td>
<td><p>Contains any errors from processing the [<strong>MultiplePDPContextPolicies</strong>](https://msdn.microsoft.com/library/windows/apps/dn394018) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[TetheringSettings](element-tetheringsettings.md)</td>
<td><p>Contains any errors from processing the [<strong>TetheringSettings</strong>](https://msdn.microsoft.com/library/windows/apps/dn394030) element from the last provisioning attempt.</p></td>
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
<td>[CarrierProvisioningResult](element-carrierprovisioningresult.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierProvisioning</strong>](https://msdn.microsoft.com/library/windows/apps/hh868289) element from the last provisioning attempt. [<strong>CarrierProvisioningResult</strong>](https://msdn.microsoft.com/library/windows/apps/hh868380) is the unique root element for the provisioning results.</p></td>
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

 

 



