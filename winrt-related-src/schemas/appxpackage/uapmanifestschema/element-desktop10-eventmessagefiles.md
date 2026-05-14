---
title: desktop10:EventMessageFiles
description: Defines 1 or more DLL files containing the language strings describing the events.
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 05/23/2022
ms.topic: reference
no-loc: [Package, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog, desktop10:CustomEventSource, desktop10:EventMessageFiles]
---

# desktop10:EventMessageFiles

Defines 1 or more DLL files containing the language strings describing the events.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomEventSource>`](element-desktop10-customeventsource.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:EventMessageFiles>`**  

## Syntax

```xml
<desktop10:EventMessageFiles>

  <!-- Child Elements -->
  desktop10:File{0,10000}

</desktop10:EventMessageFiles>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop10:File](element-desktop10-file.md) | Specifies an event log DLL within the package. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop10:CustomEventSource](element-desktop10-customeventsource.md) | Defines an event source within a custom event log. |

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |
