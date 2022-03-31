---
title: com4:Format
description: Specifies the file format an application can read from or write to. (com4:Format)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Format



## Description
Specifies the file format an application can read from or write to. 



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-class.md">&lt;com4:Class&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-conversion.md">&lt;com4:Conversion&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-readable.md">&lt;com4:Readable&gt;</a></dt>
<dd>
<b>&lt;com4:Format&gt;</b>
</dd>
</dl>
<dl><dt><a href = "element-com4-readwritable.md">&lt;com4:ReadWritable&gt;</a></dt>
<dd>
<b>&lt;com4:Format&gt;</b>
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
</dd>
</dl>

## Syntax
```syntax
<com4:Format     FormatName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    StandardFormat = A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).
></com4:Format>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| FormatName | The string file format name. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| StandardFormat | StandardFormat | A string in hexadecimal format containing numbers or the letters a, b, c, d, e, f (capital or lower case).| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
