---
title: desktop8:EventTracing
description: Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:EventTracing

Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:EventTracing\>**

## Syntax

```xml
<desktop8:EventTracing>

  <!-- Child Elements -->
  desktop8:Provider

</desktop8:EventTracing>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop8:Provider](element-desktop8-provider.md) | Registers a provider to Event Tracing and enables its functionality. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Extension (in Package/Application)](element-desktop8-extension.md) | Declares an extensibility point for the application. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| Minimum OS Version | Windows 11 version 21H2 (Build 22000) |
