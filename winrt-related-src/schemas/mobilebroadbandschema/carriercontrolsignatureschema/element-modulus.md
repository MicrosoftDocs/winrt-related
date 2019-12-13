---
Description: Defines the RSA public key modulus.
Search.Product: eADQiWindows 10XVcnh
title: Modulus
ms.assetid: 33ec8118-3a6a-4273-96bf-2109d4305ca8

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# Modulus


Defines the RSA public key modulus as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).

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
<dt><a href="element-rsakeyvalue.md">&lt;RSAKeyValue&gt;</a></dt>
<dd><b>&lt;Modulus&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Modulus>

  base64Binary

</Modulus>
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
<td><a href="element-rsakeyvalue.md">RSAKeyValue</a> </td>
<td><p>Defines a RSA public key as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
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

 

 



