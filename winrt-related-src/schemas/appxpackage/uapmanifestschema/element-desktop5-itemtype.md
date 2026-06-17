---
title: desktop5:ItemType
description: Contains the type of command to be registered in the context menu (desktop5:ItemType).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop5:Extension, desktop5:FileExplorerContextMenus, desktop5:ItemType]
---

# desktop5:ItemType

Contains the type of command to be registered in the context menu.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop5:Extension>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop5:FileExplorerContextMenus>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop5:ItemType>`**

## Syntax

```xml
<desktop5:ItemType
  Type = 'A required value. <!-- TODO: Add description for desktop5:ST_FileTypeOrStarWithDirectory -->' >

  <!-- Child elements -->
  desktop5:Verb{0,10000}

</desktop5:ItemType>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The file type to associate the context menu handler with. | A value. <!-- TODO: Add data type for desktop5:ST_FileTypeOrStarWithDirectory --> | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop5:Verb](element-desktop5-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md) | Registers items for the context menu of File Explorer. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
