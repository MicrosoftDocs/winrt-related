---
Description: Contains any errors from processing the CarrierProvisioning element from the last provisioning attempt. 
Search.Product: eADQiWindows 10XVcnh
title: CarrierProvisioningResult
ms.assetid: cee41310-6d39-431c-8548-aaec3249ce50

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierProvisioningResult


Contains any errors from processing the [**CarrierProvisioning**](../carriercontrolschema/element-carrierprovisioning.md) element from the last provisioning attempt. [**CarrierProvisioningResult**](../resultsschema/element-carrierprovisioningresult.md) is the unique root element for the provisioning results.

## Element hierarchy

**&lt;CarrierProvisioningResult&gt;**

## Syntax

``` syntax
<CarrierProvisioningResult errorCode? = token >

  <!-- Child elements -->
  ( Issuer
  & Subscriber
  & Activation?
  & MBNProfiles?
  & WLANProfiles?
  & Provisioning?
  & Plans?
  & CarrierNetworkMetadata
  & AdditionalPDPContexts
  )?

</CarrierProvisioningResult>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

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
<td><a href="element-activation.md">Activation</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-activation"><strong>Activation</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-additionalpdpcontexts.md">AdditionalPDPContexts</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema-v2/element-additionalpdpcontexts"><strong>AdditionalPDPContexts</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-carriernetworkmetadata.md">CarrierNetworkMetadata</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema-v2/element-carriernetworkmetadata"><strong>CarrierNetworkMetadata</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-issuer.md">Issuer</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-carrierid"><strong>CarrierId</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-mbnprofiles.md">MBNProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-mbnprofiles"><strong>MBNProfiles</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-plans.md">Plans</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-plans"><strong>Plans</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-provisioning"><strong>Provisioning</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-subscriber.md">Subscriber</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-subscriberid"><strong>SubscriberId</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-wlanprofiles.md">WLANProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/wlan/element-wlanprofile"><strong>WLANProfile</strong></a>  elements from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControlResults/v2` |

 

 