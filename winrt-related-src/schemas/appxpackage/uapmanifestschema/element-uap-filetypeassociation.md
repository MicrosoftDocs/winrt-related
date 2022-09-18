---
description: Declares an app extensibility point of type windows.fileTypeAssociation (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:FileTypeAssociation (Windows 10)
ms.assetid: 5e876ef3-c8ca-461d-9764-4ea672e7c0ea
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:FileTypeAssociation (Windows 10)

Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:FileTypeAssociation\>**

## Syntax

```xml
<FileTypeAssociation
  Name = 'A string with a value between 1 and 100 characters in length.'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  desktop2:UseUrl = 'An optional boolean value.'
  desktop2:AllowSilentDefaultTakeOver = 'An optional boolean value.' 
  desktop5:ThumbnailTypeOverlay = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.' >

  <!-- Child elements -->
  uap:DisplayName?
  & uap:Logo?
  & uap:InfoTip?
  & uap:EditFlags?
  & uap:SupportedFileTypes?
  & uap2:SupportedVerbs?
  & uap4:KindMap?
  & rescap3:MigrationProgIds?
  & desktop2:ThumbnailHandler?
  & desktop2:OleClass?
  & desktop2:DesktopPreviewHandler?
  & desktop2:DesktopPropertyHandler?
  & desktop3:PropertyLists?
  & desktop7:Logo?

</uap:FileTypeAssociation>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the file type association. You can use this name to organize and group file types. The name must be all lower case characters with no spaces. | A string with a value between 1 and 100 characters in length. | Yes |  |
| **DesiredView** | The desired amount of screen space to use when the app launches. This view mode preference is a requested value only. The preferred size that you specify is not guaranteed to be honored by Windows, so you should not write code that relies on never getting into a size that is smaller than the preferred minimum size or larger than the preferred maximum size. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, or *useMinimum*. | No |  |
| **desktop2:UseUrl** | If set to true, specifies that the application can accept a URL, instead of a file name, on the command line. Applications that can open documents directly from the internet, like web browsers and media players, should use this value. When `ShellExecuteEx` starts an application and this value is set to false, the default behavior, `ShellExecuteEx` downloads the document to a local file and invokes the handler on the local copy. | An optional boolean value. | No |  |
| **desktop2:AllowSilentDefaultTakeOver** | If set to *true*, the app will appear in an "Open With" list, but it won't be the default app for the file type. | An optional boolean value. | No |  |
| **desktop5:ThumbnailTypeOverlay** | An image resource for a thumbnail overlay. | A string with a value between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap:DisplayName](element-uap-displayname.md) | A friendly name that can be displayed to users. |
| [uap:EditFlags](element-uap-editflags.md) | Specifies the type of info the user sees when opening a file associated to the extensibility point. |
| [uap:InfoTip](element-uap-infotip.md) | Defines a string that provides additional info to the user about the file type. |
| [uap:Logo](element-uap-logo.md) | A path to a file that contains an image. |
| [uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md) | Defines the file types associated with the app. They are unique per package and are case sensitive. |
| [uap2:SupportedVerbs](element-uap2-supportedverbs.md) | Contains verbs for a file context menu. |
| [uap4:KindMap](element-uap4-kindmap.md) | Specifies what Kind is and how it's used. |
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describe the application, component, and version of each desktop application from which you want to inherit file associations. |
| [desktop2:ThumbnailHandler](element-desktop2-thumbnailhander.md) | Enables a ThumbnailProvider for a file type association. |
| [desktop2:OleClass](element-desktop2-oleclass.md) | Enables OLE to get the OLE class registered for a given file extension. |
| [desktop2:DesktopPreviewHandler](element-desktop2-DesktopPreviewHandler.md) | Enables declaration of a preview handler for a file type association. |
| [desktop2:DesktopPropertyHandler](element-desktop2-DesktopPropertyHandler.md) | Enables declaration of a property handler for a file type association. |
| [desktop3:PropertyLists](element-desktop3-propertylists.md) | Contains a list of properties to show under the properties tab of a file. |
| [desktop7:Logo](element-desktop7-logo.md) | A path to a file that contains an image. Adds support for .ico file extensions. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
