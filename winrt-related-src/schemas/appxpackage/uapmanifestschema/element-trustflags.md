---
Description: TrustFlags (Windows 10)
Search.Product: eADQiWindows 10XVcnh
title: TrustFlags (Windows 10)
ms.assetid: 44ea0d79-4774-4152-8f69-c5d9ff9287aa
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# TrustFlags (Windows 10)


Indicates whether the certificates for the package are exclusive to the package.

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
<dd><b>&lt;TrustFlags&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TrustFlags ExclusiveTrust = boolean />
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
<td><strong>ExclusiveTrust</strong></td>
<td><p>Indicates whether the declared certificates are exclusive to the package. <strong>true</strong> if they are exclusive to the package; otherwise, <strong>false</strong>.</p></td>
<td>boolean</td>
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
<td>[Certificates](element-certificates.md)</td>
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
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



