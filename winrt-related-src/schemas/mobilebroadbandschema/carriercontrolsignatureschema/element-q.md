---
Description: Defines an integer
Search.Product: eADQiWindows 10XVcnh
title: Q
ms.assetid: 08b57f31-76f6-4a4e-8fac-8bd1711e2498
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Q


Defines an integer in the range 2\*\*159 &lt; [**Q**](element-q.md) &lt; 2\*\*160 which is a prime divisor of [**P**](element-p.md)-1 as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyinfo.md">&lt;KeyInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-keyvalue.md">&lt;KeyValue&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dsakeyvalue.md">&lt;DSAKeyValue&gt;</a></dt>
<dd><b>&lt;Q&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Q>

  base64Binary

</Q>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

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
<td>[DSAKeyValue](element-dsakeyvalue.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



