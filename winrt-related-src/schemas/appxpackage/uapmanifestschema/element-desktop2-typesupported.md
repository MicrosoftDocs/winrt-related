---
title: desktop2:TypeSupported
description: Specifies the types of events that are supported.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop2:Extension, desktop2:DesktopEventLogging, desktop2:TypesSupported, desktop2:TypeSupported]
---

# desktop2:TypeSupported

Specifies the types of events that are supported.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:DesktopEventLogging>`](element-desktop2-desktopeventlogging.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:TypesSupported>`](element-desktop2-typessupported.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:TypeSupported>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:DesktopEventLogging>`](element-desktop2-desktopeventlogging.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:TypesSupported>`](element-desktop2-typessupported.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:TypeSupported>`**

## Syntax

```xml
<desktop2:TypeSupported
  Value = 'A required string that can have one of the following values: "EVENTLOG_AUDIT_FAILURE", "EVENTLOG_AUDIT_SUCCESS", "EVENTLOG_ERROR_TYPE", "EVENTLOG_INFORMATION_TYPE", or "EVENTLOG_WARNING_TYPE".' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Value** | The value of event log types supported. | A string that can have one of the following values: *EVENTLOG_AUDIT_FAILURE*, *EVENTLOG_AUDIT_SUCCESS*, *EVENTLOG_ERROR_TYPE*, *EVENTLOG_INFORMATION_TYPE*, *EVENTLOG_WARNING_TYPE*. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop2:TypesSupported](element-desktop2-typessupported.md) | Contains the event log types that are supported. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
