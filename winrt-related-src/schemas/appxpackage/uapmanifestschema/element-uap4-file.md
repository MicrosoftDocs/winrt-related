---

ms.assetid: 1bf8af5e-3a64-4048-b013-981f805d4836
title: uap4:SharedFonts
description: Specifies the shared fonts.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:SharedFonts

## Description
Specifies the shared fonts.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap4-extension.md">&lt;uap4:Extension&gt;</a></dt>
<dd><b>&lt;uap4:SharedFonts&gt;</b></dd>
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
<uap4:Font File = A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", |, ?, or *. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| File | The font file. | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | Yes |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/4</p></td>
</tr>
</tbody>
</table>