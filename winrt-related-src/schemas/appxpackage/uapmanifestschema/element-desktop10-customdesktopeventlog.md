---
title: desktop10:CustomDesktopEventLog
description: Defines a custom event log.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog]
---

# desktop10:CustomDesktopEventLog

Defines a custom event log.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomDesktopEventLog>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomDesktopEventLog>`**

## Syntax

```xml
<desktop10:CustomDesktopEventLog
  CustomEventLogName = 'A required string between 1 and 2048 characters in length.'
  DisplayNameFile = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension `.dll` or `.exe`.'
  DisplayNameID = 'An optional positive integer between 0 and 4294967295.'
  MaxSize = 'An optional positive integer between 0 and 4294967295.'
  PrimaryModule = 'An optional string between 1 and 2048 characters in length.'
  Retention = 'An optional positive integer between 0 and 4294967295.' >

  <!-- Child elements -->
  desktop10:CustomEventSources

</desktop10:CustomDesktopEventLog>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **CustomEventLogName** |  The name of the custom event log. Used as the registry key name.  | A string between 1 and 2048 characters in length. | Yes |  |
| **DisplayNameFile** |  DLL file that contains the language strings to use for name of this event log.  | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension `.dll` or `.exe`. | No |  |
| **DisplayNameID** |  The ID number of the language string within the *DisplayNameFile* to use for the event log name.  | An optional positive integer between 0 and 4294967295. | No |  |
| **MaxSize** |  Maximum size of the event log file, in bytes.  | An optional positive integer between 0 and 4294967295. | No |  |
| **PrimaryModule** |  The name of the subkey that contains the default values for the entries in the subkey for the event source.  | An optional string between 1 and 2048 characters in length. | No |  |
| **Retention** |  Specifies whether events get overwritten or discarded when the log reaches *MaxSize*. If this value is 0, the records of events are always overwritten. If this value is any nonzero value, records are never overwritten. When the log file reaches its maximum size, you must clear the log manually; otherwise, new events are discarded. The default value is 0.  | An optional positive integer between 0 and 4294967295. | No |  |

## Child elements

| Child element | Description |
|-|-|
| **desktop10:CustomEventSources** | <!-- TODO: Add description --> |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

For more information on custom event logs, see [Eventlog Key](/windows/win32/eventlog/eventlog-key).

## Examples

<!-- Author content goes here -->
