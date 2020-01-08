---
Description: A certificate for use with the package and placed in the system certificate stores.
Search.Product: eADQiWindows 10XVcnh
title: Certificate
ms.assetid: d3682c0f-fb91-466a-a612-a60c1e6025c9


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Certificate


A certificate for use with the package and placed in the system certificate stores.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-certificates.md">&lt;Certificates&gt;</a></dt>
<dd><b>&lt;Certificate&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Certificate StoreName = A string between 1 and 50 characters in length that cannot contain these characters: <, >, :, %, ", /, \, |, ?, or *.
             Content   = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *. />
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
<td><strong>Content</strong></td>
<td><p>The path to the certificate content to place in the store. This string must be between 1 and 256 characters in length and cannot contain these characters: &lt;, &gt;, :, &quot;, /, \, |, ?, or *</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StoreName</strong></td>
<td><p>The store name to place the certificate.</p></td>
<td>A string between 1 and 50 characters in length that cannot contain these characters: &lt;, &gt;, :, %, &quot;, /, \, |, ?, or *.</td>
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
<td><a href="element-certificates.md">Certificates</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.certificates</strong>. The app requires one or more certificates from the specified certificate stores.</p></td>
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
<td><pre>http://schemas.microsoft.com/appx/2010/manifest</pre></td>
</tr>
</tbody>
</table>

 

 



