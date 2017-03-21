---
author: laurenhughes
ms.assetid: 14552b44-db78-47f8-9f45-4021d82f1d74
title: com:ImplementedCategories (in ExeServer/Class)
description: Specifies categories implemented by the class.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---

# com:ImplementedCategories (in ExeServer/Class)

## -description
Specifies categories implemented by the class.

## -element-hierarchy
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
<dd><b>&lt;com:ImplementedCategories&gt;</b></dd>
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


## -syntax
```syntax
<com:ImplementedCategories>  
  <!-- Child elements -->
  ImplementedCategory{1,1000}
</com:ImplementedCategories>
```

## -key
`{}`   specific range of occurrences 

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [ImplementedCategory](element-com-exe-implementedcategory.md) | Indicates that the class has implemented the specified category. |

## -remarks

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
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>