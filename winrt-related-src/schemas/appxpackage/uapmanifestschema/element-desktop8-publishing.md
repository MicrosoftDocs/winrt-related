---
title: desktop8:Publishing
description: Provides access to the Publishing feature within an Event Tracing channel.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop
no-loc: [Package, Applications, Application, Extensions, desktop8:Extension, desktop8:EventTracing, desktop8:Provider, desktop8:Channels, desktop8:Channel, desktop8:Publishing]
---

# desktop8:Publishing

Provides access to the Publishing feature within an Event Tracing channel.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:EventTracing>`](element-desktop8-eventtracing.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Provider>`](element-desktop8-provider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Channels>`](element-desktop8-channels.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Channel>`](element-desktop8-channel.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:Publishing>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:EventTracing>`](element-desktop8-eventtracing.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Provider>`](element-desktop8-provider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Channels>`](element-desktop8-channels.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Channel>`](element-desktop8-channel.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:Publishing>`**

## Syntax

```xml
<desktop8:Publishing
  Level = 'An optional integer between 0 and 255.'
  Keywords = 'An optional positive integer between 0 and 18446744073709551615.'
  ControlGuid = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  BufferSize = 'An optional positive integer between 0 and 4294967295.'
  FileMax = 'An optional positive integer between 0 and 4294967295.'
  MinBuffers = 'An optional positive integer between 0 and 4294967295.'
  MaxBuffers = 'An optional positive integer between 0 and 4294967295.'
  Latency = 'An optional positive integer between 0 and 4294967295.'
  ClockType = 'An optional string that can have one of the following values: "systemTime", or "queryPerformanceCounter".'
  SidType = 'An optional string that can have one of the following values: "none", or "publishing".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Level** | Specifies the level for publishing. | An optional integer between 0 and 255. | No |  |
| **Keywords** | Specifies the keywords used for publishing. | An optional positive integer between 0 and 18446744073709551615. | No |  |
| **ControlGuid** | Specifies the GUID used for controlling publishing. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **BufferSize** | Specifies the buffer size during publishing. | An optional positive integer between 0 and 4294967295. | No |  |
| **FileMax** | Specifies the maximum file size for publishing. | An optional positive integer between 0 and 4294967295. | No |  |
| **MinBuffers** | Specifies the minimum buffer size during publshing. | An optional positive integer between 0 and 4294967295. | No |  |
| **MaxBuffers** | Specifies the maximum buffer size during publishing. | An optional positive integer between 0 and 4294967295. | No |  |
| **Latency** | Specifies the latency to accept when publishing. | An optional positive integer between 0 and 4294967295. | No |  |
| **ClockType** | Specifies the clock type to be used during publishing. | An optional string that can have one of the following values: *systemTime*, *queryPerformanceCounter*. | No | systemTime |
| **SidType** | Specifies the security identifier type for publishing. | An optional string that can have one of the following values: *none*, *publishing*. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Channel](element-desktop8-channel.md) | Specifies a channel to be used for event tracing. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
