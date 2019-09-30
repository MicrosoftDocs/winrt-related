---
author: mcleanbyron
ms.assetid: 80ce46c6-31e0-4e75-87b1-a8e6e18aea31
title: com:DataFormat (in SurrogateServer/Class)
description: The data format supported by an application.
ms.author: mcleans
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:DataFormat (in SurrogateServer/Class)

## Description
The data format supported by an application.

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
<dt><a href="element-com-surrogate-dataformats.md">&lt;com:DataFormats&gt;</a></dt>
<dd><b>&lt;com:DataFormat&gt;</b></dd>
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
<com:DataFormat
  AspectFlag = A string as one of the enumeration values: Content, Thumbnail, Icon, or DocPrint.
  MediumFlag = An integer value in the range of 0-127.
  Direction = A string as one of the enumeration values: Get, Set, or GetAndSet.
  FormatName? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
  StandardFormat? = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). >
</com:DataFormat>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| AspectFlag | Represents a [DVASPECT](https://msdn.microsoft.com/library/windows/desktop/ms690318.aspx) enumeration value for the desired data or view aspect. | A string as one of the enumeration values: Content, Thumbnail, Icon, or DocPrint. | Yes |
| MediumFlag | The type of storage medium used for data transfer. This corresponds to the [TYMED](https://msdn.microsoft.com/library/windows/desktop/ms691227.aspx) enumeration. | An integer value in the range of 0-127. | Yes |
| Direction | This represents the [DATADIR](https://msdn.microsoft.com/library/windows/desktop/ms680661.aspx) enumeration which corresponds to the direction of the data flow. | A string as one of the enumeration values: Get, Set, or GetAndSet. | Yes |
| FormatName | The name of the data format. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| StandardFormat | The integer value of the data format. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | No |

## Remarks
Note that **FormatName** and **StandardFormat** are mutually exclusive attributes and are [Standard Clipboard Formats](https://msdn.microsoft.com/library/windows/desktop/ff729168.aspx).

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