---

title: desktop5:Verb
description: Names and class IDs of the commands registered in the Shell for a file explorer context menu (desktop5:Verb).

ms.date: 10/03/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop5:Verb

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
<dt><a href="element-desktop5-itemtype.md">&lt;desktop5:ItemType&gt;</a></dt>
<dd><b>&lt;desktop5:Verb&gt;</b></dd>
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
<desktop5:Verb Id    = An alphanumeric string from 3 to 64 characters in length. 
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
[Creating a Shell Extension Handler](/windows/win32/shell/handlers)

## Requirements

|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/5` |