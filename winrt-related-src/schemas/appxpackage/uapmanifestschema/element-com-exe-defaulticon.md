---
author: mcleanbyron
ms.assetid: 3c95a0bb-546f-4b73-8194-eb491af54a8b
title: com:DefaultIcon (in ExeServer/Class)
description: Provides default icon information for iconic presentations of objects.
ms.author: mcleans
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:DefaultIcon (in ExeServer/Class)

## Description
Provides default icon information for iconic presentations of objects.

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
<dd><b>&lt;com:DefaultIcon&gt;</b></dd>
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
<com:DefaultIcon
  Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
  ResourceIndex? = An integer type. >
</com:DefaultIcon>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | The full path to the executable name of the server application. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |
| ResourceIndex | The integer at the end of the path, separated from the path by a comma, e.g., C:\Foo\Bar\Baz.exe,5. See the nIconIndex parameter in [ExtractIcon](https://msdn.microsoft.com/library/windows/desktop/ms648068.aspx) for more details. | An integer type. | No |

## Remarks

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