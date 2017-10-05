---
author: laurenhughes
title: uap5:ContentType
description: Specifies the media/content type supported by the media source. 
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:ContentType

## Description
Specifies the media/content type supported by the media source. 

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
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-mediasource.md">&lt;uap5:MediaSource&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-SupportedContentTypes.md">&lt;uap5:SupportedContentTypes&gt;</a></dt>
<dd><b>&lt;uap5:ContentType&gt;</b></dd>
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
<uap5:ContentType SubType = A string that contains two components between 1 and 127 characters in length, separated by a forward slash ("/"). It follows the RFC 4288 naming requirements. />
```

### Key

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| SubType | The name of a subtype. | A string that contains two components between 1 and 127 characters in length, separated by a forward slash ("/"). It follows the RFC 4288 naming requirements. | Yes | 

### Child Elements
None

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>