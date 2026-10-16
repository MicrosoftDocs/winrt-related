---
title: desktop10:Verb
description: Identifies a packaged Shell context menu command and its COM handler class.
ms.date: 10/12/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop4:Extension, desktop4:FileExplorerContextMenus, desktop10:ItemType, desktop10:Verb]
---

# desktop10:Verb

Identifies a packaged Shell context menu command and the COM class that handles it.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:Extension>`](element-desktop4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:FileExplorerContextMenus>`](element-desktop4-fileexplorercontextmenus.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:ItemType>`](element-desktop10-itemtype.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:Verb>`**

## Syntax

```xml
<desktop10:Verb
  Id = 'A required ASCII alphanumeric string between 3 and 64 characters in length.'
  Clsid = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The identifier for the command registration. This is not the displayed menu label. | A string of 3 to 64 characters consisting of `A` through `Z`, `a` through `z`, and `0` through `9`. | Yes | |
| **Clsid** | The class ID of the COM context menu handler. It must match the class ID in the handler's COM registration. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes | |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:ItemType](element-desktop10-itemtype.md) | Associates packaged Shell context menu commands with a file type or another Shell context. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11, version 22H2 (Build 22621) |

## Remarks

The COM handler implements [IExplorerCommand](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iexplorercommand). The Shell obtains the displayed command label from [IExplorerCommand::GetTitle](/windows/win32/api/shobjidl_core/nf-shobjidl_core-iexplorercommand-gettitle), rather than displaying the manifest's `Id` attribute.

For a complete registration example, including the matching COM class, see [desktop10:ItemType](element-desktop10-itemtype.md#examples).

## Examples

This verb associates a command registration with its handler for drive items.

```xml
<desktop10:ItemType Type="Drive">
  <desktop10:Verb Id="ContosoDriveCommand"
                  Clsid="3f26f44f-15e0-4b8d-9f80-841c767e20f0" />
</desktop10:ItemType>
```
