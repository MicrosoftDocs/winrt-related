---
title: desktop10:CustomEventSource
description: Defines an event source within a custom event log.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog, desktop10:CustomEventSources, desktop10:CustomEventSource]
---

# desktop10:CustomEventSource

Defines an event source within a custom event log.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSources>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSource>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSources>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSource>`**

## Syntax

```xml
<desktop10:CustomEventSource
  EventSourceName = 'A required string between 1 and 2048 characters in length.'
  CategoryCount = 'An optional positive integer between 0 and 4294967295.'
  CategoryMessageFile = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension `.dll` or `.exe`.' >

  <!-- Child elements -->
  desktop10:EventMessageFiles
  desktop10:TypesSupported

</desktop10:CustomEventSource>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **EventSourceName** |  The name of the custom event source. Used as the registry key name.  | A string between 1 and 2048 characters in length. | Yes |  |
| **CategoryCount** |  Number of event categories supported.  | An optional positive integer between 0 and 4294967295. | No |  |
| **CategoryMessageFile** |  Path to the category message file. A category message file contains language-dependent strings that describe the categories.  | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension `.dll` or `.exe`. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Defines 1 or more DLL files containing the language strings describing the events. |
| [desktop10:TypesSupported](element-desktop10-typessupported.md) | Defines 1 or more of the event log types supported by the event source. |

## Parent elements

| Parent element | Description |
|-|-|
| **desktop10:CustomEventSources** | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

For more information on custom event sources, see [Event Sources](/windows/win32/eventlog/event-sources).

## Examples

<!-- Author content goes here -->
