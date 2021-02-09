---
description: Defines the length, in bits, of the SignatureValue element.
Search.Product: eADQiWindows 10XVcnh
title: HMACOutputLength
ms.assetid: 062c1b2e-8cf2-4503-abb2-8083cac63fa2

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# HMACOutputLength


Defines the length, in bits, of the [**SignatureValue**](element-signaturevalue.md) element as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signedinfo.md">&lt;SignedInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signaturemethod.md">&lt;SignatureMethod&gt;</a></dt>
<dd><b>&lt;HMACOutputLength&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<HMACOutputLength>

  integer

</HMACOutputLength>
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
<td><a href="element-signaturemethod.md">SignatureMethod</a> </td>
<td><p>Defines the algorithm used to generate the signature thumbprint in <a href="element-signaturevalue.md"><strong>SignatureValue</strong></a>  as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
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
<td><p>http://www.w3.org/2000/09/xmldsig#</p></td>
</tr>
</tbody>
</table>

 

 



