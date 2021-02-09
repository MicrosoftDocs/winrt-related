---
description: Defines a Digital Signature Algorithm (DSA) public key.
Search.Product: eADQiWindows 10XVcnh
title: DSAKeyValue
ms.assetid: 41c1ee09-ee66-47a6-b971-6fd9d5340c43

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
<td><a href="element-g.md">G</a> </td>
<td><p>Defines an integer with certain properties with respect to <a href="element-p.md"><strong>P</strong></a>  and <a href="element-q.md"><strong>Q</strong></a> as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-j.md">J</a> </td>
<td><p>Defines (<a href="element-p.md"><strong>P</strong></a>  - 1) / <a href="element-q.md"><strong>Q</strong></a> as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-p.md">P</a> </td>
<td><p>Defines a prime modulus meeting the <a href="https://www.w3.org/2000/09/xmldsig#dsa-sha1 ">DSAwithSHA1</a>  requirements as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-pgencounter.md">PgenCounter</a> </td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation counter as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-q.md">Q</a> </td>
<td><p>Defines an integer in the range 2**159 &lt; <a href="element-q.md"><strong>Q</strong></a>  &lt; 2**160 which is a prime divisor of <a href="element-p.md"><strong>P</strong></a>-1 as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-seed.md">Seed</a> </td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation seed as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-y.md">Y</a> </td>
<td><p>Defines <a href="element-g.md"><strong>G</strong></a> **X mod <a href="element-p.md"><strong>P</strong></a> (where X is part of the private key and not made public) as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
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
<td><a href="element-keyvalue.md">KeyValue</a> </td>
<td><p>Defines a single public key as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
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

 

 



