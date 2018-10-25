---
author: laurenhughes
ms.assetid: 152ab966-bf59-4b40-83b6-1a653f9361f9
title: com:DataFormats (in SurrogateServer/Class)
description: Specifies the default and main data formats supported by an application.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:DataFormats (in SurrogateServer/Class)

## Description
Specifies the default and main data formats supported by an application.

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
<dd><b>&lt;com:DataFormats&gt;</b></dd>
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
<com:DataFormats
  DefaultFormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
  DefaultStandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). >

  <!-- Child elements -->
  DataFormat{0,1000}
</com:DataFormats>
```

## Key
`{}`   specific range of occurrences 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DefaultFormatName | The string value of the format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| DefaultStandardFormat | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | Yes |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [DataFormat](element-com-surrogate-dataformat.md) | The data format supported by an application. |

## Remarks
**DefaultFormatName** is the string value, and **DefaultStandardFormat** is the integer value of the supported data formats. These values are mutually exclusive.

This element corresponds to the [DataFormats](https://msdn.microsoft.com/library/windows/desktop/ms678525.aspx) subkey.

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