---
Description: Defines all key information used to validate the signature.
Search.Product: eADQiWindows 10XVcnh
title: KeyInfo
ms.assetid: f593f831-e9e6-40f8-861e-3405e7ae8f3d
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# KeyInfo


Defines all key information used to validate the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd><b>&lt;KeyInfo&gt;</b></dd>
</dl>

## Syntax

``` syntax
<KeyInfo Id? = ID >

  <!-- Child elements -->
  ( KeyValue
  | X509Data
  | any element in a non-schema namespace{}
  )+

  <!-- This element may also contain text (mixed content). -->

</KeyInfo>
```

### Key

`?`   optional (zero or one)
`+`   required (one or more)
`{}`   specific range of occurrences
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
<td><p>A unique element identifier to be used as a reference to [<strong>KeyInfo</strong>](element-keyinfo.md).</p></td>
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
<td>[KeyValue](element-keyvalue.md)</td>
<td><p>Defines a single public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[X509Data](element-x509data.md)</td>
<td><p>Defines one or more X.509 compliant signatures as defined in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

## Remarks

The **KeyInfo** element is required.

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

 

 



