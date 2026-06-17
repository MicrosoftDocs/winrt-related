---
title: desktop10:Folder
description: Defines a folder to hold shortcuts, with localizable details.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:Folder]
---

# desktop10:Folder

Defines a folder to hold shortcuts, with localizable details.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:Folder>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:Folder>`**

## Syntax

```xml
<desktop10:Folder
  KnownFolder = 'A required string that can have one of the following values: "Common Programs", "Programs", or "Desktop".'
  RelativePath = 'An optional string that cannot contain these characters: <, >, |, ?, or *.'
  Name = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  Icon = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  IconIndex = 'An optional unsigned byte value.'
  Description = 'An optional string between 1 and 2048 characters in length.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **KnownFolder** |  The known folder to which the *RelativePath* value is relative.  | A string that can have one of the following values: *Common Programs*, *Programs*, *Desktop*. | Yes |  |
| **RelativePath** |  The path the folder, relative to the folder specified in *KnownFolder*  | An optional string that cannot contain these characters: <, >, &#124; , ?, or *. | No |  |
| **Name** |  The on-disk name of the folder.  | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **DisplayName** |  The display name for the folder.  | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **Icon** |  The icon image to show up for the lnk file, in [Multilingual User Interface](/windows/win32/intl/multilingual-user-interface) string format.  | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **IconIndex** |  The index of the icon within the current icon file.  | An optional unsigned byte value. | No |  |
| **Description** |  The description of the folder.  | An optional string between 1 and 2048 characters in length. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
