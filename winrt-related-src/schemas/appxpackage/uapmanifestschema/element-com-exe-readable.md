---

ms.assetid: 5f282cfa-4670-4989-8829-841842117e81
title: com:Readable (in ExeServer/Class)
description: Specifies that an application can only read files (in ExeServer/Class).

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:Readable (in ExeServer/Class)

## Description
Specifies that an application can only read files.

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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-comserver.md">&lt;com:ComServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver.md">&lt;com:ExeServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exeserver-class.md">&lt;com:Class&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-exe-conversion.md">&lt;com:Conversion&gt;</a></dt>
<dd><b>&lt;com:Readable&gt;</b></dd>
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
</dd>
</dl>



## Syntax
```syntax
<com:Readable> 
  <!-- Child elements -->
  Format
</com:Readable>
```

## Key

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Format](element-com-exe-rformat.md) | Specifies the file format an application can read (convert from). |

## Remarks

## Examples

## Requirements
|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |