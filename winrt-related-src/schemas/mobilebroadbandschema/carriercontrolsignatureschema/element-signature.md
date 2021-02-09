---
description: Defines the root element of an XML DSIG compliant signature.
Search.Product: eADQiWindows 10XVcnh
title: Signature
ms.assetid: 58a2b918-192d-41ee-879c-b739b498bff0

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Signature


Defines the root element of an [XML DSIG](https://www.w3.org/TR/xmldsig-core/) compliant signature. [**Signature**](element-signature.md) is the unique root element for a provisioning file signature.

## Element hierarchy

**&lt;Signature&gt;**

## Syntax

``` syntax
<Signature Id? = ID >

  <!-- Child elements -->
  SignedInfo,
  SignatureValue,
  KeyInfo?

</Signature>
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
<td><p>A unique element identifier to be used as a reference to <a href="element-signature.md"><strong>Signature</strong></a> .</p></td>
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
<td><a href="element-keyinfo.md">KeyInfo</a> </td>
<td><p>Defines all key information used to validate the signature as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-signaturevalue.md">SignatureValue</a> </td>
<td><p>Defines the signature thumbprint as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> . The algorithm used to generate <a href="element-signaturevalue.md"><strong>SignatureValue</strong></a> is defined in <a href="element-signaturemethod.md"><strong>SignatureMethod</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-signedinfo.md">SignedInfo</a> </td>
<td><p>Defines all signed content within the signature as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
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
<td><p>http://www.w3.org/2000/09/xmldsig#</p></td>
</tr>
</tbody>
</table>

 

 



