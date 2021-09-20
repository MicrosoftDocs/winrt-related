---

ms.assetid: acf329e3-a99a-42db-8a2a-068eb9ffa28b
title: ContentGroup (Automatic\ContentGroup)
description: Specifies the automatic content group (Automatic\ContentGroup).

ms.date: 03/29/2017
ms.topic: article


keywords: windows 10, uwp, streaming install, content group, map, final content group, automatic content group
---

# ContentGroup (Automatic\ContentGroup)

## Description
Specifies the automatic content group.

## Element Hierarchy
<dl>
<dt><a href="element-source-contentgroupmap.md">&lt;ContentGroupMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-source-automatic.md">&lt;Automatic&gt;</a></dt>
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
| Name | Friendly name of the Content Group. | String type. | Yes |


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [File](element-source-automatic-file.md) | The files specified in the automatic content group. |

## Remarks
Automatic content group names must be unique.

> [!NOTE]
> Automatic content groups cannot be named "Required."

## Examples

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2016/sourcecontentgroupmap` |
