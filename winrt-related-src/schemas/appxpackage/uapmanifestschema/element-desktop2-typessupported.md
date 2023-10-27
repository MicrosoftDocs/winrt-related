---
ms.assetid: f2d6f151-53bb-4ae0-971b-23f8deb16980
title: desktop2:TypesSupported
description: Contains the event log types that are supported.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:TypesSupported

Contains the event log types that are supported.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-package-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:DesktopEventLogging\>](element-desktop2-DesktopEventLogging.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:TypesSupported\>**

## Syntax

```xml
<desktop2:TypesSupported>

  <!-- Child elements -->
  desktop2:TypeSupported{1,5}

</desktop2:TypesSupported>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [TypeSupported](element-desktop2-typesupported.md) | Specifies the types of events that are supported. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:DesktopEventLogging](element-desktop2-DesktopEventLogging.md) | Enables Windows Desktop Bridge apps to register for Windows event logging. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
