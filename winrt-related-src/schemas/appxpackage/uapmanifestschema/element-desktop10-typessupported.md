---
title: desktop10:TypesSupported
description: Defines 1 or more of the event log types supported by the event source.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
---

# desktop10:TypesSupported

Defines 1 or more of the event log types supported by the event source.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:CustomDesktopEventLog\>](element-desktop10-customdesktopeventlog.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:CustomEventSource\>](element-desktop10-customeventsource.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:TypesSupported\>**

## Syntax

```xml
<desktop10:TypesSupported>

  <!-- Child Elements -->
  desktop10:TypeSupported

</desktop10:TypesSupported>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop10:TypeSupported](element-desktop10-typesupported.md) | Specifies a supported event log type. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Remarks

For more information on event log types, see [Event Sources](/windows/win32/eventlog/event-sources).

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |
