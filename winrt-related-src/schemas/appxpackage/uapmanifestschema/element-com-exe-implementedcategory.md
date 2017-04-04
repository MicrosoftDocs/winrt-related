---
author: laurenhughes
ms.assetid: 53e347fc-d43e-4585-9499-06a132e86d0c
title: com:ImplementedCategory (in ExeServer/Class)
description: Indicates that the class has implemented the specified category.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:ImplementedCategory (in ExeServer/Class)

## Description
Indicates that the class has implemented the specified category.

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
<dt><a href="element-com-exe-implementedcategories.md">&lt;com:ImplementedCategories&gt;</a></dt>
<dd><b>&lt;com:ImplementedCategory&gt;</b></dd>
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
<com:ImplementedCategory
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >
</com:ImplementedCategory>
```

## Key

## Attributes 

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The ID of the COM category that is implemented. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Remarks

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
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>