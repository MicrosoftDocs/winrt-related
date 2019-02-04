---
Description: Defines the digest value as specified in XML DSIG.
Search.Product: eADQiWindows 10XVcnh
title: DigestValue
ms.assetid: 2145779c-b719-46f3-aeea-02bc36638962
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DigestValue


Defines the digest value as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/). The algorithm used to generate [**DigestValue**](element-digestvalue.md) is defined in [**DigestMethod**](element-digestmethod.md).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signedinfo.md">&lt;SignedInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-reference.md">&lt;Reference&gt;</a></dt>
<dd><b>&lt;DigestValue&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DigestValue>

  base64Binary

</DigestValue>
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
<td>[Reference](element-reference.md)</td>
<td><p>Defines a digest value, digest method, and transforms as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



