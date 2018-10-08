---
author: laurenhughes
title: uap7:SharedFonts
description: Contains the locations of shared fonts to be used with the app.
ms.author: lahugh
ms.date: 10/03/2018
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap7:SharedFonts

## Description
Contains the locations of shared fonts to be used with the app.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap7-extension.md">&lt;uap7:Extension&gt;</a></dt>
<dd><b>&lt;uap7:SharedFonts&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<uap7:SharedFonts >

 <!-- Child elements -->
 uap4:Font

</uap7:SharedFonts>
```

## Attrbutes and Elements

### Attributes
None

### Child Elements
| Child Element | Description |
|---------------|-------------|
| uap4:Font | Specifies the font file packaged with the app. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/7</p></td>
</tr>
</tbody>
</table>