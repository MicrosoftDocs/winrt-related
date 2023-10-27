---
title: UAP10:MediaContentDecryptionModule
description: Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# UAP10:MediaContentDecryptionModule

Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:Extension\>](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**<\uap10:MediaContentDecryptionModule\>**

## Syntax

```xml
<uap10:MedicaContentDecryptionModule
  DisplayName = 'A string with a value between 1 and 256 characters in length.'
  Description = 'A string with a value between 1 and 2048 characters in length.'
  SupportedKeySystems = 'A string with a value between 1 and 255 characters in length.'
  wincap3:ActivatableClassId = 'A string with a value between 1 and 255 characters in length.'
  wincap3:Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, ", |, ?, or *.'
  wincap3:ProcessorArchitecture = 'A string value that can be one of the following: "x86", "x64", "arm", "arm64", or "neutral".' />
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | A user-friendly display name for the media content. | A string with a value between 1 and 256 characters in length. | Yes |
| **Description** | A user-friendly description for the media content. | A string with a value between 1 and 2048 characters in length. | Yes |
| **SupportedKeySystems** | Defines the key systems used to encrypt/descrypt media content. | A string with a value between 1 and 255 characters in length. | Yes |
| **rescap3:ActivatableClassId** | The class ID associated with this media content. | A string with a value between 1 and 255 characters in length. | No |
| **rescap3:Path** | The path to the media content. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `"`, `|`, `?`, or `*`. | No |
| **rescap3:ProcessorArchitecture** | The processor architecture used for the media content. | A string value that can be one of the following: *x86*, *x64*, *arm*, *arm64*, or *neutral*. | No |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **rescap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/windowscapabilities/3` |
| Minimum OS Version | Windows 10 version 2004 (Build 19041) |
