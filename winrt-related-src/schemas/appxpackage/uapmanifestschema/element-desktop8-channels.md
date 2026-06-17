---
title: desktop8:Channels
description: Allows one or more channels to be specified for event tracing.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop
no-loc: [Package, Applications, Application, Extensions, desktop8:Extension, desktop8:EventTracing, desktop8:Provider, desktop8:Channels]
---

# desktop8:Channels

Allows one or more channels to be specified for event tracing.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:EventTracing>`](element-desktop8-eventtracing.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Provider>`](element-desktop8-provider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:Channels>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:EventTracing>`](element-desktop8-eventtracing.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Provider>`](element-desktop8-provider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:Channels>`**

## Syntax

```xml
<desktop8:Channels>

  <!-- Child elements -->
  desktop8:ImportChannel{0,1000}
  desktop8:Channel{0,1000}

</desktop8:Channels>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop8:ImportChannel](element-desktop8-importchannel.md) | Specifies an imported channel to be used for event tracing. |
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Provider](element-desktop8-provider.md) | Registers a provider to Event Tracing and enables its functionality. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
