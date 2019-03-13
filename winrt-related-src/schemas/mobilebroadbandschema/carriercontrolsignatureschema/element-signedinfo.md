---
Description: Defines all signed content within the signature.
Search.Product: eADQiWindows 10XVcnh
title: SignedInfo
ms.assetid: 85648eb7-6cb7-4c55-aa7c-3744068c5273
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SignedInfo


Defines all signed content within the signature as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd><b>&lt;SignedInfo&gt;</b></dd>
</dl>

## Syntax

``` syntax
<SignedInfo Id? = ID >

  <!-- Child elements -->
  CanonicalizationMethod,
  SignatureMethod,
  Reference

</SignedInfo>
```

### Key

`?`   optional (zero or one)

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
<td><strong>Id</strong></td>
<td><p>A unique element identifier to be used as a reference to <a href="element-signedinfo.md"><strong>SignedInfo</strong></a> .</p></td>
<td>ID</td>
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
<td><a href="element-canonicalizationmethod.md">CanonicalizationMethod</a> </td>
<td><p>Defines the canonicalization method applied to <a href="element-signedinfo.md"><strong>SignedInfo</strong></a>  as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/). Must be of type Canonical XML.</p></td>
</tr>
<tr class="even">
<td><a href="element-reference.md">Reference</a> </td>
<td><p>Defines a digest value, digest method, and transforms as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-signaturemethod.md">SignatureMethod</a> </td>
<td><p>Defines the algorithm used to generate the signature thumbprint in <a href="element-signaturevalue.md"><strong>SignatureValue</strong></a>  as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td><a href="element-signature.md">Signature</a> </td>
<td><p>Defines the root element of an <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>  compliant signature. [<strong>Signature</strong>](element-signature.md) is the unique root element for a provisioning file signature.</p></td>
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

 

 



