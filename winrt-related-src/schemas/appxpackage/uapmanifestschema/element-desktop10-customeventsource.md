---
title: desktop10:CustomEventSource
description: Defines an event source within a custom event log.
ms.date: 10/12/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog, desktop10:CustomEventSources, desktop10:CustomEventSource]
---

# desktop10:CustomEventSource

Defines an event source within a custom event log.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomDesktopEventLog>`](element-desktop10-customdesktopeventlog.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:CustomEventSources>`](element-desktop10-customeventsources.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomEventSource>`**

## Syntax

```xml
<desktop10:CustomEventSource
  EventSourceName = 'A required nonempty ASCII alphanumeric string that can contain internal whitespace.'
  CategoryCount = 'An optional unsigned integer between 0 and 4294967295.'
  CategoryMessageFile = 'An optional package-relative path to a DLL or EXE message resource file.' >

  <!-- Child elements -->
  desktop10:EventMessageFiles
  desktop10:TypesSupported

</desktop10:CustomEventSource>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **EventSourceName** | The name of the custom event source, used as its registry key name. Choose a name that satisfies the Windows Event Log naming rules. | A nonempty string of ASCII letters and digits, with whitespace permitted only between alphanumeric characters. | Yes | |
| **CategoryCount** | Number of event categories supported. If specified, `CategoryMessageFile` must also be specified. | An unsigned integer between 0 and 4294967295. | No | |
| **CategoryMessageFile** | Package-relative path to the file containing language-dependent category descriptions. If specified, `CategoryCount` must also be specified. | A package-relative path ending in the case-insensitive file extension `.dll` or `.exe`. | No | |

## Child elements

| Child element | Description |
|-|-|
| [desktop10:EventMessageFiles](element-desktop10-eventmessagefiles.md) | Required. Contains 1 to 10,000 message resource files. Each `desktop10:File` must have a distinct `Path` within this container. |
| [desktop10:TypesSupported](element-desktop10-typessupported.md) | Required. Contains 1 to 5 `desktop10:TypeSupported` entries with distinct `Value` attributes. |

Each child container must appear exactly once; they can appear in either order.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:CustomEventSources](element-desktop10-customeventsources.md) | Contains the event sources registered within a custom event log. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11, version 22H2 (Build 22621) |

## Remarks

For more information on custom event sources, see [Event Sources](/windows/win32/eventlog/event-sources).

`CategoryCount` and `CategoryMessageFile` must either both be present or both be omitted. The manifest is rejected if only one is present.

`TypesSupported` is required by the manifest schema. Do not treat its declaration as a runtime filter: the Windows Event Logging reference describes the corresponding legacy `TypesSupported` registry value as unused.

For the enclosing extension and capability prerequisites, see [desktop10:CustomDesktopEventLog](element-desktop10-customdesktopeventlog.md#remarks).

## Examples

This source supplies event messages without category descriptions. Replace the example file name with a message resource module included in the package.

```xml
<desktop10:CustomEventSource EventSourceName="Contoso App">
  <desktop10:EventMessageFiles>
    <desktop10:File Path="ContosoMessages.dll" />
  </desktop10:EventMessageFiles>
  <desktop10:TypesSupported>
    <desktop10:TypeSupported Value="informationType" />
    <desktop10:TypeSupported Value="errorType" />
  </desktop10:TypesSupported>
</desktop10:CustomEventSource>
```

To add category descriptions, supply both category attributes. The category resource module must contain the category messages corresponding to the count.

```xml
<desktop10:CustomEventSource EventSourceName="Contoso App Categories"
                             CategoryCount="2"
                             CategoryMessageFile="ContosoCategories.dll">
  <desktop10:EventMessageFiles>
    <desktop10:File Path="ContosoMessages.dll" />
  </desktop10:EventMessageFiles>
  <desktop10:TypesSupported>
    <desktop10:TypeSupported Value="informationType" />
  </desktop10:TypesSupported>
</desktop10:CustomEventSource>
```
