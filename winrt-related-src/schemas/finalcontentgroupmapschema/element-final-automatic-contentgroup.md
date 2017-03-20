---
author: laurenhughes
ms.assetid: 95db2dea-30af-4148-bd4f-9e47c64d8634  
title: ContentGroup
description: Specifies the automatic content group.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# ContentGroup

## -description
Specifies the automatic content group.

## -element-hierarchy
<dl>
<dt><a href="element-final-contentgroupmap.md">&lt;ContentGroupMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-final-automatic.md">&lt;Automatic&gt;</a></dt>
<dd><b>&lt;ContentGroup&gt;</b></dd>
</dl>
</dd>
</dl>

## -syntax
```syntax
<ContentGroup Name = String type. >

  <!-- Child elements -->
  File{1,2147483647}
</ContentGroup>
```

## -key
`{}`   specific range of occurrences

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | Friendly name of the Content Group. | String type. | Yes |


## -child-elements

| Child Element | Description |
|---------------|-------------|
| [File](element-final-automatic-file.md) | The files specified in the automatic content group. |

## -remarks
Automatic content group names must be unique.

> [!NOTE]
> Automatic content groups cannot be named "Required."

## -examples

## -requirements
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