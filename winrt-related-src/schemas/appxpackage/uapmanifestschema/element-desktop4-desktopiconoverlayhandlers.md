---
title: desktop4:DesktopIconOverlayHandlers
description: Contains Windows Shell icon overlay handlers for cloud based placeholder files.  
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:DesktopIconOverlayHandlers

Contains Windows Shell icon overlay handlers for cloud based placeholder files. 

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:CloudFiles\>](element-desktop3-cloudfiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop4:DesktopIconOverlayHandlers\>**

## Syntax

```xml
<desktop4:DesktopIconOverlayHandlers>
    
  <!-- Child elements -->
  desktop4:DesktopIconOverlayHandler{0,10000} 
    
</desktop4:DesktopIconOverlayHandlers>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop4:DesktopIconOverlayHandler](element-desktop4-desktopiconoverlayhandler.md) | Registration for a Windows Shell icon overlay handler. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop3:CloudFiles](element-desktop3-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |

## See Also

[How to Register Icon Overlay Handlers](/windows/win32/shell/how-to-register-icon-overlay-handlers)

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
