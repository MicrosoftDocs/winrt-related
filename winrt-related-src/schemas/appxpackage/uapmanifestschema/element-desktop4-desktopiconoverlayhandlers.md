---
title: desktop4:DesktopIconOverlayHandlers
description: Contains Windows Shell icon overlay handlers for cloud based placeholder files.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop4:Extension, desktop4:CloudFiles, desktop4:DesktopIconOverlayHandlers]
---

# desktop4:DesktopIconOverlayHandlers

Contains Windows Shell icon overlay handlers for cloud based placeholder files.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:Extension>`](element-desktop4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop4:CloudFiles>`](element-desktop3-cloudfiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop4:DesktopIconOverlayHandlers>`**

## Syntax

```xml
<desktop4:DesktopIconOverlayHandlers>

  <!-- Child elements -->
  desktop4:DesktopIconOverlayHandler{0,10000}

</desktop4:DesktopIconOverlayHandlers>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop4:DesktopIconOverlayHandler](element-desktop4-desktopiconoverlayhandler.md) | Windows Shell icon overlay handlers for cloud based placeholder files. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop3:CloudFiles](element-desktop3-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1803 (Build 17134) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
