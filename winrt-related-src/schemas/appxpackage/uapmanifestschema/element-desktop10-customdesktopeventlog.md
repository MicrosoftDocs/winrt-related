---
title: desktop10:CustomDesktopEventLog
description: Defines a custom event log.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:CustomDesktopEventLog

Defines a custom event log.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:CustomDesktopEventLog\>**

## Syntax

```xml
<desktop10:CustomDesktopEventLog
  CustomEvenLogName = 'An optional string with a value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.'
  DisplayNameFile = 'An optional string with a value between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  DisplayNameID = 'An optional unsigned integer value. A number between -2147483648 and 2147483647.'
  MaxSize = 'An optional unsigned integer value. A number between -2147483648 and 2147483647.'
  PrimaryModule = 'An optional string with a value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.'
  Retention = 'An optional unsigned integer value. A number between -2147483648 and 2147483647.' >

  <!-- Child Elements -->
  desktop10:CustomEventSource{0, 16384}

</desktop10:CustomDesktopEventLog>
```

### Key

`{}` a specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **CustomEventLogName** | The name of the custom event log. Used as the registry key name. | An optional string with a value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | No |  |
| **DisplayNameFile** | DLL file that contains the language strings to use for name of this event log. | An optional string with a value between 1 and 256 characters in length that must end with `.dll` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **DisplayNameID** | The ID number of the language string within the *DisplayNameFile* to use for the event log name. | An optional unsigned integer value. A number between -2147483648 and 2147483647. | No |  |
| **MaxSize** | Maximum size of the event log file, in bytes. | An optional unsigned integer value. A number between -2147483648 and 2147483647. | No |  |
| **PrimaryModule** | The name of the subkey that contains the default values for the entries in the subkey for the event source. | An optional string with a value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | No |  |
| **Retention** | Specifies whether events get overwritten or discarded when the log reaches *MaxSize*. If this value is 0, the records of events are always overwritten. If this value is any nonzero value, records are never overwritten. When the log file reaches its maximum size, you must clear the log manually; otherwise, new events are discarded. The default value is 0. | An optional unsigned integer value. A number between -2147483648 and 2147483647. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Defines an event source within a custom event log. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Remarks

For more information on custom event logs, see [Eventlog Key](/windows/win32/eventlog/eventlog-key).

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |
