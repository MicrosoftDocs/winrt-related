---
title: desktop4:ItemType
description: Contains the type of command to be registered in the context menu (desktop4:ItemType).
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:ItemType

Contains the type of command to be registered in the context menu.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:Extension\>](element-desktop4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:FileExplorerContextMenus\>](element-desktop4-fileexplorercontextmenus.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop4:ItemType\>**

## Syntax

```xml
<desktop4:ItemType 
  Type = 'A string with a value between 1 and 64 characters in length that must begin with a period ("."), cannot have additional periods, and cannot contain these characters: <, >, :, ", /, \, |, ?. Can also be a wildcard "*" character.' >

  <!-- Child elements -->
  desktop4:Verb{0,10000}

</desktop4:ItemType>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| Type | The file type to associate the context menu handler with. | A string with a value between 1 and 64 characters in length that must begin with a period (`.`), cannot have additional periods, and cannot contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`. Can also be a wildcard `*` character. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop4:Verb](element-desktop4-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md) | Registers items for the context menu of File Explorer. |

## Remarks

For more information about this element, see the remarks for [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |
