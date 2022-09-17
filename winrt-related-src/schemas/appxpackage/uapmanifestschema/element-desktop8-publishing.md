---
title: desktop8:Publishing
description: Provides access to the Publishing feature within an Event Tracing channel.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Publishing

Provides access to the Publishing feature within an Event Tracing channel.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:EventTracing\>](element-desktop8-eventtracing.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Provider\>](element-desktop8-provider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Channels\>](element-desktop8-channels.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Channel\>](element-desktop8-channel.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:Publishing\>**

## Syntax

```xml
<desktop8:Publishing
  Level = 'An optional number with a value between 0 and 127 characters.'
  Keywords = 'An optional string with a value between 0 and 4294967295 characters.'
  ControlGuid = 'An optional hexadecimal string that may only contain the following values: "0-9" or "A-F" (uppercase or lowercase) representing the unique identifier of the provider.'
  BufferSize = 'An optional integer value.'
  FileMax = 'An optional integer value.'
  MinBuffers = 'An optional integer value.'
  MaxBuffers = 'An optional integer value.'
  Latency = 'An optional integer value.'
  ClockType = 'An optional string that can have one of the following values: "systemTime" or "queryPerformanceCounter".'
  SidType = 'A string that can have one of the following values: "none" or "publishing".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Level** | Specifies the level for publishing. | An optional number with a value between 0 and 127 characters. | No |  |
| **Keywords** | Specifies the keywords used for publishing. | An optional string with a value between 0 and 4294967295 characters. | No |  |
| **ControlGuid** | Specifies the GUID used for controlling publishing. | An optional hexadecimal string that may only contain the following values: `0-9` or `A-F` (uppercase or lowercase) representing the unique identifier of the provider. | No |  |
| **BufferSize** | Specifies the buffer size during publishing. | An optional integer value. | No |  |
| **FileMax** | Specifies the maximum file size for publishing. | An optional integer value. | No |  |
| **MinBuffers** | Specifies the minimum buffer size during publshing. | An optional integer value. | No |  |
| **MaxBuffers** | Specifies the maximum buffer size during publishing. | An optional integer value. | No |  |
| **Latency** | Specifies the latency to accept when publishing. | An optional integer value. | No |  |
| **ClockType** | Specifies the clock type to be used during publishing. | An optional string that can have one of the following values: *systemTime* or *queryPerformanceCounter*. | No |  |
| **SidType** | Specifies the security identifier type for publishing. | A string that can have one of the following values: *none* or *publishing*. | No |  |

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
