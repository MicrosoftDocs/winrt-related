---
title: desktop10:File
description: Defines an event log DLL within the package.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog, desktop10:CustomEventSources, desktop10:CustomEventSource, desktop10:EventMessageFiles, desktop10:File]
---

# desktop10:File

Specifies an event log DLL within the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSources>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomEventSource>`](element-desktop10-customeventsource.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:EventMessageFiles>`](element-desktop10-eventmessagefiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:File>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSources>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomEventSource>`](element-desktop10-customeventsource.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:EventMessageFiles>`](element-desktop10-eventmessagefiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:File>`**

## Syntax

```xml
<desktop10:File
  Path = 'A required string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension `.dll` or `.exe`.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** |  The package-relative path to the event log dll. The path must be unique within the parent **EventMessageFiles** element.  | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension `.dll` or `.exe`. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Defines 1 or more DLL files containing the language strings describing the events. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
