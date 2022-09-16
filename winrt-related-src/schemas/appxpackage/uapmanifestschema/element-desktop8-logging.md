---
title: desktop8:Logging
description: Provides access to the Logging feature within an Event Tracing channel.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Logging

Provides access to the Logging feature within an Event Tracing channel.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:EventTracing\>](element-desktop8-eventtracing.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Provider\>](element-desktop8-provider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Channels\>](element-desktop8-channels.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Channel\>](element-desktop8-channel.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:Logging\>**

## Syntax

```xml
<desktop8:Logging
  Autobackup = 'An optional boolean value. Specifies whether or not logs should be automatically backed up.'
  Retention = 'An optional boolean value. Specifies whether or not logs should be saved.'
  MaxSize = 'An optional decimal number value specifying the maximum size of the logging file.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Autobackup** | Specifies whether or not logs should be automatically backed up. | An optional boolean value. | No |  |
| **Retention** | Specifies whether or not logs should be saved. | An optional boolean value. | No |  |
| **MaxSize** | Specifies the maximum size of the logging file. | An optional decimal number value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
