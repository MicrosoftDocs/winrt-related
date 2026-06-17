---
title: desktop3:CloudFiles
description: Registration for the handlers implemented in an application and context menu options for cloud based placeholder files.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop3:Extension, desktop3:CloudFiles]
---

# desktop3:CloudFiles

Registration for the handlers implemented in an application and context menu options for cloud based placeholder files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop3:Extension>`](element-desktop3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop3:CloudFiles>`**

## Syntax

```xml
<desktop3:CloudFiles
  IconResource = 'An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both.' >

  <!-- Child elements -->
  desktop3:CustomStateHandler?
  desktop3:ThumbnailProviderHandler?
  desktop3:ExtendedPropertyHandler?
  desktop3:BannersHandler?
  desktop3:ContentUriSource?
  desktop3:CloudFilesContextMenus?
  desktop3:DesktopIconOverlayHandlers?
  desktop3:StorageProviderStatusUISourceFactory?

</desktop3:CloudFiles>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **IconResource** | A path to an icon that represents the sync provider. | An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, ` &#124; `, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop3:CustomStateHandler](element-desktop3-customstatehandler.md) | Registration of a Windows Shell CustomStateHandler for cloud based placeholder files. |
| [desktop3:ThumbnailProviderHandler](element-desktop3-thumbnailproviderhandler.md) | Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. |
| [desktop3:ExtendedPropertyHandler](element-desktop3-extendedpropertyhandler.md) | Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files. |
| [desktop3:BannersHandler](element-desktop3-bannershandler.md) | Registration of a Windows Shell BannersHandler for cloud based placeholder files. |
| [desktop4:ContentUriSource](element-desktop4-contenturisource.md) | Registration of a Windows Shell ContentUriSource enabling cloud storage providers to provide a file ID for a given local path. |
| [desktop3:CloudFilesContextMenus](element-desktop3-cloudfilescontextmenus.md) | Registration of a context menu for a cloud based placeholder file. |
| [desktop4:DesktopIconOverlayHandlers](element-desktop4-desktopiconoverlayhandlers.md) | Contains Windows Shell icon overlay handlers for cloud based placeholder files. |
| [cloudFiles2:StorageProviderStatusUISourceFactory](element-cloudfiles2-storageproviderstatusuisourcefactory.md) | Registration of a Windows shell [IStorageProviderStatusUISourceFactory](/uwp/api/windows.storage.provider.istorageproviderstatusuisourcefactory) for cloud-based placeholder files. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop3:Extension](element-desktop3-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also

[Creating Shell Extension Handlers](/windows/win32/shell/handlers)
