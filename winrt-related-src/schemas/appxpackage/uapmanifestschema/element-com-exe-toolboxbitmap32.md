---

ms.assetid: 04d8934f-e032-4b10-b119-343c07364163
title: com:ToolboxBitmap32 (in ExeServer/Class)
description: Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:ToolboxBitmap32 (in ExeServer/Class)

## Description
Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.

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
<dd><b>&lt;com:ToolboxBitmap32&gt;</b></dd>
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
<com:ToolboxBitmap32
  Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
  ResourceId? = An integer type. >
</com:ToolboxBitmap32>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | The path to the bitmap. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |
| ResourceId | The resource ID of the bitmap. | An integer type. | No |

## Remarks

## Examples

## Requirements
|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |