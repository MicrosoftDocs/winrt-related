---
title: uap5:SupportedFileTypes
description: Contains the file types supported by the media source.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:SupportedFileTypes

Contains the file types supported by the media source.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:MediaSource\>](element-uap5-mediasource.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:SupportedFileTypes\>**

## Syntax

```xml
<uap5:SupportedFileTypes>

  <!-- Child elements -->
  uap5:FileType{0,1000}

</uap5:SupportedFileTypes>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None

### Child elements

| Child element | Description |
|-|-|
| [FileType](element-uap5-filetype.md) | Specifies the file type suppoerted by the media source. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:MediaSource](element-uap5-mediasource.md) | Specifies the media source and the app service that it exposes. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| Minimum OS Version | Windows 10 version 1709 (Build 16299) |
