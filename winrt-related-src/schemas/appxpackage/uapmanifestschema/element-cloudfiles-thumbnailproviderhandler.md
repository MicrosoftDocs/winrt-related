---
title: cloudFiles:ThumbnailProviderHandler
description: Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. (cloudFiles:ThumbnailProviderHandler)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, cloudFiles:Extension, cloudFiles:CloudFiles, cloudFiles:ThumbnailProviderHandler]
---

# cloudFiles:ThumbnailProviderHandler

Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. 

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:Extension>`](element-cloudfiles-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:CloudFiles>`](element-cloudfiles-cloudfiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<cloudFiles:ThumbnailProviderHandler>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:Extension>`](element-cloudfiles-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles:CloudFiles>`](element-cloudfiles-cloudfiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<cloudFiles:ThumbnailProviderHandler>`**  


## Syntax

```xml
<cloudFiles:ThumbnailProviderHandler
  Clsid = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**Clsid**| The class ID of the app that implements the ThumbnailProviderHandler, used for thumbnail images of placeholder files. |An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|No||

## Child elements

None.


## Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:CloudFiles](element-cloudfiles-cloudfiles.md) | Registers the handlers implemented in an application and context menu options for cloud based placeholder files. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |
| **Minimum OS Version** | Windows 10 (Build 19645) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also

[Creating Shell Extension Handlers](/windows/win32/shell/handlers)
