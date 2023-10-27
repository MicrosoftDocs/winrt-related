---
title: desktop10:CustomEventSource
description: Defines an event source within a custom event log.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:CustomEventSource

## Description

Defines an event source within a custom event log.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:CustomDesktopEventLog\>](element-desktop10-customdesktopeventlog.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:CustomEventSource\>**

## Syntax

```xml
<desktop10:CustomEventSource
  EventSourceName = 'A string with a value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.'
  CategoryCount = 'An optional unsigned integer value. A number between -2147483648 and 2147483647.'
  CategoryMessageFile = 'A string with a value between 1 and 256 characters in length and cannot contain these characters: <, >, :, ", |, ?, or *.'
  >

  <!-- Child Elements -->
  desktop10:CustomEventSource
  desktop10:TypesSupported

</desktop10:CustomEventSource>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **EventSourceName** | The name of the custom event source. Used as the registry key name. | A string with a value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | Yes |
| **CategoryCount** | Number of event categories supported. | An optional unsigned integer value. A number between -2147483648 and 2147483647. | No |
| **CategoryMessageFile** | Path to the category message file. A category message file contains language-dependent strings that describe the categories.  | A string with a value between 1 and 256 characters in length and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |

### Child elements

| Child element | Description |
|-|-|
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Defines 1 or more DLL files containing the language strings describing the events. |
| [desktop10:TypesSupported](element-desktop10-typessupported.md) | Defines 1 or more of the event log types supported by the event source. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:CustomDesktopEventLog](element-desktop10-customdesktopeventlog.md) | Declares an extensibility point for the app. |

## Remarks

For more information on custom event sources, see [Event Sources](/windows/win32/eventlog/event-sources).

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| Minimum OS Version | Windows 11 version 22H2 (Build 22621) |
