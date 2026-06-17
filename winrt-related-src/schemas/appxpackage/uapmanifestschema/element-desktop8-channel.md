---
title: desktop8:Channel
description: Specifies a channel to be used for event tracing.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop
no-loc: [Package, Applications, Application, Extensions, desktop8:Extension, desktop8:EventTracing, desktop8:Provider, desktop8:Channels, desktop8:Channel]
---

# desktop8:Channel

Specifies a channel to be used for event tracing.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:EventTracing>`](element-desktop8-eventtracing.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Provider>`](element-desktop8-provider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Channels>`](element-desktop8-channels.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:Channel>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Extension>`](element-desktop8-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:EventTracing>`](element-desktop8-eventtracing.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Provider>`](element-desktop8-provider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop8:Channels>`](element-desktop8-channels.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop8:Channel>`**

## Syntax

```xml
<desktop8:Channel
  Name = 'A required string between 1 and 2084 characters in length in the form of a valid URI.'
  Type = 'A required string that can have one of the following values: "admin", "operational", "analytic", "analytic", or "debug".'
  Access = 'An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).'
  Isolation = 'An optional string that can have one of the following values: "application", "system", or "custom".'
  Enabled = 'An optional boolean value.' >

  <!-- Child elements -->
  desktop8:Logging?
  desktop8:Publishing?

</desktop8:Channel>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the channel. | A string between 1 and 2084 characters in length in the form of a valid URI. | Yes |  |
| **Type** | The type of the channel. | A string that can have one of the following values: *admin*, *operational*, *analytic*, *analytic*, *debug*. | Yes |  |
| **Access** | The access level of the channel. | An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). | No |  |
| **Isolation** | Specifies the channel's isolation attribute. | An optional string that can have one of the following values: *application*, *system*, *custom*. | No |  |
| **Enabled** | Specifies whether or not the channel is enabled. | An optional boolean value. | No | false |

## Child elements

| Child element | Description |
|-|-|
| [desktop8:Logging](element-desktop8-logging.md) | Provides access to the Logging feature within an Event Tracing channel. |
| [desktop8:Publishing](element-desktop8-publishing.md) | Provides access to the Publishing feature within an Event Tracing channel. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
