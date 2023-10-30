---
description: Declares an app extensibility point of type windows.aowApp.
Search.Product: eADQiWindows 10XVcnh
title: mobile:AowApp (Windows 10)
ms.assetid: 5a716d59-0796-4584-890f-98f26b0654ce
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# mobile:AowApp (Windows 10)

Declares an app extensibility point of type **windows.aowApp**.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<mobile:Extension\>](element-mobile-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<mobile:AowApp\>**

## Syntax

```xml
<mobile:Extension

  <!-- Child elements -->
  mobile:PayloadName
  & mobile:PayloadVersion

</mobile:Extension>
```

### Key

`&`  interleave connector (may occur in any order)

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| **mobile:PayloadName**    | An element containing a string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. |
| **mobile:PayloadVersion** | An element containing a string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. |

### Parent elements

| Parent element | Description |
|-|-|
| [**mobile:Extension**](element-mobile-extension-manual.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/mobile/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
