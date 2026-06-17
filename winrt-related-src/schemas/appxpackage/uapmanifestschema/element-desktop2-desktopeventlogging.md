---
title: desktop2:DesktopEventLogging
description: Enables Windows Desktop Bridge apps to register for Windows event logging.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop2:Extension, desktop2:DesktopEventLogging]
---

# desktop2:DesktopEventLogging

Enables Windows Desktop Bridge apps to register for Windows event logging.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:DesktopEventLogging>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop2:Extension>`](element-desktop2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop2:DesktopEventLogging>`**

## Syntax

```xml
<desktop2:DesktopEventLogging
  AppName = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  desktop2:EventMessageFiles
  desktop2:TypesSupported

</desktop2:DesktopEventLogging>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AppName** |  The name of the app that will use desktop event logging.  | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop2:EventMessageFiles](element-desktop2-eventmessagefiles.md) | Contains event message files. |
| [desktop2:TypesSupported](element-desktop2-typessupported.md) | Contains the event log types that are supported. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
