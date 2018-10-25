---
author: laurenhughes
ms.assetid: deb8e538-57e7-4b92-b121-6b2ea53f5094
title: uap4:MediaEncodingProperties
description: Contains the media coded input and output types.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:MediaEncodingProperties

## Description
Contains the media coded input and output types.

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
<dd><b>&lt;uap4:MediaEncodingProperties&gt;</b></dd>
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
<uap4:MediaEncodingProperties>
  <!-- Child elements -->
  uap4:InputTypes,
  uap4:OutputTypes
</uap4:MediaEncodingProperties>                   
```

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [InputTypes](element-uap4-inputtypes.md) | Contains the media codec input types. |
| [OutputTypes](element-uap4-outputtypes.md) | Contains the media codec output types. |


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