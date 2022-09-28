---
title: desktop5:ItemType
description: Contains the type of command to be registered in the context menu (desktop5:ItemType).
ms.date: 10/03/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop5:ItemType

Contains the type of command to be registered in the context menu.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:Extension\>](element-desktop4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:FileExplorerContextMenus\>](element-desktop4-fileexplorercontextmenus.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop5:ItemType\>**

## Syntax

```xml
<desktop5:ItemType
  Type = 'A string with a value between 1 and 64 characters in length that meets one of the requirements specified in the attributes section below.' >

  <!-- Child elements -->
  desktop5:Verb{0,10000}

</desktop5:ItemType>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The file type to associate the context menu handler with. | A string between 1 and 64 characters in length. The following string formats are supported: A.) A string that begins with a period (`.`), has no additional periods, and does not contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, or `?`, B.) A string that contains the wildcard `*` character, or C.) The string values `Directory` or `Directory\Background`. | Yes |  |

### Child elements

| Child element | Description |
|---------------|-------------|
| [desktop5:Verb](element-desktop4-verb.md) | Names and class IDs of the commands registered in the Shell for a file explorer context menu. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md) | Registers items for the context menu of File Explorer. |

## See Also

[Creating a Shell Extension Handler](/windows/win32/shell/handlers)

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/5` |
