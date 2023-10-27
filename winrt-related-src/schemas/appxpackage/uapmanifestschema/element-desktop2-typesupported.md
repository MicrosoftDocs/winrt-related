---
ms.assetid: 948fbf9b-c4c8-42d6-8659-04392d3c13f2
title: desktop2:TypeSupported
description: Specifies the types of events that are supported.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:TypeSupported

Specifies the types of events that are supported.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-package-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:DesktopEventLogging\>](element-desktop2-DesktopEventLogging.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:TypesSupported\>](element-desktop2-typessupported.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:TypeSupported\>**

## Syntax

```xml
<desktop2:TypeSupported
  Value = 'A string that can have one of the following values: "EVENTLOG_AUDIT_FAILURE", "EVENTLOG_AUDIT_SUCCESS", "EVENTLOG_ERROR_TYPE", "EVENTLOG_INFORMATION_TYPE", or "EVENTLOG_WARNING_TYPE".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Value** | The value of event log types supported. | A string that can have one of the following values: *EVENTLOG_AUDIT_FAILURE*, *EVENTLOG_AUDIT_SUCCESS*, *EVENTLOG_ERROR_TYPE*, *EVENTLOG_INFORMATION_TYPE*, or *EVENTLOG_WARNING_TYPE*. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:TypesSupported](element-desktop2-typessupported.md) | Contains the event log types that are supported. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
