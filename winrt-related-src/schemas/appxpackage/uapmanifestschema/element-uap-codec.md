---
description: Specifies the codec to use for transcoding.
Search.Product: eADQiWindows 10XVcnh
title: uap:Codec (Windows 10)
ms.assetid: 7b42abe0-154d-4377-ba94-4edda3d0586c
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:Codec (Windows 10)

Specifies the codec to use for transcoding.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:MediaPlayback\>](element-uap-mediaplayback.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:Codec\>**

## Syntax

```xml
<uap:Codec
  Name = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the codec. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:MediaPlayback](element-uap-mediaplayback.md) | Declares an app extensibility point of type *mediaPlayback* so that your app can declare that it performs video transcoding. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
