---
Description: Defines the algorithm used to generate the signature thumbprint in SignatureValue.
Search.Product: eADQiWindows 10XVcnh
title: SignatureMethod
ms.assetid: 1a82d9c6-795f-41a9-a1fa-b3c339a22b02
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# SignatureMethod


Defines the algorithm used to generate the signature thumbprint in [**SignatureValue**](element-signaturevalue.md) as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signedinfo.md">&lt;SignedInfo&gt;</a></dt>
<dd><b>&lt;SignatureMethod&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<SignatureMethod Algorithm = anyURI >

  <!-- Child elements -->
  HMACOutputLength?,
  any element in a non-schema namespace*

  <!-- This element may also contain text (mixed content). -->

</SignatureMethod>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)

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
<td><strong>Algorithm</strong></td>
<td><p>Defines the Uniform Resource Locator (URI) of the algorithm used.</p></td>
<td>anyURI</td>
<td>Yes</td>
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
<td>[HMACOutputLength](element-hmacoutputlength.md)</td>
<td><p>Defines the length, in bits, of the [<strong>SignatureValue</strong>](element-signaturevalue.md) element as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td>[SignedInfo](element-signedinfo.md)</td>
<td><p>Defines all signed content within the signature as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



