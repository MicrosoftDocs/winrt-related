---
title: com4:ToolboxBitmap32
description: Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button. (com4:ToolboxBitmap32)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ToolboxBitmap32



## Description
Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.



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
<b>&lt;com4:ToolboxBitmap32&gt;</b>
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
<com4:ToolboxBitmap32     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ResourceId = A positive integer.
></com4:ToolboxBitmap32>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | The path to the bitmap.  | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| ResourceId | The resource ID of the bitmap. | A positive integer.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
