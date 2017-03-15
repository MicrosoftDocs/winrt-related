---
Description: TrustedCertificates
MS-HAID: MBAE.element\_TrustedCertificates
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: TrustedCertificates
ms.assetid: 26d8eb7c-6059-4e7a-9d07-8ad5054385e3
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# TrustedCertificates


Defines the list of trusted security certificates required for provisioning on the mobile network.

## Element hierarchy

<dl>
<dt><a href="element-mobilebroadbandinfo.md">&lt;MobileBroadbandInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioningengine.md">&lt;ProvisioningEngine&gt;</a></dt>
<dd><b>&lt;TrustedCertificates&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TrustedCertificates>

  <!-- Child elements -->
  TrustedCertificate{0,256},
  any element in a non-schema namespace*

</TrustedCertificates>
```

### Key

`*`   optional (zero or more)
`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

None.

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
<td>[TrustedCertificate](element-trustedcertificate.md)</td>
<td><p>Defines the subject name and issuer name of a trusted certificate required for provisioning on the mobile network.</p></td>
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
<td>[ProvisioningEngine](element-provisioningengine.md)</td>
<td><p>Defines the trusted certificate values for Subject Name and Issuer Name required for provisioning on the mobile network.</p></td>
</tr>
</tbody>
</table>

 

## See also


[MBAE schema](schema-root.md)

[**MobileBroadbandInfo**](element-mobilebroadbandinfo.md)

[**ProvisioningEngine**](element-provisioningengine.md)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo</p></td>
</tr>
</tbody>
</table>

 

 



