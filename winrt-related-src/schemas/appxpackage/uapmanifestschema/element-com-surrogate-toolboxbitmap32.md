---
author: laurenhughes
ms.assetid: 7f73aea2-6b7e-4c78-ba9b-74e574370a58
title: com:ToolboxBitmap32 (in SurrogateServer/Class)
description: Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---


# com:ToolboxBitmap32 (in SurrogateServer/Class)

## -description
Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.

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
<dt><a href="element-com-surrogateserver.md">&lt;com:SurrogateServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogateserver-class.md">&lt;com:Class&gt;</a></dt>
<dd><b>&lt;com:ToolboxBitmap32&gt;</b></dd>
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
<com:ToolboxBitmap32
  Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
  ResourceId? = An integer type. >
</com:ToolboxBitmap32>
```

## -key
`?`    optional (zero or one) 

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | The path to the bitmap. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |
| ResourceId | The resource ID of the bitmap. | An integer type. | No |

## -remarks

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