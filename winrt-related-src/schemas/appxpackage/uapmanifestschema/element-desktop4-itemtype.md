---
author: laurenhughes
title: desktop4:ItemType
description: Contains the type of command to be registered in the context menu.
ms.author: lahugh
ms.date: 04/10/2018
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:ItemType

## Description
Contains the type of command to be registered in the context menu.

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
<dd>
<dl>
<dt><a href="element-desktop4-fileexplorercontextmenus.md">&lt;desktop4:FileExplorerContextMenus&gt;</a></dt>
<dd><b>&lt;desktop4:ItemType&gt;</b></dd>
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
<desktop4:ItemType Type = A string between 1 and 64 characters in length that must begin with a period ("."), cannot have additional periods, and cannot contain these characters: &lt;, &gt;, :, ", /, \, |, ?. Can also be a wildcard "*" character. >

  <!-- Child elements -->
  desktop4:Verb{0,10000}

</desktop4:ItemType>
```

### Key
`{}`   specific range of occurrences

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Type | The file type to associate the context menu handler with. | A string between 1 and 64 characters in length that must begin with a period ("."), cannot have additional periods, and cannot contain these characters: <, >, :, ", /, \, &#124;, ?. Can also be a wildcard "*" character. | Yes |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop4:Verb](element-desktop4-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |  

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