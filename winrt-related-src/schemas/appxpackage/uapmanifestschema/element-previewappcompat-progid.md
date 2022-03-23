---
title: previewappcompat:ProgId
description: A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# previewappcompat:ProgId

A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-package-extension.md">&lt;uap10:Extension&gt;</a></dt>
<dd><b>&lt;previewappcompat:ProgId&gt;</b></dd>
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
<previewAppCompat:ProgId>
  An alphanumeric string that contains between 1 and 255 characters.

</previewAppCompat:ProgId>
```

### Key
`?` optional (zero or one)

## Attributes

None.

## Child Elements

None.

## Parent Elemnts 

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
<td><a href="link.md">UAP10:Protocol</a> </td>
<td><p>Sets parameters to define the protocol of the extensions.</p></td>
</tr>
</tbody>
</table>

## Requirements
|   | Value |
|--|--|
| **previewappcompat** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/msixappcompatsupport/3` |