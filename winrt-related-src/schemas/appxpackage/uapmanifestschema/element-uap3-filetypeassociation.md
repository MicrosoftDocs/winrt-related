---
title: uap3:FileTypeAssociation
description: Defines the types of files used within the application.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:FileTypeAssociation

Defines the types of files used within the application.

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:FileTypeAssociation\>**

## Syntax

```xml
<uap3:FileTypeAssociation
  Name = 'A string with a value between 1 and 100 characters in length.'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  desktop2:UseUrl = 'An optional boolean value.'
  desktop2:AllowSilentDefaultTakeOver = 'An optional boolean value.' 
  desktop5:ThumbnailTypeOverlay = 'A string with a value between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both.'
  Parameters = 'An optional string with a value between 1 and 32767 characters.'
  MultiSelectModel = 'An optional string that can have one of the following values: "Player", "Document", or "Single".' >

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
  & desktop7:ProgId?
  & desktop10:IconHandler?

</uap3:FileTypeAssociation>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Parameters** | Specifies parameters to define the types of files used in the application. | An optional string with a value between 1 and 32767 characters. | No |  |
| **MultiSelectModel** | Specifies the model used to define the types of files used in the application. | An optional string that can have one of the following values: *Player*, *Document*, or *Single*. | No |  |

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
| [desktop2:ThumbnailHandler](element-desktop2-thumbnailhandler.md) | Enables a ThumbnailProvider for a file type association. |
| [desktop2:OleClass](element-desktop2-oleclass.md) | Enables OLE to get the OLE class registered for a given file extension. |
| [desktop2:DesktopPreviewHandler](element-desktop2-DesktopPreviewHandler.md) | Enables declaration of a preview handler for a file type association. |
| [desktop2:DesktopPropertyHandler](element-desktop2-DesktopPropertyHandler.md) | Enables declaration of a property handler for a file type association. |
| [desktop3:PropertyLists](element-desktop3-propertylists.md) | Contains a list of properties to show under the properties tab of a file. |
| [desktop7:Logo](element-desktop7-logo.md) | A path to a file that contains an image. Adds support for .ico file extensions. |
| [desktop7:ProgId](element-desktop7-progId.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. |
| [desktop10:IconHandler](element-desktop10-iconhandler.md) | Enables an IconHandler for a file type association. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Sets parameters to define the protocol of the extensions. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
