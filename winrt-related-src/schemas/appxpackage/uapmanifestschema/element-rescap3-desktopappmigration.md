---
title: rescap3:DesktopAppMigration
description: Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, rescap3:Extension, rescap3:DesktopAppMigration]
---

# rescap3:DesktopAppMigration

Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:Extension>`](element-rescap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap3:DesktopAppMigration>`**  

## Syntax

```xml
<rescap3:DesktopAppMigration
  AcquisitionUri = 'An optional string between 1 and 2084 characters in length in the form of a valid URI.' >

  <!-- Child elements -->
  rescap3:DesktopApp{0,10000}

</rescap3:DesktopAppMigration>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AcquisitionUri** | The URI that a tile/pin will be migrated to. | An optional string between 1 and 2084 characters in length in the form of a valid URI. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [rescap3:DesktopApp](element-rescap3-desktopapp.md) | Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins. |

## Parent elements

| Parent element | Description |
|-|-|
| [rescap3:Extension](element-rescap3-extension.md) | Declares an extensibility point for the app. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
