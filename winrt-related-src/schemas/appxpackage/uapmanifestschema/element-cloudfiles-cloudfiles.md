---
title: cloudFiles:CloudFiles
description: Registers the handlers implemented in an application and context menu options for cloud-based placeholder files. (cloudFiles:CloudFiles)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, cloudFiles:Extension, cloudFiles:CloudFiles]
---

# cloudFiles:CloudFiles

Registers the handlers implemented in an application and context menu options for cloud based placeholder files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:Extension>`](element-cloudfiles-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<cloudFiles:CloudFiles>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:Extension>`](element-cloudfiles-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<cloudFiles:CloudFiles>`**  


## Syntax

```xml
<cloudFiles:CloudFiles
  IconResource = 'An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both.' >

  <!-- Child elements -->
  cloudFiles:CustomStateHandler?
  cloudFiles:ThumbnailProviderHandler?
  cloudFiles:ExtendedPropertyHandler?
  cloudFiles:BannersHandler?
  cloudFiles:ContentUriSource?
  cloudFiles:CloudFilesContextMenus?
  cloudFiles:DesktopIconOverlayHandlers?
  cloudFiles:StorageProviderStatusUISourceFactory?

</cloudFiles:CloudFiles>
```

### Key

`?` optional (zero or one)


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**IconResource**| A path to an icon that represents the sync provider. |An optional string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `&#124;`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both.|No||

## Child elements
| Child element | Description |
|-|-|
| [cloudFiles:CustomStateHandler](element-cloudfiles-customstatehandler.md) | Registration of a Windows Shell CustomStateHandler for cloud based placeholder files. |
| [cloudFiles:ThumbnailProviderHandler](element-cloudfiles-thumbnailproviderhandler.md) | Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. |
| [cloudFiles:ExtendedPropertyHandler](element-cloudfiles-extendedpropertyhandler.md) | Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files. |
| [cloudFiles:BannersHandler](element-cloudfiles-bannershandler.md) | Registration of a Windows Shell BannersHandler for cloud based placeholder files. |
| [cloudFiles:ContentUriSource](element-cloudfiles-contenturisource.md) | Registration of a Windows Shell CustomStateHandler for cloud based placeholder files. |
| [cloudFiles:CloudFilesContextMenus](element-cloudfiles-cloudfilescontextmenus.md) | Registration of a context menu for a cloud based placeholder file. |
| [cloudFiles:DesktopIconOverlayHandlers](element-cloudfiles-desktopiconoverlayhandlers.md) | Contains Windows Shell icon overlay handlers for cloud based placeholder files. |
| [cloudFiles2:StorageProviderStatusUISourceFactory](element-cloudfiles2-storageproviderstatusuisourcefactory.md) | Registration of a Windows shell [IStorageProviderStatusUISourceFactory](/uwp/api/windows.storage.provider.istorageproviderstatusuisourcefactory) for cloud-based placeholder files. |

## Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:Extension](element-cloudfiles-extension.md) | Declares an extensibility point for the app that registers the handlers implemented in an application and context menu options for cloud-based placeholder files. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |
| **Minimum OS Version** | Windows 10 (Build 19645) |


## Remarks

For more information, see [Build a Cloud Sync Engine that Supports Placeholder Files](/windows/win32/cfapi/build-a-cloud-file-sync-engine).

## Examples

<!-- Author content goes here -->
