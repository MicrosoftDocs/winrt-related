---
title: cloudFiles2:StorageProviderStatusUISourceFactory
description: Registration of a Windows Shell StorageProviderStatusUI for cloud-based placeholder files. (cloudFiles2:StorageProviderStatusUISourceFactory)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, cloudFiles2:Extension, cloudFiles2:CloudFiles, cloudFiles2:StorageProviderStatusUISourceFactory]
---

# cloudFiles2:StorageProviderStatusUISourceFactory

Registration of a Windows shell [IStorageProviderStatusUISourceFactory](/uwp/api/windows.storage.provider.istorageproviderstatusuisourcefactory) for cloud-based placeholder files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles2:Extension>`](element-cloudfiles-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<cloudFiles2:CloudFiles>`](element-cloudfiles-cloudfiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<cloudFiles2:StorageProviderStatusUISourceFactory>`**  


## Syntax

```xml
<cloudFiles2:StorageProviderStatusUISourceFactory
  Clsid = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|**Clsid**| The class ID of the app that implements the **IStorageProviderStatusUI** interface, used for the storage provider status UI flyout for placeholder files. |A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.|Yes||

## Child elements

None.


## Parent elements

| Parent element | Description |
|-|-|
| [desktop3:CloudFiles](element-desktop3-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10/2` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also

[Creating Shell Extension Handlers](/windows/win32/shell/handlers)
