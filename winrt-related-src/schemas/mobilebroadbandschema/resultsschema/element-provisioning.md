---
Description: Provisioning
MS-HAID: ResultsSchema.element\_Provisioning
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Provisioning
ms.assetid: a6e7f546-9036-4796-b57d-0d45b591f3d6
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# Provisioning


Contains any errors from processing the [**Provisioning**](https://msdn.microsoft.com/library/windows/apps/hh868300) element from the last provisioning attempt.

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
  TrustedCertificate?,
  Policy?

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
<td>[Policy](element-policy.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierPolicy</strong>](https://msdn.microsoft.com/library/windows/apps/hh868345) schema from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[RefreshParameters](element-refreshparameters.md)</td>
<td><p>Contains any errors from processing the [<strong>RefreshParameters</strong>](https://msdn.microsoft.com/library/windows/apps/hh868302) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[TrustedCertificate](element-trustedcertificate.md)</td>
<td><p>Contains errors from processing any of the [<strong>TrustedCertificate</strong>](https://msdn.microsoft.com/library/windows/apps/hh868306) element from the last provisioning attempt.</p></td>
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
<td><p>Contains any errors from processing the [<strong>CarrierProvisioning</strong>](https://msdn.microsoft.com/library/windows/apps/hh868289) element from the last provisioning attempt. [<strong>CarrierProvisioningResult</strong>](element-carrierprovisioningresult.md) is the unique root element for the provisioning results.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControlResults/v1</p></td>
</tr>
</tbody>
</table>

 

 



