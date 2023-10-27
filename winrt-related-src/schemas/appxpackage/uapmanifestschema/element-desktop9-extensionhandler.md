---
title: desktop9:ExtensionHandler
description: Specifies a handler for a legacy IContextMenu implementation.
ms.date: 09/17/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop9:ExtensionHandler

Specifies a handler for a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a context menu handler shell extension for a packaged desktop app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop9:Extension\>](element-desktop9-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop9:FileExplorerClassicContextMenuHandler\>](element-desktop9-fileexplorerclassiccontextmenuhandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop9:ExtensionHandler\>**

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop9:FileExplorerClassicDragDropContextMenuHandler\>](element-desktop9-fileexplorerclassicdragdropcontextmenuhandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop9:ExtensionHandler\>**

## Syntax

```xml
<desktop9:ExtensionHandler
    Type = 'A string with a value between 1 and 64 characters in length with a non-whitespace character at its beginning and end.'
    Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The file type to associate the context menu handler with. | A string with a value between 1 and 64 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Clsid** | The CLSID of the COM server being registered. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop9:FileExplorerClassicContextMenuHandler](element-desktop9-fileexplorerclassiccontextmenuhandler.md) | Registers a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a context menu handler shell extension for a packaged desktop app. |
| [desktop9:FileExplorerClassicDragDropContextMenuHandler](element-desktop9-fileexplorerclassicdragdropcontextmenuhandler.md) | Registers a legacy [IContextMenu](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) implementation of a drag and drop handler shell extension for a packaged desktop app. |

## Remarks

Packaged desktop apps that use the legacy **IContextMenu** COM interface to implement a context menu shell extension should include this element in their package manifest file. For more information, see [Support legacy context menus for packaged apps](/windows/msix/packaging-tool/support-legacy-context-menus).

## Examples

The following example shows the usage of the **ExtensionHandler** element within a package manifest file to register a context menu shell extension.

```xml
<desktop9:Extension Category="windows.fileExplorerClassicContextMenuHandler">
    <desktop9:FileExplorerClassicContextMenuHandler>
        <desktop9:ExtensionHandler Type="*" Clsid="<GUID-for-the-com-server>" />
        <desktop9:ExtensionHandler Type=".txt" Clsid="<GUID-for-the-com-server>" />
        <desktop9:ExtensionHandler Type="Directory" Clsid="<GUID-for-the-com-server>" />
    </desktop9:FileExplorerClassicContextMenuHandler>
</desktop9:Extension>
```

This example assumes you have added the desktop9 xml namespace to your manifest file using the following syntax.

```xml
<xmlns:desktop9="http://schemas.microsoft.com/appx/manifest/desktop/windows10/9">
```

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/9` |
| Minimum OS Version | Windows 11 version 21H2 (Build 22159) |
