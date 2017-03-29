---
author: laurenhughes
ms.assetid: 4159e108-5b94-44d4-838d-6db1280a45ff 
title: File
description: The files specified in the automatic content group.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# File

## Description
The files specified in the automatic content group.

## Element Hierarchy
<dl>
<dt><a href="element-final-contentgroupmap.md">&lt;ContentGroupMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-final-automatic.md">&lt;Automatic&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-final-automatic-contentgroup.md">&lt;ContentGroup&gt;</a></dt>
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
File names in the final content group map cannot use wildcards. Note that wildcards can be used in the source content group map, which can be converted into a final content group map. For more information, see [Create and convert a source content group map](https://docs.microsoft.com/windows/uwp/packaging/create-cgm). 

## Examples

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2016/contentgroupmap</p></td>
</tr>
</tbody>
</table>