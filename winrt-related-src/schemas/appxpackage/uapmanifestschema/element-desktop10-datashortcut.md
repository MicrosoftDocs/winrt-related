---
title: desktop10:DataShortcut
description: Creates a shortcut to a file that is not an executable.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:DataShortcuts, desktop10:DataShortcut]
---

# desktop10:DataShortcut

Creates a shortcut to a file that is not an executable.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:DataShortcuts>`](element-desktop10-datashortcuts.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:DataShortcut>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:DataShortcuts>`](element-desktop10-datashortcuts.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:DataShortcut>`**  

## Syntax

```xml
<desktop10:DataShortcut
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  WorkingDirectory = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  WindowOption = 'An optional string that can have one of the following values: "minimized", "maximized", or "normal".'
  Comment = 'An optional string between 1 and 2048 characters in length.'
  DisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  Icon = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  IconIndex = 'An optional unsigned byte value.'
  AUMID = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The package-relative path to the file. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
| **WorkingDirectory** | The package-relative working directory. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **WindowOption** | Specifies whether the app should to start minimized, maximized, or normal. Default is normal. | An optional string that can have one of the following values: *minimized*, *maximized*, *normal*. | No |  |
| **Comment** | A comment for the shortcut. | An optional string between 1 and 2048 characters in length. | No |  |
| **DisplayName** | The name to display on the start menu. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Icon** | The icon image to show up for the lnk file, in [Multilingual User Interface](/windows/win32/intl/multilingual-user-interface) string format. If no icon is specified, the shell selects a default icon. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **IconIndex** | The index of the icon within the current icon file. | An optional unsigned byte value. | No |  |
| **AUMID** | The Application User Model ID (AUMID) associated with the shortcut. See Remarks for more information. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:DataShortcuts](element-desktop10-datashortcuts.md) | Specifies a list of non-executable shortcuts. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

Apps that specify multiple data shortcuts should specifiy unique AUMID values for each one to make sure that all shortcuts are added to the start menu. The *AUMID* attribute allows you to specify a unique Application User Model ID (AUMID) value for each shortcut. If multiple shortcuts are specified in the extension and no AUMID is specified, the shell may use the same auto-generated AUMID for all shortcuts in the extension overwriting the provided shortcuts with a single lnk file.

## Examples

<!-- Author content goes here -->
