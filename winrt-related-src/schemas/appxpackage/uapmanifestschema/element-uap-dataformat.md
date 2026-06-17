---
title: uap:DataFormat
description: Specifies a data package format such as text or HTML format that the app can share (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:ShareTarget, uap:DataFormat]
---

# uap:DataFormat

Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:ShareTarget>`](element-uap-sharetarget.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:DataFormat>`**  

## Syntax

```xml
<uap:DataFormat>
    <!-- TODO: Add value description -->
</uap:DataFormat>
```

## Value

A string with a value between 1 and 255 characters in length. DataFormat values specified by the user must be unique within the app.

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:ShareTarget](element-uap-sharetarget.md) | Declares an app extension point of type *windows.shareTarget*. The app can share the specified types of files. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<uap:ShareTarget>
  <uap:SupportedFileTypes>
    <uap:FileType>.txt</uap:FileType>
    <uap:FileType>.docx</uap:FileType>
  </uap:SupportedFileTypes>
  <uap:DataFormat>Text</uap:DataFormat>
  <uap:DataFormat>Uri</uap:DataFormat>
  <uap:DataFormat>Bitmap</uap:DataFormat>
  <uap:DataFormat>Html</uap:DataFormat>
  <uap:DataFormat>http://schema.org/Book</uap:DataFormat>
</uap:ShareTarget>
```
