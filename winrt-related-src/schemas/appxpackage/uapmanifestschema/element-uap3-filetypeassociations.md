---
title: uap3:FileTypeAssociations
description: Defines the types of files used within the application.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:FileTypeAssociations

Defines the types of files used within the application.

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:FileTypeAssociations\>**

## Syntax

```xml
<uap3:FileTypeAssociations
  Parameters = 'An optional string with a value between 1 and 32767 characters.'
  MultiSelectModel = 'An optional string that can have one of the following values: "Player", "Document", or "Single".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Parameters** | Specifies parameters to define the types of files used in the application. | An optional string with a value between 1 and 32767 characters. | No |  |
| **MultiSelectModel** | Specifies the model used to define the types of files used in the application. | An optional string that can have one of the following values: *Player*, *Document*, or *Single*. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Sets parameters to define the protocol of the extensions. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| Minimum OS Version | Windows 10 version 1607 (Build 14393) |
