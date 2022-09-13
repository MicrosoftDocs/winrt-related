---
title: desktop4:FileExplorerContextMenus
description: Registers items for the context menu of File Explorer.
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:FileExplorerContextMenus

Registers items for the context menu of File Explorer.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:Extension\>](element-desktop4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop4:FileExplorerContextMenus\>**

## Syntax

```xml
<desktop4:FileExplorerContextMenus>
    desktop4:ItemType{0,10000}
    desktop5:ItemType{0,10000}
</desktop4:FileExplorerContextMenus>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop4:ItemType](element-desktop4-itemtype.md) (Windows 10, version 1803) | Contains the type of command to be registered in the context menu. |  
| [desktop5:ItemType](element-desktop5-itemtype.md) (Windows 10, version 1809 and later) | Contains the type of command to be registered in the context menu. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop4:Extension](element-desktop4-extension.md) | Declares an extensibility point for the app. |

## Remarks

Use this element to register a [context menu handler](/windows/desktop/shell/context-menu-handlers) that is implemented by your desktop application. For more information about how to use this element to register a context menu handler in a packaged desktop application, see [Specify a context menu handler for a file type](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#context-menu).

For a code sample that demonstrates how to implement a context menu handler by implementing the [IExplorerCommand](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) and [IExplorerCommandState](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate) interfaces, see the [ExplorerCommandVerb](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/ExplorerCommandVerb) code sample.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
