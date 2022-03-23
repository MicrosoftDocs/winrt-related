---
title: uap10:Logo
description: A path to a file that contains an image.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap10:Logo

A path to a file that contains an image.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-package-extension.md">&lt;UAP10:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-protocol.md">&lt;uap10:Protocol&gt;</a></dt>
<dd><b>&lt;uap10:Logo&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap10:Logo>
  A string between 1 and 256 characters in length that ends with ".jpg", ".png", "jpeg".
</uap10:Logo>
```

## Attributes

None.

## Child Elements

None.

## Parent Elements

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
<td><a href="element-uap10-protocol.md">UAP10:Protocol</a> </td>
<td><p>Sets parameters to define the protocol of the extensions.</p></td>
</tr>
</tbody>
</table>

## Requirements
|   | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |