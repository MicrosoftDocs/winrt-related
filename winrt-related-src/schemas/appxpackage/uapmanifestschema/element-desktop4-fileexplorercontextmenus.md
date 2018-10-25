---
author: laurenhughes
title: desktop4:FileExplorerContextMenus
description: Registers items for the context menu of File Explorer.
ms.author: lahugh
ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:FileExplorerContextMenus

## Description
Registers items for the context menu of File Explorer.

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
<dt><a href="element-desktop4-extension.md">&lt;desktop4:Extension&gt;</a></dt>
<dd><b>&lt;desktop4:FileExplorerContextMenus&gt;</b></dd>
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
<desktop4:FileExplorerContextMenus>
    desktop4:ItemType{0,10000}
</desktop4:FileExplorerContextMenus>
```

### Key
`{}` specific range of occurrences


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop4:ItemType](element-desktop4-itemtype.md) | Contains the type of command to be registered in the context menu. |  

## See Also
[Creating a Shell Extension Handler](https://msdn.microsoft.com/library/windows/desktop/cc144067.aspx)


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/4</p></td>
</tr>
</tbody>
</table>