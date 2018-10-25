---
author: laurenhughes
ms.assetid: ddc64ab8-4c79-4034-ab23-476053c7dbb3
title: uap4:InputTypes
description: Contains the media codec input types.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:InputTypes

## Description
Contains the media codec input types.

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
<dd><b>&lt;uap4:InputTypes&gt;</b></dd>
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
<uap4:InputTypes>
  <!-- Child elements -->
  uap4:InputType{1,1000}
</uap4:InputTypes>                   
```

### Key
`{}` specific range of occurrences


| Child Element | Description |
|---------------|-------------|
| [InputType](element-uap4-inputtype.md) | The media codec input type. |


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