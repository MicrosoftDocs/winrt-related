---
title: desktop7:Shortcut
description: Creates a shortcut to a file.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:Shortcut]
---

# desktop7:Shortcut

Creates a shortcut to a file.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:Shortcut>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:Shortcut>`**

## Syntax

```xml
<desktop7:Shortcut
  File = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  Icon = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  Arguments = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  PinToStartMenu = 'An optional boolean value.'
  ExcludeFromShowInNewInstall = 'An optional boolean value.'
  Description = 'An optional string between 1 and 2048 characters in length.'
  desktop10:DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  desktop10:Description = 'An optional string between 1 and 2048 characters in length.' >

  <!-- Child elements -->
  desktop7:AppMigrations?

</desktop7:Shortcut>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **File** | The path to the file that is the target of the shortcut. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
| **Icon** | The path to the file that is the icon of the shortcut. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
| **Arguments** | Arguments to the shortcut. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **PinToStartMenu** | A boolean value specifying if the shortcut is pinned to the Start menu. | An optional boolean value. | No |  |
| **ExcludeFromShowInNewInstall** | A boolean value specifying if the shortcut should be excluded from the highlighting that is applied to newly installed apps. | An optional boolean value. | No |  |
| **Description** | The description of the shortcut. | An optional string between 1 and 2048 characters in length. | No |  |
| **desktop10:DisplayName** | The display name for the shortcut. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **desktop10:Description** | The localizable description for the shortcut. | An optional string between 1 and 2048 characters in length. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop7:AppMigrations](element-desktop7-appmigrations.md) | Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop7:Extension](element-desktop7-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

The *File* path format is a path relative to one of the following constants that resolve to a directory.

| Constant | Directory |
|----------|-----------|
| Common Programs | C:\ProgramData\Microsoft\Windows\Start Menu\Programs |
| Programs | C:\Users\\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs |
| Desktop | C:\Users\\<username>\Desktop |

So, for example the following value for *File* creates a shortcut with the path `C:\Users\<username>\Desktop\Shortcut.lnk`.

```xml
File="$(Desktop)\Shortcut.lnk"
```

## Examples

<!-- Author content goes here -->
