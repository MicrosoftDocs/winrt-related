---
Description: CarrierNetworkMetadata
MS-HAID: ResultsSchema\_v2.element\_CarrierNetworkMetadata
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: CarrierNetworkMetadata
ms.assetid: 6b8fa3df-5138-475d-ac95-305c273730fe
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# CarrierNetworkMetadata


Contains any errors from processing the [**CarrierNetworkMetadata**](https://msdn.microsoft.com/library/windows/apps/dn393998) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;CarrierNetworkMetadata&gt;</b></dd>
</dl>

## Syntax

``` syntax
<CarrierNetworkMetadata errorCode = token >

  <!-- Child elements -->
  NetworkSettings?,
  DataClassFriendlyNames?,
  CustomerSupportPhoneNumber?

</CarrierNetworkMetadata>
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
<td>[CustomerSupportPhoneNumber](element-customersupportphonenumber.md)</td>
<td><p>Contains any errors from processing the [<strong>CustomerSupportPhoneNumber</strong>](https://msdn.microsoft.com/library/windows/apps/dn394004) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[DataClassFriendlyNames](element-dataclassfriendlynames.md)</td>
<td><p>Contains any errors from processing the [<strong>DataClassFriendlyNames</strong>](https://msdn.microsoft.com/library/windows/apps/dn394005) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[NetworkSettings](element-networksettings.md)</td>
<td><p>Contains any errors from processing the [<strong>NetworkSettings</strong>](https://msdn.microsoft.com/library/windows/apps/dn394020) element from the last provisioning attempt.</p></td>
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

 

 



