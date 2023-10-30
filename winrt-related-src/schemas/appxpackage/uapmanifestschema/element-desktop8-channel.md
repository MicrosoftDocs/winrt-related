---
title: desktop8:Channel
description: Specifies a channel to be used for event tracing.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Channel

Specifies a channel to be used for event tracing.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:EventTracing\>](element-desktop8-eventtracing.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Provider\>](element-desktop8-provider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Channels\>](element-desktop8-channels.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:Channel\>**

## Syntax

```xml
<desktop8:Channel
  Name = 'A string with a value between 1 and 2084 characters.'
  Type = 'A string that can be one of the following values: "admin", "operational", "analytic", or "debug".'
  Access = 'An alphanumeric string with a value between 1 and 2084 characters.'
  Isolation = 'A string that can be one of the following values: "application", "system", or "custom".'
  Enabled = 'A boolean value.' >

  <!-- Child Elements -->
  desktop8:Logging
  desktop8:Publishing

</desktop8:Channel>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the channel. | A string with a value between 1 and 2,084 characters. | Yes |  |
| **Type** | The type of the channel. | A string value that can be one of the following: *admin*, *operational*, *analytic*, or *debug*. | Yes |  |
| **Access** | The access level of the channel. | An alphanumeric string with a value between 1 and 2084 characters. | No |  |
| **Isolation** | Specifies the channel's isolation attribute. | A string that can be one of the following values: *application*, *system*, or *custom*. | No |  |
| **Enabled** | Specifies whether or not the channel is enabled. | A boolean value. | No | false |

### Child elements

| Child element | Description |
|-|-|
| [desktop8:Logging](element-desktop8-logging.md) | Provides access to the Logging feature within an Event Tracing channel. |
| [desktop8:Publishing](element-desktop8-publishing.md) | Provides access to the Publishing feature within an Event Tracing channel. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |
