---
ms.assetid: dbddff21-f1f6-488d-9ad5-12a3365a00e3
title: desktop2:DesktopEventLogging
description: Enables Windows Desktop Bridge apps to register for Windows event logging.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:DesktopEventLogging

Enables Windows Desktop Bridge apps to register for Windows event logging.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[desktop2:Extension](element-desktop2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:DesktopEventLogging\>**

## Syntax

```xml
<desktop2:DesktopEventLogging
  AppName = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  desktop2:EventMessageFiles
  desktop2:TypesSupported

</desktop2:DesktopEventLogging>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AppName** | The name of the app that will use desktop event logging. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

### Child elements

| Child element | Description |
|-|-|
| [EventMessageFiles](element-desktop2-eventmessagefiles.md) | Contains event message files. |
| [TypesSupported](element-desktop2-typessupported.md) | Contains the event log types that are supported. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
