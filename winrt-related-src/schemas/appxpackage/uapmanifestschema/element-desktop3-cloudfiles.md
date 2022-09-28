---
title: desktop3:CloudFiles
description: Registration for the handlers implemented in an application and context menu options for cloud based placeholder files.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:CloudFiles

Registration for the handlers implemented in an application and context menu options for cloud based placeholder files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop3:CloudFiles\>**

## Syntax

```xml
<desktop3:CloudFiles IconResource = 'A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that cant contain these characters: <, >, :, %, ", |, ?, or *. In this string, the / and \ characters cant be the first or last characters. Also, the string can contain / or \ but not both.' >
    
  <!-- Child elements -->
  ( desktop3:CustomStateHandler,
    desktop3:ThumbnailProviderHandler, 
    desktop3:ExtendedPropertyHandler,
    desktop3:BannersHandler,
    desktop3:CloudFilesContextMenus,
    desktop4:ContentUriSource )
    
</desktop3:CloudFiles>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **IconResource** | A path to an icon that represents the sync provider. | A string between 1 and 256 characters in length that ends with `.jpg`, `.png`, or `.jpeg` that can't contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. In this string, the `/` and `\` characters can't be the first or last characters. Also, the string can contain `/` or `\` but not both. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop3:CustomStateHandler](element-desktop3-customstatehandler.md) | Registration of a Windows Shell CustomStateHandler for cloud based placeholder files. |  
| [desktop3:ThumbnailProviderHandler](element-desktop3-ThumbnailProviderHandler.md) | Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. |  
| [desktop3:ExtendedPropertyHandler](element-desktop3-ExtendedPropertyHandler.md) | Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files. |  
| [desktop3:BannersHandler](element-desktop3-BannersHandler.md) | Registration of a Windows Shell BannersHandler for cloud based placeholder files. |  
| [desktop3:CloudFilesContextMenus](element-desktop3-CloudFilesContextMenus.md) | Registration of a context menu for a cloud based placeholder file. |
| [desktop4:ContentUriSource](element-desktop4-contenturisource.md) | Registration of a Windows Shell ContentUriSource enabling cloud storage providers to provide a file ID for a given local path. |  

### Parent elements

| Parent element | Description |
|-|-|
| [desktop3:Extension](element-desktop3-extension.md) | Declares an extensibility point for the app. |

## See also

[Creating Shell Extension Handlers](/windows/win32/shell/handlers)

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
