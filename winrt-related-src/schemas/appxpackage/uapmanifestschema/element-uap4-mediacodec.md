---
ms.assetid: 1fe032ac-19b2-49a5-9f8f-093ab9102e66
title: uap4:MediaCodec
description: Defines an extension that enables an app to install media codecs from the Microsoft Store.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:MediaCodec

Defines an extension that enables an app to install media codecs from the Microsoft Store.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:Extension\>](element-uap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:MediaCodec\>**

## Syntax

```xml
<uap4:MediaCodec
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
  Description = 'A string between 1 and 2048 characters in length.'
  Category = 'A string that can have one of the following values: "audioDecoder", "audioEncoder","videoDecoder", or "videoEncoder".'
  AppServiceName = 'An optional string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.' 
  wincap3:ActivatableClassId = 'A string with a value between 1 and 255 characters in length.'
  wincap3:Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, ", |, ?, or *.'
  wincap3:ProcessorArchitecture = 'A string value that can be one of the following: "x86", "x64", "arm", "arm64", or "neutral".' >

  <!-- Child elements -->
  uap4:MediaEncodingProperties

</uap4:MediaCodec>                   
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The friendly name of the codec. | A string with a value between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **Description** | A description of the codec. | A string between 1 and 2048 characters in length. | Yes |  |
| **Category** | The category of the codec. | A string that can have one of the following values: *audioDecoder*, *audioEncoder*,*videoDecoder*, or *videoEncoder*. | Yes |  |
| **AppServiceName** | The app service that is launched as the codec. | An optional string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | No |  |
| **rescap3:ActivatableClassId** | The class ID associated with this media content. | A string with a value between 1 and 255 characters in length. | No |
| **rescap3:Path** | The path to the media content. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `"`, `|`, `?`, or `*`. | No |
| **rescap3:ProcessorArchitecture** | The processor architecture used for the media content. | A string value that can be one of the following: *x86*, *x64*, *arm*, *arm64*, or *neutral*. | No |


### Child elements

| Child element | Description |
|-|-|
| [MediaEncodingProperties](element-uap4-MediaEncodingProperties.md) | Contains the media coded input and output types. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
