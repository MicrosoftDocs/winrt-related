---
title: uap10:MediaContentDecryptionModule
description: Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, uap10:Extension, uap10:MediaContentDecryptionModule]
---

# uap10:MediaContentDecryptionModule

Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:Extension>`](element-uap10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:MediaContentDecryptionModule>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap10:Extension>`](element-uap10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:MediaContentDecryptionModule>`**  

## Syntax

```xml
<uap10:MediaContentDecryptionModule
  DisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  Description = 'A required string between 1 and 2048 characters in length.'
  SupportedKeySystem = 'A required string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  wincap3:ActivatableClassId = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  wincap3:Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  wincap3:ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | A user-friendly display name for the media content. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Description** | A user-friendly description for the media content. | A string between 1 and 2048 characters in length. | Yes |  |
| **SupportedKeySystem** | Defines the key system used to encrypt/decrypt media content. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | Yes |  |
| **wincap3:ActivatableClassId** | The class ID associated with this media content. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **wincap3:Path** | The path to the media content. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | No |  |
| **wincap3:ProcessorArchitecture** | The processor architecture used for the media content. | An optional string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *neutral*. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **wincap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/windowscapabilities/3` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

> [!NOTE]
> The LIVE documentation previously listed this attribute as `SupportedKeySystems` (plural). The XSD schema defines it as `SupportedKeySystem` (singular), representing a single key system identifier per element instance.

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
