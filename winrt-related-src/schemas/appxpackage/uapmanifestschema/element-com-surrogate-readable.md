---
author: laurenhughes
ms.assetid: 066c1245-b3f1-4022-8f96-3bb1d7f6fbc0
title: com:Readable (in SurrogateServer/Class)
description: Specifies that an application can only read files.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---


# com:Readable (in SurrogateServer/Class)

## -description
Specifies that an application can only read files.

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
<dd>
<dl>
<dt><a href="element-com-surrogate-conversion.md">&lt;com:Conversion&gt;</a></dt>
<dd><b>&lt;com:Readable&gt;</b></dd>
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

## -syntax
```syntax
<com:Readable> 
  <!-- Child elements -->
  Format
</com:Readable>
```

## -key

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [Format](element-com-surrogate-rformat.md) | Specifies the file format an application can read (convert from). |

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