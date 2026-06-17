---
title: desktop7:ShadowCopyExcludeFiles
description: Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:ShadowCopyExcludeFiles]
---

# desktop7:ShadowCopyExcludeFiles

Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:ShadowCopyExcludeFiles>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:ShadowCopyExcludeFiles>`**

## Syntax

```xml
<desktop7:ShadowCopyExcludeFiles>

  <!-- Child elements -->
  desktop7:ShadowCopyExcludeFile{0,1000}

</desktop7:ShadowCopyExcludeFiles>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop7:ShadowCopyExcludeFile](element-desktop7-shadowcopyexcludefile.md) | Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop7:Extension](element-desktop7-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

For more information on VSS, see [Volume Shadow Copy Service Overview](/windows/win32/vss/volume-shadow-copy-service-overview).

## Examples

<!-- Author content goes here -->
