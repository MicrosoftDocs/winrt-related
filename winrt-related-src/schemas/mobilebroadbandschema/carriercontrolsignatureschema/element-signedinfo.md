---
Description: SignedInfo
MS-HAID: CarrierControlSignatureSchema.element\_SignedInfo
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: SignedInfo
ms.assetid: 85648eb7-6cb7-4c55-aa7c-3744068c5273
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# SignedInfo


Defines all signed content within the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

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
<td><p>A unique element identifier to be used as a reference to [<strong>SignedInfo</strong>](element-signedinfo.md).</p></td>
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
<td>[CanonicalizationMethod](element-canonicalizationmethod.md)</td>
<td><p>Defines the canonicalization method applied to [<strong>SignedInfo</strong>](element-signedinfo.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/). Must be of type Canonical XML.</p></td>
</tr>
<tr class="even">
<td>[Reference](element-reference.md)</td>
<td><p>Defines a digest value, digest method, and transforms as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[SignatureMethod](element-signaturemethod.md)</td>
<td><p>Defines the algorithm used to generate the signature thumbprint in [<strong>SignatureValue</strong>](element-signaturevalue.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td>[Signature](element-signature.md)</td>
<td><p>Defines the root element of an [XML DSIG](http://www.w3.org/TR/xmldsig-core/) compliant signature. [<strong>Signature</strong>](element-signature.md) is the unique root element for a provisioning file signature.</p></td>
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

 

 



