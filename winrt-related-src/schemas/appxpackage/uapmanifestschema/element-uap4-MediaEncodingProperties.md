---
ms.assetid: deb8e538-57e7-4b92-b121-6b2ea53f5094
title: uap4:MediaEncodingProperties
description: Contains the media coded input and output types.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:MediaEncodingProperties

Contains the media coded input and output types.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:Extension\>](element-uap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:MediaCodec\>](element-uap4-mediacodec.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:MediaEncodingProperties\>**

## Syntax

```xml
<uap4:MediaEncodingProperties>

  <!-- Child elements -->
  uap4:InputTypes,
  uap4:OutputTypes

</uap4:MediaEncodingProperties>                   
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [InputTypes](element-uap4-inputtypes.md) | Contains the media codec input types. |
| [OutputTypes](element-uap4-outputtypes.md) | Contains the media codec output types. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap4:MediaCodec](element-uap4-mediacodec.md) | Defines an extension that enables an app to install media codecs from the Microsoft Store. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
