---

title: desktop5:ItemType
description: Contains the type of command to be registered in the context menu.

ms.date: 10/03/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop5:ItemType

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
<dd><b>&lt;desktop5:ItemType&gt;</b></dd>
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
<desktop5:ItemType Type = A string between 1 and 64 characters in length that meets one of the requirements specified in the attributes section below. >

  <!-- Child elements -->
  desktop5:Verb{0,10000}

</desktop5:ItemType>
```

### Key
`{}`   specific range of occurrences

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Type | The file type to associate the context menu handler with. | A string between 1 and 64 characters in length. The following string formats are supported:<ul><li>A string that begins with a period ("."), has no additional periods, and does not contain these characters: <, >, :, ", /, \, &#124;, ?.</li><li>A string that contains the wildcard `*` character.</li><li>The strings `Directory` or `Directory\Background`.</li> | Yes |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop5:Verb](element-desktop4-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |  

## See Also
[Creating a Shell Extension Handler](/windows/win32/shell/handlers)

## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/5` |