---
Description: Defines a transform applied to the digested data object prior to DigestMethod.
Search.Product: eADQiWindows 10XVcnh
title: Transform
ms.assetid: 21cc5a17-8420-4794-978e-97cfec3f3ac9
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Transform


Defines a transform applied to the digested data object prior to [**DigestMethod**](element-digestmethod.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signedinfo.md">&lt;SignedInfo&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-reference.md">&lt;Reference&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-transforms.md">&lt;Transforms&gt;</a></dt>
<dd><b>&lt;Transform&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Transform Algorithm = "http://www.w3.org/2000/09/xmldsig#enveloped-signature" >

  string

</Transform>
```

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
<td><p>Defines the Uniform Resource Locator (URI) of the transform used.</p></td>
<td><p>This attribute must have the following value when present: http://www.w3.org/2000/09/xmldsig#enveloped-signature</p></td>
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
<td>[Transforms](element-transforms.md)</td>
<td><p>Defines a an ordered list of transforms applied to the digested data object as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
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

 

 



