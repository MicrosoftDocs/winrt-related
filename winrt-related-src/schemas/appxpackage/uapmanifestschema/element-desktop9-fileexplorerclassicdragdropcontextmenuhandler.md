---
title: desktop9:FileExplorerClassicDragDropContextMenuHandler
description: Registers a legacy IContextMenu implementation of a drag and drop handler shell extension for a packaged desktop app.
ms.date: 09/17/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop9:FileExplorerClassicDragDropContextMenuHandler

Registers a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a drag and drop handler shell extension for a packaged desktop app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop9:Extension\>](element-desktop9-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop9:FileExplorerClassicDragDropContextMenuHandler\>**

## Syntax

```xml
<desktop9:FileExplorerClassicDragDropContextMenuHandler>

    desktop9:ExtensionHandler{0,1000}

</desktop9:FileExplorerClassicDragDropContextMenuHandler>
```

### Key

`{}` A specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop9:ExtensionHandler](element-desktop9-extensionhandler.md) | Specifies a handler for a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a context menu handler shell extension for a packaged desktop app. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop9:Extenson](element-desktop9-extension.md) | Declares an extensibility point for the app. |

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
<xmlns:desktop9="http://schemas.microsoft.com/appx/manifest/desktop/windows10/9">
```

The AppXManifest file must have the dependency MaxTested set to at least version 10.0.21300.0. Support for OS builds starting with the minimum version of 10.0.21300.0.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/9` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22159) |
