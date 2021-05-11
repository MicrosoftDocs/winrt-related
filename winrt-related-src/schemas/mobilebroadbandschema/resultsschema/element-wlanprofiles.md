---
description: Contains any errors from processing the WLANProfile elements from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: WLANProfiles
ms.assetid: ca31898f-b3c9-4f87-9a8e-8adc30875413

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# WLANProfiles


Contains any errors from processing the [**WLANProfile**](../wlan/element-wlanprofile.md) elements from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd><b>&lt;WLANProfiles&gt;</b></dd>
</dl>

## Syntax

``` syntax
<WLANProfiles errorCode? = token >

  <!-- Child elements -->
  WLANProfile+

</WLANProfiles>
```

### Key

`?`   optional (zero or one)
`+`   required (one or more)

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
<td><a href="element-wlanprofile.md">WLANProfile</a> </td>
<td><p>Contains any errors from processing a <a href="/uwp/schemas/mobilebroadbandschema/wlan/element-wlanprofile"><strong>WLANProfile</strong></a>  element from the last provisioning attempt.</p></td>
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

 

## Remarks

If processing all WLAN profiles failed with the same error, this error will be shown as **ErrorCode**. If different profiles failed for different reasons, then each profile will be enumerated and have individual **ErrorCode** attributes.

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v1` |

 

 
