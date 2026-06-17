---
title: uap4:MediaEncodingProperties
description: Contains the media coded input and output types.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap4:Extension, uap4:MediaCodec, uap4:MediaEncodingProperties]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap4:MediaEncodingProperties

Contains the media coded input and output types.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:Extension>`](element-uap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:MediaCodec>`](element-uap4-mediacodec.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:MediaEncodingProperties>`**

## Syntax

```xml
<uap4:MediaEncodingProperties>

  <!-- Child elements -->
  uap4:InputTypes
  uap4:OutputTypes

</uap4:MediaEncodingProperties>
```

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap4:InputTypes](element-uap4-inputtypes.md) | Contains the media codec input types. |
| [uap4:OutputTypes](element-uap4-outputtypes.md) | Contains the media codec output types. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap4:MediaCodec](element-uap4-mediacodec.md) | Defines an extension that enables an app to install media codecs from the Microsoft Store. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
