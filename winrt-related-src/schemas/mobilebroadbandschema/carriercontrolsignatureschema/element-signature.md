---
Description: Signature
MS-HAID: CarrierControlSignatureSchema.element\_Signature
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Signature
ms.assetid: 58a2b918-192d-41ee-879c-b739b498bff0
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Signature


Defines the root element of an [XML DSIG](http://www.w3.org/TR/xmldsig-core/) compliant signature. [**Signature**](element-signature.md) is the unique root element for a provisioning file signature.

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
<td><p>A unique element identifier to be used as a reference to [<strong>Signature</strong>](element-signature.md).</p></td>
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
<td>[KeyInfo](element-keyinfo.md)</td>
<td><p>Defines all key information used to validate the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[SignatureValue](element-signaturevalue.md)</td>
<td><p>Defines the signature thumbprint as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/). The algorithm used to generate [<strong>SignatureValue</strong>](element-signaturevalue.md) is defined in [<strong>SignatureMethod</strong>](element-signaturemethod.md).</p></td>
</tr>
<tr class="odd">
<td>[SignedInfo](element-signedinfo.md)</td>
<td><p>Defines all signed content within the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



