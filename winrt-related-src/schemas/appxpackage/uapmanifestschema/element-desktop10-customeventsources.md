---
title: desktop10:CustomEventSources
description: Contains the event sources registered within a custom event log.
ms.date: 10/12/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog, desktop10:CustomEventSources, desktop10:CustomEventSource]
---

# desktop10:CustomEventSources

Contains the event sources registered within a custom event log.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSources>`**

## Syntax

```xml
<desktop10:CustomEventSources>

  desktop10:CustomEventSource{1,16384}

</desktop10:CustomEventSources>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Defines an event source within the custom event log. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:CustomDesktopEventLog](element-desktop10-customdesktopeventlog.md) | Defines a custom event log. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11, version 22H2 (Build 22621) |

## Remarks

`CustomEventSources` is a required child of `CustomDesktopEventLog`. The manifest schema permits 1 to 16,384 sources in this container. Windows Event Log limits also apply; see [Event Sources](/windows/win32/eventlog/event-sources).

For extension declaration and capability prerequisites, see [desktop10:CustomDesktopEventLog](element-desktop10-customdesktopeventlog.md#remarks).

## Examples

```xml
<desktop10:CustomEventSources>
  <desktop10:CustomEventSource EventSourceName="Contoso App">
    <desktop10:EventMessageFiles>
      <desktop10:File Path="ContosoMessages.dll" />
    </desktop10:EventMessageFiles>
    <desktop10:TypesSupported>
      <desktop10:TypeSupported Value="informationType" />
    </desktop10:TypesSupported>
  </desktop10:CustomEventSource>
</desktop10:CustomEventSources>
```

`ContosoMessages.dll` represents a message resource module that must be included in the package.
