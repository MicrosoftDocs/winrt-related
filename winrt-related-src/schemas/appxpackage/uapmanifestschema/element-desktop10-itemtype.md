---
title: desktop10:ItemType
description: Associates packaged Shell context menu commands with file types, directories, drives, or the desktop background.
ms.date: 10/12/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop4:Extension, desktop4:FileExplorerContextMenus, desktop10:ItemType, desktop10:Verb]
---

# desktop10:ItemType

Associates packaged Shell context menu commands with a file type or another Shell context. This version adds support for the `Drive` and `DesktopBackground` values.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:Extension>`](element-desktop4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:FileExplorerContextMenus>`](element-desktop4-fileexplorercontextmenus.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:ItemType>`**

## Syntax

```xml
<desktop10:ItemType
  Type = 'A required string between 1 and 64 characters in length, as described below.' >

  desktop10:Verb{0,10000}

</desktop10:ItemType>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Type** | The file type or Shell context with which to associate the commands. | A string between 1 and 64 characters in length, without leading or trailing whitespace, in one of the formats listed below. | Yes | |

The following `Type` values are supported:

| Value | Context |
|-|-|
| A file extension, such as `.txt` | Files with that extension. The value begins with a period, has at least one character after the period, and contains no additional periods or backslashes. |
| `*` | All file types. |
| `Directory` | File system directory items. |
| `Directory\Background` | The background of a file system directory, rather than a selected item in that directory. |
| `Drive` | Drive items, such as the drive represented by `C:\`. |
| `DesktopBackground` | The desktop background, rather than a selected item on the desktop. |

## Child elements

| Child element | Description |
|-|-|
| [desktop10:Verb](element-desktop10-verb.md) | Identifies a command and its COM handler class. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop4:FileExplorerContextMenus](element-desktop4-fileexplorercontextmenus.md) | Registers items for the context menu of File Explorer. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11, version 22H2 (Build 22621) |

## Remarks

Declare this element inside an application-level `desktop4:Extension` with `Category="windows.fileExplorerContextMenus"`. Use `desktop10:Verb` children with `desktop10:ItemType`; the namespace of the enclosing extension remains desktop4.

Each verb's `Clsid` identifies a COM class that implements [IExplorerCommand](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iexplorercommand). Register that class in the package's COM server declaration. The manifest registration does not implement the command: the handler supplies its title, state, and action.

For the COM registration and packaging steps, see [Add a File Explorer context menu command to a packaged desktop app](/windows/apps/desktop/modernize/integrate-packaged-app-with-file-explorer). For the distinction between Shell registration contexts, see [Registering Shell Extension Handlers](/windows/win32/shell/reg-shell-exts).

## Examples

The following application-level extension registers the same handler for a drive's context menu and the desktop background's context menu. Declare the desktop4 and desktop10 namespaces in the manifest, and include them in `IgnorableNamespaces` as appropriate for the package's target OS versions.

```xml
<desktop4:Extension Category="windows.fileExplorerContextMenus">
  <desktop4:FileExplorerContextMenus>
    <desktop10:ItemType Type="Drive">
      <desktop10:Verb Id="ContosoDriveCommand"
                      Clsid="3f26f44f-15e0-4b8d-9f80-841c767e20f0" />
    </desktop10:ItemType>
    <desktop10:ItemType Type="DesktopBackground">
      <desktop10:Verb Id="ContosoDesktopCommand"
                      Clsid="3f26f44f-15e0-4b8d-9f80-841c767e20f0" />
    </desktop10:ItemType>
  </desktop4:FileExplorerContextMenus>
</desktop4:Extension>
```

The corresponding application-level COM declaration uses the same class ID. `ContosoContextMenu.dll` represents a handler DLL that must be supplied in the package; replace the example class ID and file name with those of your implementation.

```xml
<com:Extension Category="windows.comServer">
  <com:ComServer>
    <com:SurrogateServer DisplayName="Contoso context menu">
      <com:Class Id="3f26f44f-15e0-4b8d-9f80-841c767e20f0"
                 Path="ContosoContextMenu.dll"
                 ThreadingModel="STA" />
    </com:SurrogateServer>
  </com:ComServer>
</com:Extension>
```
