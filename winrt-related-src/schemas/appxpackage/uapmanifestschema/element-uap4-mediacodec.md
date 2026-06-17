---
title: uap4:MediaCodec
description: Defines an extension that enables an app to install media codecs from the Microsoft Store.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap4:Extension, uap4:MediaCodec]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap4:MediaCodec

Defines an extension that enables an app to install media codecs from the Microsoft Store.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:Extension>`](element-uap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:MediaCodec>`**

## Syntax

```xml
<uap4:MediaCodec
  DisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  Description = 'A required string between 1 and 2048 characters in length.'
  Category = 'A required string that can have one of the following values: "audioDecoder", "audioEncoder", "videoDecoder", or "videoEncoder".'
  AppServiceName = 'An optional string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  wincap3:ActivatableClassId = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  wincap3:Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  wincap3:ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".'
  mc:CodecType = 'An optional string that can have one of the following values: "software", or "hardware".' >

  <!-- Child elements -->
  uap4:MediaEncodingProperties

</uap4:MediaCodec>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The friendly name of the codec. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Description** | A description of the codec. | A string between 1 and 2048 characters in length. | Yes |  |
| **Category** | The type of extension. | A string that can have one of the following values: *audioDecoder*, *audioEncoder*, *videoDecoder*, *videoEncoder*. | Yes |  |
| **AppServiceName** | The app service that is launched as the codec. | An optional string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | No |  |
| **wincap3:ActivatableClassId** | The class ID associated with this media content. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **wincap3:Path** | The path to the media content. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | No |  |
| **wincap3:ProcessorArchitecture** | The processor architecture used for the media content. | An optional string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *neutral*. | No |  |
| **mc:CodecType** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *software*, *hardware*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap4:MediaEncodingProperties](element-uap4-mediaencodingproperties.md) | Contains the media coded input and output types. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **mc** | `http://schemas.microsoft.com/appx/manifest/mediacodec/windows10` |
| **wincap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/windowscapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
