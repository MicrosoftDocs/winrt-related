---
title: desktop4:DesktopIconOverlayHandler
description: Windows Shell icon overlay handlers for cloud based placeholder files. 
ms.date: 4/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:DesktopIconOverlayHandler

Windows Shell icon overlay handlers for cloud based placeholder files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:CloudFiles\>](element-desktop3-cloudfiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop4:DesktopIconOverlayHandlers\>](element-desktop4-desktopiconoverlayhandlers.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop4:DesktopIconOverlayHandler\>**

## Syntax

```xml
<desktop4:DesktopIconOverlayHandler
  Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | The class ID of the app that implements the overlay handler. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop4:DesktopIconOverlayHandlers](element-desktop4-desktopiconoverlayhandlers.md) | Contains Windows Shell icon overlay handlers for cloud based placeholder files. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
