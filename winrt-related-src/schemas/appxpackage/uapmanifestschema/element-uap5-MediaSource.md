---
title: uap5:MediaSource
description: Specifies the media source and the app service that it exposes.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:MediaSource

Specifies the media source and the app service that it exposes.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:MediaSource\>**

## Syntax

```xml
<uap5:MediaSource
  DisplayName = 'An optional string with a value between 1 and 256 characters in length. This string is localizable.'
  Description = 'An optional string with a value between 1 and 2048 characters in length.'
  AppServiceName  = 'A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.' >

  <!-- Child elements -->
  uap5:SupportedFileTypes
  uap5:SupportedContentTypes

</uap5:MediaSource>
```

### Key

`?`   optional (zero or one)

## Attrbutes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The media source display name. | An optional string with a value between 1 and 256 characters in length. This string is localizable. | No |
| **Description** | A brief description of the media source. | An optional string with a value between 1 and 2048 characters in length. | No |
| **AppServiceName** | The name of the app service exposed by the media source. Note that an app service is required for a media source. | A string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | Yes |

### Child elements

| Child element | Description |
|-|-|
| [SupportedFileTypes](element-uap5-SupportedFileTypes.md) | Contains the file types supported by the media source. |
| [SupportedContentTypes](element-uap5-SupportedContentTypes.md) | Contains the media/content types supported by the media source. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
