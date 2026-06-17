---
title: desktop7:DesktopAppMigration
description: Specifies a set of app migration entries for tiles and pins.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:DesktopAppMigration]
---

# desktop7:DesktopAppMigration

Specifies a set of app migration entries for tiles and pins.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:DesktopAppMigration>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:DesktopAppMigration>`**

## Syntax

```xml
<desktop7:DesktopAppMigration
  AcquisitionUri = 'An optional string between 1 and 2084 characters in length in the form of a valid URI.' >

  <!-- Child elements -->
  desktop7:DesktopApp{0,10000}

</desktop7:DesktopAppMigration>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AcquisitionUri** | <!-- TODO: Add description --> | An optional string between 1 and 2084 characters in length in the form of a valid URI. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop7:DesktopApp](element-desktop7-desktopapp.md) | Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration. |

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

This element requires the [runFullTrust](/windows/uwp/packaging/app-capability-declarations) capability.

## Examples

<!-- Author content goes here -->
