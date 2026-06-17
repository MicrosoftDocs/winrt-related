---
title: desktop4:FileExplorerContextMenus
description: Registers items for the context menu of File Explorer.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop4:Extension, desktop4:FileExplorerContextMenus]
---

# desktop4:FileExplorerContextMenus

Registers items for the context menu of File Explorer.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:Extension>`](element-desktop4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop4:FileExplorerContextMenus>`**

## Syntax

```xml
<desktop4:FileExplorerContextMenus>

  <!-- Child elements -->
  desktop4:ItemType{0,10000}
  desktop4:ItemType{0,10000}
  desktop4:ItemType{0,10000}

</desktop4:FileExplorerContextMenus>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop4:ItemType](element-desktop4-itemtype.md) | Contains the type of command to be registered in the context menu. |
| [desktop5:ItemType](element-desktop5-itemtype.md) | Contains the type of command to be registered in the context menu. |
| **desktop10:ItemType** | Contains the type of command to be registered in the context menu. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop4:Extension](element-desktop4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

Use this element to register a [context menu handler](/windows/desktop/shell/context-menu-handlers) that is implemented by your desktop application. For more information about how to use this element to register a context menu handler in a packaged desktop application, see [Specify a context menu handler for a file type](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#context-menu).

For a code sample that demonstrates how to implement a context menu handler by implementing the [IExplorerCommand](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) and [IExplorerCommandState](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate) interfaces, see the [ExplorerCommandVerb](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/ExplorerCommandVerb) code sample.

## Examples

<!-- Author content goes here -->
