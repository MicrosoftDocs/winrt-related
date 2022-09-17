---
title: desktop10:Folder
description: Defines a folder to hold shortcuts, with localizable details.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:Folder

Defines a folder to hold shortcuts, with localizable details.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:Folder\>**

## Syntax

```xml
<desktop10:Folder
  KnownFolder = 'A string that can be one of the following values: "Common Programs", "Programs", or "Desktop".'
  RelativePath = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  Name = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  DisplayName = 'An optional alphanumeric string with a value between 1 and 256 characters in length. This string is localizable.'
  Icon = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  IconIndex = 'An optional numerical value between 0 and 255.'
  Description = 'An optional string with a value between 1 and 2048 characters. This string is localizable.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **KnownFolder** | The known folder to which the *RelativePath* value is relative. | A string that can be one of the following values: *Common Programs*, *Programs*, or *Desktop*. | Yes |  |
| **RelativePath** | The path the folder, relative to the folder specified in *KnownFolder* | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **Name** | The on-disk name of the folder. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **DisplayName** | The display name for the folder. | An optional alphanumeric string with a value between 1 and 256 characters in length. This string is localizable. | No |  |
| **Icon** | The icon image to show up for the lnk file, in [Multilingual User Interface](/windows/win32/intl/multilingual-user-interface) string format. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`.  | No |  |
| **IconIndex** | The index of the icon within the current icon file. | A numerical value between 0 and 255. | No |  |
| **Description** | The description of the folder. | An optional string with a value between 1 and 2048 characters. This string is localizable. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
