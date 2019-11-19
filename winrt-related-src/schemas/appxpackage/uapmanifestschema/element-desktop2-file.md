---
author: mcleanbyron
ms.assetid: 314cfaee-840a-4e05-92c9-b8c635c22e72
title: desktop2:File
description: Specifies the path to an event message file.
ms.author: mcleans
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:File

## Description
Specifies the path to an event message file.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-package-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-DesktopEventLogging.md">&lt;desktop2:DesktopEventLogging&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-EventMessageFiles.md">&lt;desktop2:EventMessageFiles&gt;</a></dt>
<dd><b>&lt;desktop2:File&gt;</b></dd>
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
<desktop2:File Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | The path to an event message file. | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | Yes |


## Requirements

|||
|-|-|
|Namespace|`http://schemas.microsoft.com/appx/manifest/desktop/windows10/2`|