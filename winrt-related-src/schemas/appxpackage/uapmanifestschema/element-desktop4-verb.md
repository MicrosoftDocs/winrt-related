---
author: laurenhughes
title: desktop4:Verb
description: Names and class IDs of the commands registered in the Shell for a file explorer context menu.
ms.author: lahugh
ms.date: 04/10/2018
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:Verb

## Description
Names and class IDs of the commands registered in the Shell for a file explorer context menu.

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
<dd>
<dl>
<dt><a href="element-desktop4-itemtype.md">&lt;desktop4:ItemType&gt;</a></dt>
<dd><b>&lt;desktop4:Verb&gt;</b></dd>
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
<desktop4:Verb Id    = An alphanumeric string from 3 to 64 characters in length. 
               Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The name that appears in the File Explorer context menu. | An alphanumeric string from 3 to 64 characters in length. | Yes |
| Clsid | The class ID of the app. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Child Elements
None.

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