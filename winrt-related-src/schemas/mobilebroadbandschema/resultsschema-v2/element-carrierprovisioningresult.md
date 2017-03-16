---
Description: CarrierProvisioningResult
MS-HAID: ResultsSchema\_v2.element\_CarrierProvisioningResult
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: CarrierProvisioningResult
ms.assetid: cee41310-6d39-431c-8548-aaec3249ce50
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# CarrierProvisioningResult


Contains any errors from processing the [**CarrierProvisioning**](https://msdn.microsoft.com/library/windows/apps/hh868289) element from the last provisioning attempt. [**CarrierProvisioningResult**](https://msdn.microsoft.com/library/windows/apps/hh868380) is the unique root element for the provisioning results.

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
<td>[Activation](element-activation.md)</td>
<td><p>Contains any errors from processing the [<strong>Activation</strong>](https://msdn.microsoft.com/library/windows/apps/hh868285) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[AdditionalPDPContexts](element-additionalpdpcontexts.md)</td>
<td><p>Contains any errors from processing the [<strong>AdditionalPDPContexts</strong>](https://msdn.microsoft.com/library/windows/apps/dn393994) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[CarrierNetworkMetadata](element-carriernetworkmetadata.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierNetworkMetadata</strong>](https://msdn.microsoft.com/library/windows/apps/dn393998) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Issuer](element-issuer.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierId</strong>](https://msdn.microsoft.com/library/windows/apps/hh868288) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[MBNProfiles](element-mbnprofiles.md)</td>
<td><p>Contains any errors from processing the [<strong>MBNProfiles</strong>](https://msdn.microsoft.com/library/windows/apps/hh868295) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Plans](element-plans.md)</td>
<td><p>Contains any errors from processing the [<strong>Plans</strong>](https://msdn.microsoft.com/library/windows/apps/hh868299) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[Provisioning](element-provisioning.md)</td>
<td><p>Contains any errors from processing the [<strong>Provisioning</strong>](https://msdn.microsoft.com/library/windows/apps/hh868300) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Subscriber](element-subscriber.md)</td>
<td><p>Contains any errors from processing the [<strong>SubscriberId</strong>](https://msdn.microsoft.com/library/windows/apps/hh868305) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[WLANProfiles](element-wlanprofiles.md)</td>
<td><p>Contains any errors from processing the [<strong>WLANProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868422) elements from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

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

 

 



