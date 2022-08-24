---
description: Defines the file types that the app can share (in uap:ShareTarget).
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportedFileTypes (in uap:ShareTarget) (Windows 10)
ms.assetid: 2161f39d-f31f-4ab5-81cc-da46126808a5
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:SupportedFileTypes (in uap:ShareTarget) (Windows 10)

Defines the file types that the app can share.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:ShareTarget\>](element-uap-sharetarget.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:SupportedFileTypes\>**

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileOpenPicker\>](element-uap-fileopenpicker.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:SupportedFileTypes\>**

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileSavePicker\>](element-uap-filesavepicker.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:SupportedFileTypes\>**

## Syntax

```xml
<uap:SupportedFileTypes>

  <!-- Child elements -->
  uap:FileType{1,10000}
  uap:SupportsAnyFileType

</uap:SupportedFileTypes>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:FileType (type: *ST_FileType*)](element-1-uap-filetype.md) | A file type specified as a file type extension. It's case sensitive and unique per application in the package. |
| [uap:SupportsAnyFileType](element-uap-supportsanyfiletype.md) | Indicates whether or not all file types are supported for sharing. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:ShareTarget](element-uap-sharetarget.md) | Declares an app extension point of type **windows.shareTarget**. The app can share the specified types of files. |
| [uap:FileOpenPicker](element-uap-fileopenpicker.md) | Declares an app extensibility point of type **windows.fileOpenPicker**. The app lets the user choose and open the specified types of files. |
| [uap:FileSavePicker](element-uap-filesavepicker.md) | Declares an app extensibility point of type **windows.fileSavePicker**. The app lets the user choose the file name, extension, and storage location for the specified types of files. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[uap:SupportedFileTypes (type: *CT_FTASupportedFileTypes*)](element-uap-supportedfiletypes.md)**

## Examples

```xml
<uap:SupportedFileTypes>
  <uap:FileType>.txt</uap:FileType>
  <uap:FileType>.docx</uap:FileType>
</uap:SupportedFileTypes>
```

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
