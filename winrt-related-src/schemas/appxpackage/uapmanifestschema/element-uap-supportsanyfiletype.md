---
description: Indicates whether all file types are supported (in ShareTarget, FileOpenPicker, or FileSavePicker contexts).
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportsAnyFileType
ms.assetid: 3dbbeaac-2578-472b-80d2-f0bd0b9ead7e
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:ShareTarget, uap:FileOpenPicker, uap:FileSavePicker, uap:SupportedFileTypes, uap:SupportsAnyFileType]
---

# uap:SupportsAnyFileType

Indicates whether all file types are supported for sharing.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:ShareTarget>`](element-uap-sharetarget.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:FileOpenPicker>`](element-uap-fileopenpicker.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:FileSavePicker>`](element-uap-filesavepicker.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:SupportedFileTypes>`](element-uap-sharetarget-supportedfiletypes.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:SupportsAnyFileType>`**

## Syntax

```xml
<uap:SupportsAnyFileType>
  xs:anyType
</uap:SupportsAnyFileType>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-uap-sharetarget-supportedfiletypes.md) | Defines the file types that the app can share. |

## Examples

```xml
<uap:ShareTarget>
  <uap:SupportedFileTypes>
    <uap:SupportsAnyFileType />
  </uap:SupportedFileTypes>
  <uap:DataFormat>Text</uap:DataFormat>
  <uap:DataFormat>Uri</uap:DataFormat>
</uap:ShareTarget>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
