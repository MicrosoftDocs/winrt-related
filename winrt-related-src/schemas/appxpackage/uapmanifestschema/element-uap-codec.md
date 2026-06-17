---
title: uap:Codec
description: Specifies the codec to use for transcoding.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:MediaPlayback, uap:Codec]
---

# uap:Codec

Specifies the codec to use for transcoding.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:MediaPlayback>`](element-uap-mediaplayback.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:Codec>`**  

## Syntax

```xml
<uap:Codec
  Name = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the codec. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:MediaPlayback](element-uap-mediaplayback.md) | Declares an app extensibility point of type *mediaPlayback* so that your app can declare that it performs video transcoding. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
