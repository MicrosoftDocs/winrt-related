---
title: desktop5:Verb
description: Names and class IDs of the commands registered in the Shell for a file explorer context menu (desktop5:Verb).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop5:Extension, desktop5:FileExplorerContextMenus, desktop5:ItemType, desktop5:Verb]
---

# desktop5:Verb

Names and class IDs of the commands registered in the Shell for a file explorer context menu.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop5:Extension>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop5:FileExplorerContextMenus>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop5:ItemType>`](element-desktop5-itemtype.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop5:Verb>`**

## Syntax

```xml
<desktop5:Verb
  Id = 'A required string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only.'
  Clsid = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The name that appears in the File Explorer context menu. | A string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only. | Yes |  |
| **Clsid** | The class ID of the app. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop4:ItemType](element-desktop4-itemtype.md) | Contains the type of command to be registered in the context menu. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
