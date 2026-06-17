---
title: uap5:MediaSource
description: Specifies the media source and the app service that it exposes.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:MediaSource]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:MediaSource

Specifies the media source and the app service that it exposes.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:MediaSource>`**

## Syntax

```xml
<uap5:MediaSource
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  Description = 'An optional string between 1 and 2048 characters in length.'
  AppServiceName = 'An optional string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only.'
  wincap3:ActivatableClassId = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  wincap3:Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  wincap3:ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".' >

  <!-- Child elements -->
  uap5:SupportedFileTypes?
  uap5:SupportedContentTypes?

</uap5:MediaSource>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The media source display name. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **Description** | A brief description of the media source. | An optional string between 1 and 2048 characters in length. | No |  |
| **AppServiceName** | The name of the app service exposed by the media source. Note that an app service is required for a media source. | An optional string with a value between 2 and 39 characters in length that consists of alphanumeric characters, periods (except for the first character), and dashes only. | No |  |
| **wincap3:ActivatableClassId** | <!-- TODO: Add description --> | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **wincap3:Path** | <!-- TODO: Add description --> | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | No |  |
| **wincap3:ProcessorArchitecture** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *neutral*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap5:SupportedFileTypes](element-uap5-supportedfiletypes.md) | Contains the file types supported by the media source. |
| [uap5:SupportedContentTypes](element-uap5-supportedcontenttypes.md) | Contains the media/content types supported by the media source. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **wincap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/windowscapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
