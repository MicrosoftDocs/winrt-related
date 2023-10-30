---
description: Specifies a data package format such as text or HTML format that the app can share (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:DataFormat (Windows 10)
ms.assetid: 348b61e7-ecbd-42ea-8a82-81ef85e728cb
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:DataFormat (Windows 10)

Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:ShareTarget\>](element-uap-sharetarget.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:DataFormat\>**

## Syntax

```xml
<uap:DataFormat>
  A string with a value between 1 and 255 characters in length. DataFormat values specified by the user must be unique within the app.
</uap:DataFormat>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:ShareTarget](element-uap-sharetarget.md) | Declares an app extension point of type *windows.shareTarget*. The app can share the specified types of files. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
