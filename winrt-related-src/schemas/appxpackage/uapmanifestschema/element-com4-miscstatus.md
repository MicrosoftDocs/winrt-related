---
title: com4:MiscStatus
description: Specifies how to create and display an object. (com4:MiscStatus)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:MiscStatus



## Description
Specifies how to create and display an object.



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
<b>&lt;com4:MiscStatus&gt;</b>
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
<com4:MiscStatus     OleMiscFlag = An integer value in the range of 0-4194303.
>
<!-- Child elements -->
  Aspect
</com4:MiscStatus>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| OleMiscFlag | TBD | An integer value in the range of 0-4194303.| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Aspect](element-com4-aspect.md) | Specifies the desired data or view aspect of the object when drawing or getting data. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
