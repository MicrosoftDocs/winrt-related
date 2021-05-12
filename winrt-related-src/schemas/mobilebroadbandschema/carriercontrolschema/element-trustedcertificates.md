---
description: Defines a list of X.509 certificates whose signatures should be trusted on future provisioning files.
Search.Product: eADQiWindows 10XVcnh
title: TrustedCertificates
ms.assetid: 26d8eb7c-6059-4e7a-9d07-8ad5054385e3

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# TrustedCertificates


Defines a list of X.509 certificates whose signatures should be trusted on future provisioning files.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioning.md">&lt;Provisioning&gt;</a></dt>
<dd><b>&lt;TrustedCertificates&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TrustedCertificates>

  <!-- Child elements -->
  TrustedCertificate+

</TrustedCertificates>
```

### Key

`+`   required (one or more)

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
<td><a href="element-trustedcertificate.md">TrustedCertificate</a> </td>
<td><p>Defines the Subject and Issuer fields from a trustworthy X.509 certificate.</p></td>
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
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 



