---
title: desktop8:Channels
description: Allows one or more channels to be specified for event tracing.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Channels

Allows one or more channels to be specified for event tracing.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:EventTracing\>](element-desktop8-eventtracing.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Provider\>](element-desktop8-provider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:Channels\>**

## Syntax

```xml
<desktop8:Channels>

  <!-- Child Elements -->
  desktop8:Channel
  desktop8:ImportChannel

</desktop8:Channels>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |
| [desktop8:ImportChannel](element-desktop8-importchannel.md) | Specifies an imported channel to be used for event tracing. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Provider](element-desktop8-provider.md) | Registers a provider to Event Tracing and enables its functionality. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
