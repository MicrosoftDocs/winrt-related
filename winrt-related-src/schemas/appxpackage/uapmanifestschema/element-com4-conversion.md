---
title: com4:Conversion
description: Specifies the formats an application can read and write. (com4:Conversion)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Conversion



## Description
Specifies the formats an application can read and write.



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
<b>&lt;com4:Conversion&gt;</b>
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
<com4:Conversion>
<!-- Child elements -->
  Readable
  ReadWritable
</com4:Conversion>
```




## Child Elements

| Element | Description |
| -----------| -------------|
| [Readable](element-com4-readable.md) | Specifies that the application can only read files. |
| [ReadWritable](element-com4-readwritable.md) | Specifies that the application can read and write files. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
