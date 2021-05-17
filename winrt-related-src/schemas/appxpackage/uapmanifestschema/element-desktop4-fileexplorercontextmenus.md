---

title: desktop4:FileExplorerContextMenus
description: Registers items for the context menu of File Explorer.

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
    desktop5:ItemType{0,10000}
</desktop4:FileExplorerContextMenus>
```

### Key
`{}` specific range of occurrences


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop4:ItemType](element-desktop4-itemtype.md) (Windows 10, version 1803) | Contains the type of command to be registered in the context menu. |  
| [desktop5:ItemType](element-desktop5-itemtype.md) (Windows 10, version 1809 and later) | Contains the type of command to be registered in the context menu. |  

## Remarks

Use this element to register a [context menu handler](/windows/desktop/shell/context-menu-handlers) that is implemented by your desktop application. For more information about how to use this element to register a context menu handler in a packaged desktop application, see [Specify a context menu handler for a file type](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#context-menu).

For a code sample that demonstrates how to implement a context menu handler by implementing the [IExplorerCommand](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) and [IExplorerCommandState](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate) interfaces, see the [ExplorerCommandVerb](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/ExplorerCommandVerb) code sample.

## Requirements

|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |