---

ms.assetid: 506e7441-56a8-4c5c-994d-5c070a7eab0b 
title: File (Required\ContentGroup)
description: The files specified in the required content group.

ms.date: 03/29/2017
ms.topic: article


keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# File (Required\ContentGroup)

## Description
The files specified in the required content group.

## Element Hierarchy
<dl>
<dt><a href="element-source-contentgroupmap.md">&lt;ContentGroupMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-source-required.md">&lt;Required&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-source-required-contentgroup.md">&lt;ContentGroup&gt;</a></dt>
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
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2016/sourcecontentgroupmap</p></td>
</tr>
</tbody>
</table>