---
title: desktop10:DataShortcut
description: Creates a shortcut to a file that is not an executable.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:DataShortcut

## Description

Creates a shortcut to a file that is not an executable.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-datashortcuts.md">&lt;desktop10:DataShortcuts&gt;</a></dt>
<dd><strong>&lt;desktop10:DataShortcut&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:DataShortcut
  Path              = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  WorkingDirectory? = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  WindowOption?     = A string value that can be one of the following: "minimized", "maximized", or "normal".
  Comment?          = A string value between 1 and 2048 characters.
  DisplayName       = An alphanumeric string value between 1 and 256 characters in length.
  Icon?             = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |;, ?, or *.
  IconIndex?        = A numerical value between 0 and 255.
  AUMID?            = A string value between 1 and 32767 characters that cannot begin or end with a whitespace character.
  >

</desktop10:DataShortcut>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| Path | The package-relative path to the file. | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |
| WorkingDirectory | The package-relative working directory. | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| WindowOption | Specifies whether the app should to start minimized, maximized, or normal.  Default is normal | A string value that can be one of the following: "minimized", "maximized", or "normal". | No |
| Comment | A comment for the shortcut. | A string value between 1 and 2048 characters. | No |
| DisplayName | The name to diosplay on the start menu. | An alphanumeric string value between 1 and 256 characters in length. | Yes |
| Icon | The icon image to show up for the lnk file, in [Multilingual User Interface](/windows/win32/intl/multilingual-user-interface) string format. If no icon is specified, the shell selects a default icon. | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| IconIndex | The index of the icon within the current icon file. | A numerical value between 0 and 255. | No |
| AUMID | The Application User Model ID (AUMID) associated with the shortcut. See Remarks for more information. | A string value between 1 and 32767 characters that cannot begin or end with a whitespace character. | No | 

### Child Elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:DataShortcuts](element-desktop10-datashortcuts.md) | Declares an extensibility point for the app. |

## Remarks

Apps that specify multiple data shortcuts should specifiy unique AUMID values for each one to make sure that all shortcuts are added to the start menu. The *AUMID* attribute allows you to specify a unique Application User Model ID (AUMID) value for each shortcut. If multiple shortcuts are specified in the extension and no AUMID is specified, the shell may use the same auto-generated AUMID for all shortcuts in the extension overwriting the provided shortcuts with a single lnk file. 

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |