---
Description: Defines a RSA public key.
Search.Product: eADQiWindows 10XVcnh
title: RSAKeyValue
ms.assetid: e44e3743-024d-4edb-8612-1fdc6bcc4289
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# RSAKeyValue


Defines a RSA public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyinfo.md">&lt;KeyInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyvalue.md">&lt;KeyValue&gt;</a></dt>
<dd><b>&lt;RSAKeyValue&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<RSAKeyValue>

  <!-- Child elements -->
  Modulus,
  Exponent

</RSAKeyValue>
```

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
<td>[Exponent](element-exponent.md)</td>
<td><p>Defines the RSA public key exponent as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Modulus](element-modulus.md)</td>
<td><p>Defines the RSA public key modulus as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td>[KeyValue](element-keyvalue.md)</td>
<td><p>Defines a single public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



