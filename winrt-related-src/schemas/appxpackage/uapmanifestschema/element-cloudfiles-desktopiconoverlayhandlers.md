---
title: cloudFiles:DesktopIconOverlayHandlers
description: Contains Windows Shell icon overlay handlers for cloud based placeholder files. (cloudFiles:DesktopIconOverlayHandlers)
ms.date: 01/27/2023
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# cloudFiles:DesktopIconOverlayHandlers

Contains Windows Shell icon overlay handlers for cloud based placeholder files. 

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<cloudFiles:Extension\>](element-cloudfiles-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<cloudFiles:CloudFiles\>](element-cloudfiles-cloudfiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<cloudFiles:DesktopIconOverlayHandlers\>**

## Syntax

```xml
<cloudFiles:DesktopIconOverlayHandlers>
    
  <!-- Child elements -->
  cloudFiles:DesktopIconOverlayHandler{0,10000} 
    
</cloudFiles:DesktopIconOverlayHandlers>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [cloudFiles:DesktopIconOverlayHandler](element-cloudfiles-desktopiconoverlayhandler.md) | Registration for a Windows Shell icon overlay handler. |

### Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:CloudFiles](element-cloudfiles-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |

## See Also

[How to Register Icon Overlay Handlers](/windows/win32/shell/how-to-register-icon-overlay-handlers)

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |
