---
title: uap10:FileType
description: A supported file type specified as its file type extension, with additional uap10 attributes (uap10:FileType).
ms.date: 06/17/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap10:Extension, uap10:FileTypeAssociation, uap10:SupportedFileTypes, uap10:FileType]
---

# uap10:FileType

A supported file type specified as its file type extension.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:SupportedFileTypes>`](element-uap-filetypeassociation-supportedfiletypes.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:FileType>`**  

## Syntax

```xml
<uap10:FileType
  ContentType = 'An optional string between 1 and 255 characters in length.'
  uap4:ShellNewFileName = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *.'
  uap4:ShellNewDisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  PerceivedType = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  ShellNewCommandParameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ContentType** | The type of the content. | An optional string between 1 and 255 characters in length. | No |  |
| **uap4:ShellNewFileName** | The file from the package to be copied to the location where the user initiated the Shell New command. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **uap4:ShellNewDisplayName** | The display name of the file type that shows when a user hovers over the "New" submenu in the Windows explorer. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **PerceivedType** | The perceived type of the file (such as "image", "video", "audio", or "document"). The Shell uses this value to group and treat files differently based on their type. For example, File Explorer may display thumbnail images for files with a perceived type of "image". | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **ShellNewCommandParameters** | A parameter string to pass to the app when the user creates a new file of this type using the Shell New command (for example, from the "New" context menu in File Explorer). This attribute is mutually exclusive with **uap4:ShellNewFileName** — only one can be specified per FileType element. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:SupportedFileTypes](element-uap-filetypeassociation-supportedfiletypes.md) | Defines the file types associated with the app. They are unique per package and are case sensitive. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **uap4** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
