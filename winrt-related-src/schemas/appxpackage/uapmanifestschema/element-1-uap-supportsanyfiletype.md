---
description: Indicates whether all file types are supported for sharing (Windows 10, descendant of uap:FileOpenPicker).
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportsAnyFileType (Windows 10, descendant of uap:FileOpenPicker)
ms.assetid: dbc9307b-0811-49b6-8f97-938313188453
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:SupportsAnyFileType (Windows 10, descendant of uap:FileOpenPicker)

Indicates whether all file types are supported for sharing.

## Element hierarchy

> [\<Package\>](element-package.md)
> > [\<Applications\>](element-applications.md)
> > > [\<Application\>](element-application.md)
> > > > [\<Extensions\>](element-extensions.md)
> > > > > [\<uap:Extension\>](element-uap-extension.md)
> > > > > > [\<uap:ShareTarget\>](element-uap-sharetarget.md)
> > > > > > [\<uap:FileOpenPicker\>](element-uap-fileopenpicker.md)
> > > > > > [\<uap:FileSavePicker\>](element-uap-filesavepicker.md)
> > > > > > > **\<uap:SupportsAnyFileType\>**

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
| uap:SupportedFileTypes (type: *CT_CharmsSupportedFileTypes*) | Defines the file types the app can share. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
