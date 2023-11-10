---
title: desktop8:Provider
description: Registers a provider to Event Tracing and enables its functionality.
keywords: windows 10, uwp, schema, manifest, desktop
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Provider

Registers a provider to Event Tracing and enables its functionality.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:Extension\>](element-desktop8-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop8:EventTracing\>](element-desktop8-eventtracing.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop8:Provider\>**

## Syntax

```xml
<desktop8:Provider
  Id = 'A hexadecimal string that may only contain the following values: "0-9" or "A-F" (uppercase or lowercase) representing the unique identifier of the provider.'
  Name = 'A string with a value between 1 and 2084 characters in length that represents the name of the provider.'
  ResourceFile = 'A string value where the first character cannot contain any of the following: ".", "/", "\", or a space. Represents the path to a file.'
  MessageFile = 'A string value where the first character cannot contain any of the following: ".", "/", "\", or a space. Represents the path to a file.' >

  <!-- Child Elements -->
  desktop8:Channels

</desktop8:Provider>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The unique identifier for the provider. | A hexadecimal string that may only contain the following values: "0-9" or "A-F" (uppercase or lowercase) representing the unique identifier of the provider. | Yes |
| **Name** | The name of the provider. | A string with a value between 1 and 2084 characters in length that represents the name of the provider. | Yes |
| **ResourceFile** | Specifies the path to the provider resource files. | A string value where the first character cannot contain any of the following: `.`, `/`, `\`, or a space. Represents the path to a file. | Yes |
| **MessageFile** | Specifies the path to the provider message files. | A string value where the first character cannot contain any of the following: `.`, `/`, `\`, or a space. Represents the path to a file. | No |

### Child elements

| Child element | Description |
|-|-|
| [desktop8:Channels](element-desktop8-channels.md) | Allows one or more channels to be specified for event tracing. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop8:EventTracing](element-desktop8-eventtracing.md) | Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |
