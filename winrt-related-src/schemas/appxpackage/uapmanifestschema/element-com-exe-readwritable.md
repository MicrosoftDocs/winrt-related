---

ms.assetid: 76085908-f9c0-4ca3-b3ae-c6cce4b1bd39
title: com:ReadWritable (in ExeServer/Class)
description: Specifies that an application can read and write files.

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:ReadWritable (in ExeServer/Class)

## Description
Specifies that an application can read and write files. 

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
<dd><b>&lt;com:ReadWritable&gt;</b></dd>
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
<com:ReadWritable> 
  <!-- Child elements -->
  Format
</com:ReadWritable>
```

## Key

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Format](element-com-exe-rwformat.md) | Specifies the file format an application can read and write (activate as). |

## Remarks

## Examples

## Requirements
|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |