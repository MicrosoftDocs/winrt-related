---
Description: Defines the canonicalization method applied to SignedInfo
Search.Product: eADQiWindows 10XVcnh
title: CanonicalizationMethod
ms.assetid: d27bd016-acb9-4ae0-ae19-95d19acb79e7

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CanonicalizationMethod


Defines the canonicalization method applied to [**SignedInfo**](element-signedinfo.md) as specified in [XML DSIG](https://www.w3.org/TR/xmldsig-core/). Must be of type Canonical XML.

## Element hierarchy

<dl>
<dt><a href="element-signature.md">&lt;Signature&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-signedinfo.md">&lt;SignedInfo&gt;</a></dt>
<dd><b>&lt;CanonicalizationMethod&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<CanonicalizationMethod Algorithm = "http://www.w3.org/TR/2001/REC-xml-c14n-20010315" | "http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments" | "http://www.w3.org/2001/10/xml-exc-c14n#" | "http://www.w3.org/2001/10/xml-exc-c14n#WithComments" >

  string

</CanonicalizationMethod>
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
<td><p>Defines the Uniform Resource Locator (URI) of the algorithm used for canonicalization.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>http://www.w3.org/TR/2001/REC-xml-c14n-20010315</li>
<li>http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments</li>
<li>http://www.w3.org/2001/10/xml-exc-c14n#</li>
<li>http://www.w3.org/2001/10/xml-exc-c14n#WithComments</li>
</ul></td>
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
<td><a href="element-signedinfo.md">SignedInfo</a> </td>
<td><p>Defines all signed content within the signature as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
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

 

 



