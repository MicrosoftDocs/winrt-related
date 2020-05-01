---

ms.assetid: cd39d56f-6e73-49c1-b5d1-df4e3d75471b 
title: File (Automatic\ContentGroup)
description: The files specified in the automatic content group.

ms.date: 03/29/2017
ms.topic: article


keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# File (Automatic\ContentGroup)

## Description
The files specified in the automatic content group.

## Element Hierarchy
<dl>
<dt><a href="element-source-contentgroupmap.md">&lt;ContentGroupMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-source-automatic.md">&lt;Automatic&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-source-automatic-contentgroup.md">&lt;ContentGroup&gt;</a></dt>
<dd><b>&lt;File&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<File Name = String type. >

</File>
```

## Key

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | File name. | String type. | Yes |


## Remarks
File names in the source content group map can use wildcards in names. For more information, see [Create and convert a source content group map](https://docs.microsoft.com/windows/uwp/packaging/create-cgm).

## Examples

## Requirements
|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2016/sourcecontentgroupmap` |