---
title: uap5:SupportedContentTypes
description: Contains the media/content types supported by the media source.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:MediaSource, uap5:SupportedContentTypes]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:SupportedContentTypes

Contains the media/content types supported by the media source.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:MediaSource>`](element-uap5-mediasource.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:SupportedContentTypes>`**

## Syntax

```xml
<uap5:SupportedContentTypes>

  <!-- Child elements -->
  uap5:ContentType{0,1000}

</uap5:SupportedContentTypes>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap5:ContentType](element-uap5-contenttype.md) | Specifies the media/content type supported by the media source. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:MediaSource](element-uap5-mediasource.md) | Specifies the media source and the app service that it exposes. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
