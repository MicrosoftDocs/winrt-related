---
Description: Defines a single public key
Search.Product: eADQiWindows 10XVcnh
title: KeyValue
ms.assetid: 3d01d1da-fa17-49e8-873e-255f8ad5a110
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# KeyValue


Defines a single public key as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyinfo.md">&lt;KeyInfo&gt;</a></dt>
<dd><b>&lt;KeyValue&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<KeyValue>

  <!-- Child elements -->
  ( DSAKeyValue
  | RSAKeyValue
  | any element in a non-schema namespace{}
  )

  <!-- This element may also contain text (mixed content). -->

</KeyValue>
```

### Key

`{}`   specific range of occurrences
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
<td>[DSAKeyValue](element-dsakeyvalue.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) public key as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[RSAKeyValue](element-rsakeyvalue.md)</td>
<td><p>Defines a RSA public key as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td>[KeyInfo](element-keyinfo.md)</td>
<td><p>Defines all key information used to validate the signature as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



