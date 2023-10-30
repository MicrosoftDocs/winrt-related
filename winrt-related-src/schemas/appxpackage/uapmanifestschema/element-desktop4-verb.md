---
title: desktop4:Verb
description: Names and class IDs of the commands registered in the Shell for a file explorer context menu (desktop4:Verb).
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:Verb

Names and class IDs of the commands registered in the Shell for a file explorer context menu.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:Extension\>](element-desktop4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:FileExplorerContextMenus\>](element-desktop4-fileexplorercontextmenus.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:ItemType\>](element-desktop4-itemtype.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop4:Verb\>**

## Syntax

```xml
<desktop4:Verb
  Id = 'An alphanumeric string with a value from 3 to 64 characters in length.' 
  Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The name that appears in the File Explorer context menu. | An alphanumeric string with a value from 3 to 64 characters in length. | Yes |  |
| **Clsid** | The class ID of the app. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop4:ItemType](element-desktop4-itemtype.md) | Contains the type of command to be registered in the context menu. |

## Remarks

For more information about this element, see the remarks for [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |
