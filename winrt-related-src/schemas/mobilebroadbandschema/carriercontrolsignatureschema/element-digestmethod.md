---
Description: Defines the algorithm used to generate DigestValue
Search.Product: eADQiWindows 10XVcnh
title: DigestMethod
ms.assetid: de7b02d8-8d72-4e94-887f-5f319784e79b
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DigestMethod


Defines the algorithm used to generate [**DigestValue**](element-digestvalue.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signedinfo.md">&lt;SignedInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-reference.md">&lt;Reference&gt;</a></dt>
<dd><b>&lt;DigestMethod&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DigestMethod Algorithm = anyURI >

  <!-- Child elements -->
  any element in a non-schema namespace*

  <!-- This element may also contain text (mixed content). -->

</DigestMethod>
```

### Key

`*`   optional (zero or more)

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
<td><strong>Algorithm</strong></td>
<td><p>Defines the Uniform Resource Locator (URI) of the algorithm used.</p></td>
<td>anyURI</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><p>Defines a digest value, digest method, and transforms as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



