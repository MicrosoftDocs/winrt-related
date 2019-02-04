---
Description: Defines a Digital Signature Algorithm (DSA) public key.
Search.Product: eADQiWindows 10XVcnh
title: DSAKeyValue
ms.assetid: 41c1ee09-ee66-47a6-b971-6fd9d5340c43
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DSAKeyValue


Defines a Digital Signature Algorithm (DSA) public key as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyinfo.md">&lt;KeyInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyvalue.md">&lt;KeyValue&gt;</a></dt>
<dd><b>&lt;DSAKeyValue&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DSAKeyValue>

  <!-- Child elements -->
  P,
  Q,
  G?,
  Y,
  J?,
  Seed,
  PgenCounter

</DSAKeyValue>
```

### Key

`?`   optional (zero or one)

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
<td>[G](element-g.md)</td>
<td><p>Defines an integer with certain properties with respect to [<strong>P</strong>](element-p.md) and [<strong>Q</strong>](element-q.md) as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[J](element-j.md)</td>
<td><p>Defines ([<strong>P</strong>](element-p.md) - 1) / [<strong>Q</strong>](element-q.md) as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[P](element-p.md)</td>
<td><p>Defines a prime modulus meeting the [DSAwithSHA1](https://www.w3.org/2000/09/xmldsig#dsa-sha1 ) requirements as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[PgenCounter](element-pgencounter.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation counter as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[Q](element-q.md)</td>
<td><p>Defines an integer in the range 2**159 &lt; [<strong>Q</strong>](element-q.md) &lt; 2**160 which is a prime divisor of [<strong>P</strong>](element-p.md)-1 as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Seed](element-seed.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation seed as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[Y](element-y.md)</td>
<td><p>Defines [<strong>G</strong>](element-g.md)**X mod [<strong>P</strong>](element-p.md) (where X is part of the private key and not made public) as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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
<td><p>Defines a single public key as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



