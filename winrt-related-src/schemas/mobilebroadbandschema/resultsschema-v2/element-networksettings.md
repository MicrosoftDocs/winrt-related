---
Description: Contains any errors from processing the NetworkSettings element from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: NetworkSettings
ms.assetid: 82e8282b-5405-4fcf-b835-83fe6ec9a460

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# NetworkSettings


Contains any errors from processing the [**NetworkSettings**](https://msdn.microsoft.com/library/windows/apps/dn394020) element from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-carriernetworkmetadata.md">&lt;CarrierNetworkMetadata&gt;</a></dt>
<dd><b>&lt;NetworkSettings&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<NetworkSettings errorCode = token />
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
<td><a href="element-carriernetworkmetadata.md">CarrierNetworkMetadata</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn393998"><strong>CarrierNetworkMetadata</strong></a>  element from the last provisioning attempt.</p></td>
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

 

 



