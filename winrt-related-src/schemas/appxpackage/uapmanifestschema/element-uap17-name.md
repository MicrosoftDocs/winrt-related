---
title: uap17:Name
description: Specifies the name of an extension category that can be hosted by a PackageExtensionHost. 
ms.date: 10/12/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# uap17:Name



## Description

Specifies the name of an extension category that can be hosted by a [PackageExtensionHost](element-uap17-packageextensionhost.md). 



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-uap17-extension.md">&lt;uap17:Extension&gt;</a></dt>
<dd>
<dl><dt><a href = "element-uap17-packageextensionhost.md">&lt;uap17:PackageExtensionHost&gt;</a></dt>
<dd>
<b>&lt;uap17:Name&gt;</b>
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
<uap17:Name>A string with a value between 2 and 255 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.
</uap17:Name>
```





## Requirements

| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| uap17 | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
