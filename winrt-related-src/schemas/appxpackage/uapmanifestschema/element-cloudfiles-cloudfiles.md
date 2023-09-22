---
title: cloudFiles:CloudFiles
description: Registers the handlers implemented in an application and context menu options for cloud-based placeholder files. (cloudFiles:CloudFiles)
ms.date: 01/27/2023
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# cloudFiles:CloudFiles

Registers the handlers implemented in an application and context menu options for cloud based placeholder files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<cloudFiles:CloudFiles\>**

## Syntax

```xml
<cloudFiles:CloudFiles
  IconResource = 'A string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both.' >

  <!-- Child elements -->
  CustomStateHandler?
  ThumbnailProviderHandler?
  ExtendedPropertyHandler?
  BannersHandler?
  ContentUriSource?
  CloudFilesContextMenus?
  DesktopIconOverlayHandlers?
  cloudFiles2:StorageProviderStatusUISourceFactory?

</cloudFiles:CloudFiles>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| IconResource | A path to an icon that represents the sync provider. | A string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters cannot be the first or last characters. Also, the string can contain `/` or `\` but not both. | No |


### Child elements

| Child element | Description |
|-|-|
| [CustomStateHandler](element-cloudfiles-customstatehandler.md) | Registration of a Windows Shell CustomStateHandler for cloud-based placeholder files. |
| [ThumbnailProviderHandler](element-cloudfiles-thumbnailproviderhandler.md) | Registration of a Windows Shell ThumbnailProviderHandler for cloud-based placeholder files. |
| [ExtendedPropertyHandler](element-cloudfiles-extendedpropertyhandler.md) | Registration of a Windows Shell ExtendedPropertyHandler for cloud-based placeholder files. |
| [BannersHandler](element-cloudfiles-bannershandler.md) | Registration of a Windows Shell BannersHandler for cloud-based placeholder files. |
| [ContentUriSource](element-cloudfiles-contenturisource.md) | Registration of a Windows Shell ContentUriSource enabling cloud storage providers to provide a file ID for a given local path. |
| [CloudFilesContextMenus](element-cloudfiles-cloudfilescontextmenus.md) | Registration of a context menu for a cloud-based placeholder file. |
| [DesktopIconOverlayHandlers](element-cloudfiles-desktopiconoverlayhandlers.md) | Contains Windows Shell icon overlay handlers for cloud-based placeholder files. |
| [cloudFiles2:StorageProviderStatusUISourceFactory](element-cloudfiles2-storageproviderstatusuisourcefactory.md) | Registration of a Windows shell [IStorageProviderStatusUISourceFactory](/uwp/api/windows.storage.provider.istorageproviderstatusuisourcefactory) for cloud-based placeholder files. |


### Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:Extension](element-cloudfiles-extension.md) | Declares an extensibility point for the app that registers the handlers implemented in an application and context menu options for cloud-based placeholder files. |

## Remarks

For more information, see [Build a Cloud Sync Engine that Supports Placeholder Files](/windows/win32/cfapi/build-a-cloud-file-sync-engine).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |

