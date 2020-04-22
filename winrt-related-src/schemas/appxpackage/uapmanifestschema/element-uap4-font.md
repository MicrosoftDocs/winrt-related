---

ms.assetid: aa161fac-a537-47df-90b7-8c8be8a63718
title: uap4:Font
description: Specifies the font file packaged with the app. 

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:Font

## Description
Specifies the font file packaged with the app.

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
<dt><a href="element-uap4-sharedfonts.md">&lt;uap4:SharedFonts&gt;</a></dt>
<dd><b>&lt;uap4:Font&gt;</b></dd>
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
<uap4:Font File =  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *./>
```
## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| File | The name of the font file, packaged with the app. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
