---
title: desktop10:DataShortcut
description: Creates a shortcut to a file that is not an executable.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:DataShortcut

Creates a shortcut to a file that is not an executable.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:DataShortcuts\>](element-desktop10-datashortcuts.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:DataShortcut\>**

## Syntax

```xml
<desktop10:DataShortcut
  Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  WorkingDirectory = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  WindowOption = 'An optional string that can be one of the following values: "minimized", "maximized", or "normal".'
  Comment = 'An optional string with a value between 1 and 2048 characters.'
  DisplayName = 'An alphanumeric string with a value between 1 and 256 characters in length.'
  Icon = 'An optional string with a value between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.'
  IconIndex = 'An optional numerical value between 0 and 255.'
  AUMID = 'An optional string with a value between 1 and 32767 characters that cannot begin or end with a whitespace character.'
  uap10:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The package-relative path to the file. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **DisplayName** | The name to display on the start menu. | An alphanumeric string with a value between 1 and 256 characters in length. | Yes |  |
| **WorkingDirectory** | The package-relative working directory. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **WindowOption** | Specifies whether the app should to start minimized, maximized, or normal.  Default is normal | An optional string that can be one of the following values: *minimized*, *maximized*, or *normal*. | No |  |
| **Comment** | A comment for the shortcut. | An optional string with a value between 1 and 2048 characters. | No |  |
| **Icon** | The icon image to show up for the lnk file, in [Multilingual User Interface](/windows/win32/intl/multilingual-user-interface) string format. If no icon is specified, the shell selects a default icon. | An optional string with a value between 1 and 256 characters in length that  cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **IconIndex** | The index of the icon within the current icon file. | An optional numerical value between 0 and 255. | No |  |
| **AUMID** | The Application User Model ID (AUMID) associated with the shortcut. See Remarks for more information. |An optional string with a value between 1 and 32767 characters that cannot begin or end with a whitespace character. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:DataShortcuts](element-desktop10-datashortcuts.md) | Declares an extensibility point for the app. |

## Remarks

Apps that specify multiple data shortcuts should specifiy unique AUMID values for each one to make sure that all shortcuts are added to the start menu. The *AUMID* attribute allows you to specify a unique Application User Model ID (AUMID) value for each shortcut. If multiple shortcuts are specified in the extension and no AUMID is specified, the shell may use the same auto-generated AUMID for all shortcuts in the extension overwriting the provided shortcuts with a single lnk file.

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
