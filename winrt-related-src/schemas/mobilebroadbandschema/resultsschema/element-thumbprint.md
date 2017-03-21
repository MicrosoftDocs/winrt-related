---
Description: Contains the SignatureValue element of the Signature from the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: Thumbprint
ms.assetid: 846b806e-25e7-4db8-85c9-895f729474e0
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Thumbprint


Contains the [**SignatureValue**](https://msdn.microsoft.com/library/windows/apps/hh868332) element of the [**Signature**](https://msdn.microsoft.com/library/windows/apps/hh868330) from the last provisioning attempt.

## Element hierarchy

<dl>
<dt><a href="element-carrierprovisioningresult.md">&lt;CarrierProvisioningResult&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd><b>&lt;Thumbprint&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Thumbprint>

  base64Binary

</Thumbprint>
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
<td>[Signature](element-signature.md)</td>
<td><p>Contains any errors from processing the [<strong>Signature</strong>](https://msdn.microsoft.com/library/windows/apps/hh868330) element from the last provisioning attempt.</p></td>
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
<td><p>http://www.microsoft.com/networking/CarrierControlResults/v1</p></td>
</tr>
</tbody>
</table>

 

 



