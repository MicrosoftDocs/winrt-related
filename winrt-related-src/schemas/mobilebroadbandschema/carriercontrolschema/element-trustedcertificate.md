---
Description: TrustedCertificate
MS-HAID: CarrierControlSchema.element\_TrustedCertificate
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: TrustedCertificate
ms.assetid: 97eae84a-4357-462b-b516-3099916839c6
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# TrustedCertificate


Defines the Subject and Issuer fields from a trustworthy X.509 certificate.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-trustedcertificates.md">&lt;TrustedCertificates&gt;</a></dt>
<dd><b>&lt;TrustedCertificate&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TrustedCertificate>

  CertificateDetails

</TrustedCertificate>
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
<td>[TrustedCertificates](element-trustedcertificates.md)</td>
<td><p>Defines a list of X.509 certificates whose signatures should be trusted on future provisioning files.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControl/v1</p></td>
</tr>
</tbody>
</table>

 

 



