---
title: uap:FileTypeAssociation
description: Declares an app extensibility point of type windows.fileTypeAssociation (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:FileTypeAssociation]
---

# uap:FileTypeAssociation

Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:FileTypeAssociation>`**  

## Syntax

```xml
<uap:FileTypeAssociation
  Name = 'A required string between 1 and 64 characters in length.'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  desktop2:UseUrl = 'An optional boolean value.'
  desktop2:AllowSilentDefaultTakeOver = 'An optional boolean value.'
  desktop5:ThumbnailTypeOverlay = 'An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both.'
  uap8:Launch = 'An optional string that can have one of the following values: "file", or "placeholderFile".' >

  <!-- Child elements -->
  uap:DisplayName?
  uap:Logo?
  uap:Logo?
  uap:Logo?
  uap:InfoTip?
  uap:EditFlags?
  uap:SupportedFileTypes
  uap:FileTypeAssociationSupportedVerbsChoice?
  uap:KindMap?
  uap:MigrationProgIds?
  uap:ThumbnailHandler?
  uap:DesktopPreviewHandler?
  uap:DesktopPropertyHandler?
  uap:OleClass?
  uap:PropertyLists?
  uap:ProgId?
  uap:ProgId?
  uap:IconHandler?

</uap:FileTypeAssociation>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the file type association. You can use this name to organize and group file types. The name must be all lower case characters with no spaces. | A string between 1 and 64 characters in length. | Yes |  |
| **DesiredView** | The desired amount of screen space to use when the app launches. This view mode preference is a requested value only. The preferred size that you specify is not guaranteed to be honored by Windows, so you should not write code that relies on never getting into a size that is smaller than the preferred minimum size or larger than the preferred maximum size. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, *useMinimum*. | No |  |
| **desktop2:UseUrl** | If set to true, specifies that the application can accept a URL, instead of a file name, on the command line. Applications that can open documents directly from the internet, like web browsers and media players, should use this value. When `ShellExecuteEx` starts an application and this value is set to false, the default behavior, `ShellExecuteEx` downloads the document to a local file and invokes the handler on the local copy. | An optional boolean value. | No |  |
| **desktop2:AllowSilentDefaultTakeOver** | If set to *true*, the app will appear in an "Open With" list, but it won't be the default app for the file type. | An optional boolean value. | No |  |
| **desktop5:ThumbnailTypeOverlay** | An image resource for a thumbnail overlay. | An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `&#124;`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |
| **uap8:Launch** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *file*, *placeholderFile*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap:DisplayName](element-uap-displayname.md) | A friendly name that can be displayed to users. |
| [uap:Logo](element-uap-logo.md) | A path to a file that contains an image. |
| **previewappcompat3:Logo** | A path to a file that contains an image. Adds support for .ico file extensions. |
| [desktop7:Logo](element-desktop7-logo.md) | A path to a file that contains an image. Adds support for .ico, .dll, and .exe files. |
| [uap:InfoTip](element-uap-infotip.md) | Defines a string that provides additional info to the user about the file type. |
| [uap:EditFlags](element-uap-editflags.md) | Specifies the type of info the user sees when opening a file associated to the extensibility point. |
| **uap:SupportedFileTypes** | <!-- TODO: Add description --> |
| [uap4:KindMap](element-uap4-kindmap.md) | Specifies what Kind is and how it's used. |
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations. |
| [desktop2:ThumbnailHandler](element-desktop2-thumbnailhandler.md) | Enables a ThumbnailProvider for a file type association. |
| [desktop2:DesktopPreviewHandler](element-desktop2-desktoppreviewhandler.md) | Enables declaration of a preview handler for a file type association. |
| [desktop2:DesktopPropertyHandler](element-desktop2-desktoppropertyhandler.md) | Enables declaration of a property handler for a file type association. |
| [desktop2:OleClass](element-desktop2-oleclass.md) | Enables OLE to get the OLE class registered for a given file extension. |
| [desktop3:PropertyLists](element-desktop3-propertylists.md) | Contains a list of properties to show under the properties tab of a file. |
| [previewappcompat:ProgId](element-previewappcompat-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |
| [desktop7:ProgId](element-desktop7-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique. |
| [desktop10:IconHandler](element-desktop10-iconhandler.md) | Enables an IconHandler for a file type association. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **desktop2** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **desktop5** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/5` |
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
