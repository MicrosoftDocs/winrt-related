---

ms.assetid: deb7031e-075c-4f41-b8d9-87e64c30b588 
title: ContentGroup (Required\ContentGroup)
description: Specifies the required content group.

ms.date: 03/29/2017
ms.topic: article


keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# ContentGroup (Required\ContentGroup)

## Description
Specifies the required content group.

## Element Hierarchy
<dl>
<dt><a href="element-source-contentgroupmap.md">&lt;ContentGroupMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-source-required.md">&lt;Required&gt;</a></dt>
<dd><b>&lt;ContentGroup&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<ContentGroup Name = String type. >

  <!-- Child elements -->
  File{1,2147483647}
</ContentGroup>
```

## Key
`{}`   specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | Friendly name of the Content Group. This name must be set to: Required. | String type. | Yes |


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [File](element-source-required-file.md) | The files specified in the required content group. |

## Remarks
The **Name** of the required content group must be set to: Required, note that this value is case sensitive.

> [!NOTE]
> Automatic content groups cannot be named "Required."

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