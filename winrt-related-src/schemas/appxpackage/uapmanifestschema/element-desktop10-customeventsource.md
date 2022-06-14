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

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">desktop10:Extension</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-customdesktopeventlog.md">&lt;desktop10:CustomDesktopEventLog&gt;</a></dt>
<dd><strong>&lt;desktop10:CustomEventSource&gt;</strong></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop10:CustomEventSource
  EventSourceName      = A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values.
  CategoryCount?       = An unsigned integer value. A number between -2147483648 and 2147483647.
  CategoryMessageFile? = A string between 1 and 256 characters in length and cannot contain these characters: <, >, :, ", |, ?, or *.
  >

  <!-- Child Elements -->
  desktop10:CustomEventSource
  desktop10:TypesSupported

</desktop10:CustomEventSource>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| EventSourceName | The name of the custom event source. Used as the registry key name. | A string value between 1 and 32767 characters in length that cannot start or end with a whitespace character. May contain whitespace characters in between the first and last values. | Yes |
| CategoryCount | Number of event categories supported. | An unsigned integer value. A number between -2147483648 and 2147483647. | No |
| CategoryMessageFile | Path to the category message file. A category message file contains language-dependent strings that describe the categories.  | A string between 1 and 256 characters in length and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |

### Child Elements

| Child element | Description |
|-|-|
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Defines 1 or more DLL files containing the language strings describing the events. |
| [desktop10:TypesSupported](element-desktop10-typessupported.md) | Defines 1 or more of the event log types supported by the event source. |

### Parent Elements

| Parent element | Description |
|-|-|
| [desktop10:CustomDesktopEventLog](element-desktop10-customdesktopeventlog.md) | Declares an extensibility point for the app. |

## Remarks

For more information on custom event sources, see [Event Sources](/windows/win32/eventlog/event-sources).

## Requirements

| Namespace | Value |
|-|-|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |