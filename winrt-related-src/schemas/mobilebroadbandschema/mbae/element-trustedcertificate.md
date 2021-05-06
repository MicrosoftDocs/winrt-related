---
description: Defines the subject name and issuer name of a trusted certificate required for provisioning on the mobile network.
Search.Product: eADQiWindows 10XVcnh
title: TrustedCertificate (MBAE schema)
ms.assetid: 97eae84a-4357-462b-b516-3099916839c6

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# TrustedCertificate (MBAE schema)


Defines the subject name and issuer name of a trusted certificate required for provisioning on the mobile network.

## Element hierarchy

<dl>
<dt><a href="element-mobilebroadbandinfo.md">&lt;MobileBroadbandInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-provisioningengine.md">&lt;ProvisioningEngine&gt;</a></dt>
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

  <!-- Child elements -->
  SubjectName,
  IssuerName,
  any element in a non-schema namespace*

</TrustedCertificate>
```

### Key

`*`   optional (zero or more)

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
<td><a href="element-issuername.md">IssuerName</a> </td>
<td><p>Defines the issuer name of the trusted certificate.</p></td>
</tr>
<tr class="even">
<td><a href="element-subjectname.md">SubjectName</a> </td>
<td><p>Defines the subject name of the trusted certificate.</p></td>
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
<td><a href="element-trustedcertificates.md">TrustedCertificates</a> </td>
<td><p>Defines the list of trusted security certificates required for provisioning on the mobile network.</p></td>
</tr>
</tbody>
</table>

 

## See also


[MBAE schema](schema-root.md)

[**MobileBroadbandInfo**](element-mobilebroadbandinfo.md)

[**ProvisioningEngine**](element-provisioningengine.md)

[**TrustedCertificates**](element-trustedcertificates.md)

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo` |

 

 



