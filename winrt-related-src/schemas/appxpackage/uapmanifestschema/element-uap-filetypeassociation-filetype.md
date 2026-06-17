---
title: uap:FileType (in FileTypeAssociation)
description: A supported file type specified as its file type extension (in uap:FileTypeAssociation/uap:SupportedFileTypes).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:FileTypeAssociation, uap:SupportedFileTypes, uap:FileType]
---

# uap:FileType (in FileTypeAssociation)

A supported file type specified as its file type extension.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:SupportedFileTypes>`](element-uap-filetypeassociation-supportedfiletypes.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:FileType>`**  

## Syntax

```xml
<uap:FileType
  ContentType = 'An optional string between 1 and 255 characters in length.'
  uap4:ShellNewFileName = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  uap4:ShellNewDisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  uap10:PerceivedType = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  uap10:ShellNewCommandParameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ContentType** | The type of the content. | An optional string between 1 and 255 characters in length. | No |  |
| **uap4:ShellNewFileName** | The file from the package to be copied to the location where the user initiated the Shell New command. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **uap4:ShellNewDisplayName** | The display name of the file type that shows when a user hovers over the "New" submenu in the Windows explorer. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **uap10:PerceivedType** | <!-- TODO: Add description --> | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **uap10:ShellNewCommandParameters** | <!-- TODO: Add description --> | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| **uap:SupportedFileTypes** | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **uap4** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also
The following elements have the same name as this one, but different content or attributes:

- [uap:FileType (type: ST_FileType)](element-uap-sharetarget-filetype.md)
