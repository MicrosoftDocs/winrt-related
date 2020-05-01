---

title: desktop4:Verb
description: Names and class IDs of the commands registered in the Shell for a file explorer context menu.

ms.date: 04/10/2018
ms.topic: reference


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

## Remarks

For more information about this element, see the remarks for [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md).

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |