---
title: uap5:VideoRendererExtensionProfiles
description: Contains a list of video renderer profiles.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:VideoRendererEffect, uap5:VideoRendererExtensionProfiles]
---

# uap5:VideoRendererExtensionProfiles

Contains a list of video renderer profiles.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:VideoRendererEffect>`](element-uap5-videorenderereffect.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:VideoRendererExtensionProfiles>`**  

## Syntax

```xml
<uap5:VideoRendererExtensionProfiles>

  <!-- Child elements -->
  uap5:VideoRendererExtensionProfile{0,1000}

</uap5:VideoRendererExtensionProfiles>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap5:VideoRendererExtensionProfile](element-uap5-videorendererextensionprofile.md) | Specifies a video renderer profile. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:VideoRendererEffect](element-uap5-videorenderereffect.md) | Enables activation of video renderer effects in apps. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
