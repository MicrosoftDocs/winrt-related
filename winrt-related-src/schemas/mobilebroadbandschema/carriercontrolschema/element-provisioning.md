---
description: Defines parameters used to establish trust and refresh settings for future provisioning attempts.
Search.Product: eADQiWindows 10XVcnh
title: Provisioning
ms.assetid: a6e7f546-9036-4796-b57d-0d45b591f3d6

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Provisioning


Defines parameters used to establish trust and refresh settings for future provisioning attempts.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioning.md">&lt;CarrierProvisioning&gt;</a></dt>
<dd><b>&lt;Provisioning&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Provisioning>

  <!-- Child elements -->
  TrustedCertificates?,
  RefreshParameters?

</Provisioning>
```

### Key

`?`   optional (zero or one)

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
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
</tr>
<tr class="even">
<td><a href="element-trustedcertificates.md">TrustedCertificates</a> </td>
<td><p>Defines a list of X.509 certificates whose signatures should be trusted on future provisioning files.</p></td>
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
<td><a href="element-carrierprovisioning.md">CarrierProvisioning</a> </td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. <a href="element-carrierprovisioning.md"><strong>CarrierProvisioning</strong></a>  is the unique root element of the provisioning file.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://www.microsoft.com/networking/CarrierControl/v1` |

 

 



