---
author: laurenhughes
ms.assetid: e4acf38c-ec61-411a-bec1-388106202881
title: com:Format (in SurrogateServer/Class)
description: Specifies the file format an application can read and write (activate as).
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, com
---


# com:Format (in SurrogateServer/Class)

## Description
Specifies the file format an application can read and write (activate as).

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
<dt><a href="element-com-surrogateserver.md">&lt;com:SurrogateServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogateserver-class.md">&lt;com:Class&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogate-conversion.md">&lt;com:Conversion&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogate-readwritable.md">&lt;com:ReadWritable&gt;</a></dt>
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