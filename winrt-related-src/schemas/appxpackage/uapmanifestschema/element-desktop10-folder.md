---
title: desktop10:Folder
description: Defines a folder to hold shortcuts, with localizable details.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:Folder

## Description

Defines a folder to hold shortcuts, with localizable details.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd><strong>&lt;desktop10:Folder&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:Folder
  KnownFolder   = A string value that can be one of the following: "Common Programs", "Programs", or "Desktop".
  RelativePath? = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  Name?         = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  DisplayName?  = An alphanumeric string value between 1 and 256 characters in length. This string is localizable.
  Icon?         = A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", |, ?, or *.
  IconIndex?    = A numerical value between 0 and 255.
  Description?  = A string value between 1 and 2048 characters. This string is localizable.
  >

</desktop10:Folder>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| KnownFolder | The known folder to which the *RelativePath* value is relative. | A string value that can be one of the following: "Common Programs", "Programs", or "Desktop". | Yes |
| RelativePath | The path the folder, relative to the folder specified in *KnownFolder* | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| Name | The on-disk name of the folder. | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| DisplayName | The display name for the folder. | An alphanumeric string value between 1 and 256 characters in length. This string is localizable. | No |
| Icon | The icon image to show up for the lnk file, in [Multilingual User Interface](/windows/win32/intl/multilingual-user-interface) string format. | A string between 1 and 256 characters in length that  cannot contain these characters: <, >, :, ", &#124;, ?, or *.  | No |
| IconIndex | The index of the icon within the current icon file. | A numerical value between 0 and 255. | No |
| Description | The description of the folder. | A string value between 1 and 2048 characters. This string is localizable. | No |

### Child Elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |