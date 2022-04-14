---


title: desktop9:FileExplorerClassicDragDropContextMenuHandler
description: Registers a legacy IContextMenu implementation of a drag and drop handler shell extension for a packaged desktop app.

ms.date: 09/17/2021
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop9:FileExplorerClassicDragDropContextMenuHandler

## Description

Registers a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a drag and drop handler shell extension for a packaged desktop app.

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
<dt><a href="element-desktop9-extension.md">&lt;desktop9:Extension&gt;</a></dt>
<dd><b>&lt;desktop9:FileExplorerClassicDragDropContextMenuHandler&gt;</b></dd>
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
<desktop9:FileExplorerClassicDragDropContextMenuHandler>
    desktop9:ExtensionHandler{0,1000}
</desktop9:FileExplorerClassicDragDropContextMenuHandler>
```

### Key
`{}` A specific range of occurrences

## Attributes
None.

## Remarks

Packaged desktop apps that use the legacy **IContextMenu** COM interface to implement a drag and drop shell extension should include this element in their package manifest file. For more information, see [Support legacy context menus for packaged apps](/windows/msix/packaging-tool/support-legacy-context-menus).

## Examples 

The following example shows the usage of the **FileExplorerClassicDragDropContextMenuHandler** element within a package manifest file to register a drag and drop shell extension.

```xml
<desktop9:Extension Category="windows.fileExplorerClassicDragDropContextMenuHandler">
    <desktop9:FileExplorerClassicDragDropContextMenuHandler>
        <desktop9:ExtensionHandler Type="*" Clsid="<GUID-for-the-com-server>" />
        <desktop9:ExtensionHandler Type=".txt" Clsid="<GUID-for-the-com-server>" />
        <desktop9:ExtensionHandler Type="Directory" Clsid="<GUID-for-the-com-server>" />
    </desktop9:FileExplorerClassicDragDropContextMenuHandler>
</desktop9:Extension>
``` 

This example assumes you have added the desktop9 xml namespace to your manifest file using the following syntax.

```xml
xmlns:desktop9="http://schemas.microsoft.com/appx/manifest/desktop/windows10/9"
```

The AppXManifest file must have the dependency MaxTested set to as least version 10.0.21300.0. Support for OS builds starting with the minimum version of 10.0.21300.0.


## Requirements


| **Prefix**              |    **Namespace URL**                              |
|---------------|-------------------------------------------------------------|
| desktop9 | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/9`|