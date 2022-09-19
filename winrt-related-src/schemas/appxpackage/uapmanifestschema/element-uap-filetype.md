---
description: A supported file type specified as its file type extension (in uap:FileTypeAssociation/uap:SupportedFileTypes).
Search.Product: eADQiWindows 10XVcnh
title: uap:FileType (uap:FileTypeAssociation/uap:SupportedFileTypes)
ms.assetid: 9a872ee1-03fa-48f0-bc13-e35c7a22820e
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:FileType (in uap:FileTypeAssociation/uap:SupportedFileTypes) 

A supported file type specified as its file type extension.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:SupportedFileTypes\>](element-uap-supportedfiletypes.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:FileType\>**

## Syntax

```xml
<uap:FileType
  ContentType = 'An optional string with a value that contains two components between 1 and 127 characters in length, separated by a forward slash ("/"). It follows the RFC 4288 naming requirements.'
  uap4:ShellNewFileName = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  uap4:ShellNewDisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.' />
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ContentType** | The type of the content. | An optional string with a value that contains two components between 1 and 127 characters in length, separated by a forward slash (`/`). It follows the RFC 4288 naming requirements. | No |  |
| **uap4:ShellNewFileName** | The file from the package to be copied to the location where the user initiated the Shell New command. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **uap4:ShellNewDisplayName** | The display name of the file type that shows when a user hovers over the "New" submenu in the Windows explorer. | A string with a value between 1 and 256 characters in length. This string is localizable. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md) | Defines the file types associated with the app. They are unique per package and are case sensitive. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- [uap:FileType (type: ST_FileType)](element-1-uap-filetype.md)

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
