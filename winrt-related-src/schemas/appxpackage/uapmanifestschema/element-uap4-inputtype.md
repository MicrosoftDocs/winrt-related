---
author: mcleanbyron
ms.assetid: 5734c798-95d1-4028-a72a-33a0754aaba5
title: uap4:InputType
description: The media codec input type.
ms.author: mcleans
ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:InputType

## Description
The media codec input type.

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
<dd>
<dl>
<dt><a href="element-uap4-inputtypes.md">&lt;uap4:InputTypes&gt;</a></dt>
<dd><b>&lt;uap4:InputType&gt;</b></dd>
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
<uap4:InputType SubType            = Either a 4 character code or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. 
                uap6:CodecMimeType = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. />                 
```


## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| SubType | Either a GUID or a format type of the codec. | Either a 4 character code or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| uap6:CodecMimeType | The value of the "codecs" field within a MIME type. E.g., the value "hvc1" within "video/mp4;codecs='hvc1'" | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |


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