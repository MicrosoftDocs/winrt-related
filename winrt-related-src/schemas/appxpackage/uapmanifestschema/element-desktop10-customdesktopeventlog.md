---
title: desktop10:CustomDesktopEventLog
description: Defines a custom event log.
keywords: windows 10, uwp, schema, manifest, desktop, extension

ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:CustomDesktopEventLog

## Description

Defines a custom event log.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd><strong>&lt;desktop10:CustomDesktopEventLog&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:CustomDesktopEventLog
  CustomEvenLogName? = A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.
  DisplayNameFile?   = A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", |, ?, or *.
  DisplayNameID?     = An unsigned integer value. A number between -2147483648 and 2147483647.
  MaxSize?           = An unsigned integer value. A number between -2147483648 and 2147483647.
  PrimaryModule?     = A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.
  Retention?         = An unsigned integer value. A number between -2147483648 and 2147483647.
  >
  <!-- Child Elements -->
  desktop10:CustomEventSource{0, 16384}
</desktop10:CustomDesktopEventLog>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| CustomEventLogName | The name of the custom event log. Used as the registry key name. | A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | No |
| DisplayNameFile | DLL file that contains the language strings to use for name of this event log. | A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| DisplayNameID | The ID number of the language string within the *DisplayNameFile* to use for the event log name. | An unsigned integer value. A number between -2147483648 and 2147483647. | No |
| MaxSize | Maximum size of the event log file, in bytes. | An unsigned integer value. A number between -2147483648 and 2147483647. | No |
| PrimaryModule | The name of the subkey that contains the default values for the entries in the subkey for the event source. | A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | No |
| Retention | Specifies whether events get overwritten or discarded when the log reaches *MaxSize*. If this value is 0, the records of events are always overwritten. If this value is any nonzero value, records are never overwritten. When the log file reaches its maximum size, you must clear the log manually; otherwise, new events are discarded. The default value is 0. | An unsigned integer value. A number between -2147483648 and 2147483647. | No |

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Defines an event source within a custom event log. |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Remarks

For more information on custom event logs, see [Eventlog Key](/windows/win32/eventlog/eventlog-key).

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |