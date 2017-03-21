---
author: laurenhughes
ms.assetid: 6bca24cd-9433-4cbd-a701-9356f0a4b418
title: com:DataFormats (in ExeServer/Class)
description: Specifies the default and main data formats supported by an application.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---

# com:DataFormats (in ExeServer/Class)

## -description
Specifies the default and main data formats supported by an application.

## -element-hierarchy
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

## -syntax
```syntax
<com:DataFormats
  DefaultFormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
  DefaultStandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). >

  <!-- Child elements -->
  DataFormat{0,1000}
</com:DataFormats>
```

## -key
`{}`   specific range of occurrences 

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DefaultFormatName | The string value of the format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| DefaultStandardFormat | The hexadecimal value of the format name. | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case). | Yes |

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [DataFormat](element-com-exe-dataformat.md) | The data format supported by an application. |

## -remarks
**DefaultFormatName** is the string value, and **DefaultStandardFormat** is the integer value of the supported data formats. These values are mutually exclusive.

This element corresponds to the [DataFormats](https://msdn.microsoft.com/library/windows/desktop/ms678525.aspx) subkey.

## -examples

## -requirements
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