---

ms.assetid: fbdc96ec-04e1-4a64-9549-fd79f1e318d8
title: uap4:OutputType
description: The media codec output type.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:OutputType

## Description
The media codec output type.

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
<dt><a href="element-uap4-outputtypes.md">&lt;uap4:OutputTypes&gt;</a></dt>
<dd><b>&lt;uap4:OutputType&gt;</b></dd>
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
<uap4:OutputType SubType = Either a 4 character code or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >                 
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| SubType | Either a GUID or a format type of the codec. | Either a 4 character code or a GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

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