---
title: cloudFiles:ExtendedPropertyHandler
description: Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files. (cloudFiles:ExtendedPropertyHandler) 
ms.date: 01/27/2023
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# cloudFiles:ExtendedPropertyHandler

Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<cloudFiles:Extension\>](element-cloudfiles-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<cloudFiles:CloudFiles\>](element-cloudfiles-cloudfiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<cloudFiles:ExtendedPropertyHandler\>**

## Syntax

```xml
<cloudFiles:ExtendedPropertyHandler
  Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | The class ID of the app that implements the [IStorageProviderPropertyCapabilities](/uwp/api/windows.storage.provider.istorageproviderpropertycapabilities) interface, used for extended properties of placeholder files. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:CloudFiles](element-cloudfiles-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |
## See also

[Creating Shell Extension Handlers](/windows/win32/shell/handlers)


## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
