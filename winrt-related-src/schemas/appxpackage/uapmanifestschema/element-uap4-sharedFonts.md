---

ms.assetid: e33e1624-e994-4b74-9d27-acb7d45db2b8
title: uap4:SharedFonts
description: Contains the locations of shared fonts to be used with the app. 

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:SharedFonts

## Description
Contains the locations of shared fonts to be used with the app. 

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
<uap4:SharedFonts>
  <!-- Child elements -->
  uap4:Font
</uap4:SharedFonts>
```


## Child Elements
| Child Element | Description |
|---------------|-------------|
| [Font](element-uap4-font.md) | Specifies the shared fonts. |

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