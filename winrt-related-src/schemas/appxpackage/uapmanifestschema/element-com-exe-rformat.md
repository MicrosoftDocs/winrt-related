---
author: laurenhughes
ms.assetid: 1fbe5e60-a8b8-4dc6-b128-674c09b68109
title: com:Format
description: Specifies the file format an application can read (convert from).
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:Format

## Description
Specifies the file format an application can read (convert from).

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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-comserver.md">&lt;com:ComServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver.md">&lt;com:ExeServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver-class.md">&lt;com:Class&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exe-conversion.md">&lt;com:Conversion&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exe-readable.md">&lt;com:Readable&gt;</a></dt>
<dd><b>&lt;com:Format&gt;</b></dd>
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
<com:Format
    FormatName? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    StandardFormat? = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). >
</com:Format>
```

## Key
`?`   optional (zero or more)

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| FormatName | The string file format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| StandardFormat | The hexadecimal file format name. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | No |

## Remarks
> [!NOTE]
> **FormatName** and **StandardFormat** are mutually exclusive.

## Examples

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>