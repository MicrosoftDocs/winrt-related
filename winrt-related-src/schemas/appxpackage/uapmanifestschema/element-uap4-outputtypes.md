---
author: laurenhughes
ms.assetid: 8130088d-c1f1-4f36-ad7e-96e2f1897fdc
title: uap4:OutputTypes
description: Contains the media codec output types.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:OutputTypes

## Description
Contains the media codec output types.

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
<dd>
<dl>
<dt><a href="element-uap4-mediacodec.md">&lt;uap4:MediaCodec&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap4-MediaEncodingProperties.md">&lt;uap4:MediaEncodingProperties&gt;</a></dt>
<dd><b>&lt;uap4:OutputTypes&gt;</b></dd>
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
<uap4:OutputTypes>
  <!-- Child elements -->
  uap4:OutputType{1,1000}
</uap4:OutputTypes>                   
```

### Key
`{}` specific range of occurrences


| Child Element | Description |
|---------------|-------------|
| [OutputType](element-uap4-OutputType.md) | The media codec output type. |

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