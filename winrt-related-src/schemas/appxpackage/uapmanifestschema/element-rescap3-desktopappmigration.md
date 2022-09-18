---
ms.assetid: 350e2733-4da7-4e0b-a0aa-291c15c80e25
title: rescap3:DesktopAppMigration
description: Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:DesktopAppMigration

Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap3:Extension\>](element-rescap3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap3:DesktopAppMigration\>**

## Syntax

```xml
<rescap3:DesktopAppMigration
  AcquisitionUri = 'An optional string with a value between 1 and 2084 characters in length.' >

  <!-- Child elements -->
  rescap3:DesktopApp{1,10000}

</rescap3:DesktopAppMigration>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AcquisitionUri** | The URI that a tile/pin will be migrated to. | A string between 1 and 2084 characters in length. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [DesktopApp](element-rescap3-desktopapp.md) | Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins. |

### Parent elements

| Parent element | Description |
|-|-|
| [rescap3:Extension](element-rescap3-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
