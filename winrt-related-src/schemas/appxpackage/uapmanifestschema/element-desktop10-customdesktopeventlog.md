---
title: desktop10:CustomDesktopEventLog
description: Defines a custom event log.
ms.date: 10/12/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Extensions, desktop10:Extension, desktop10:CustomDesktopEventLog]
---

# desktop10:CustomDesktopEventLog

Defines a custom event log.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:CustomDesktopEventLog>`**

## Syntax

```xml
<desktop10:CustomDesktopEventLog
  CustomEventLogName = 'A required string between 1 and 2048 characters in length.'
  DisplayNameFile = 'An optional package-relative path to a DLL or EXE message resource file.'
  DisplayNameID = 'An optional unsigned integer between 0 and 4294967295.'
  MaxSize = 'An optional unsigned integer between 0 and 4294967295.'
  PrimaryModule = 'An optional string between 1 and 2048 characters in length.'
  Retention = 'An optional unsigned integer between 0 and 4294967295.' >

  <!-- Child elements -->
  desktop10:CustomEventSources

</desktop10:CustomDesktopEventLog>
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **CustomEventLogName** |  The name of the custom event log. Used as the registry key name.  | A string between 1 and 2048 characters in length. | Yes |  |
| **DisplayNameFile** | File containing the localized event log name. If specified, `DisplayNameID` must also be specified. | A package-relative path ending in the case-insensitive file extension `.dll` or `.exe`. | No | |
| **DisplayNameID** | The resource ID of the event log name within `DisplayNameFile`. If specified, `DisplayNameFile` must also be specified. | An unsigned integer between 0 and 4294967295. | No | |
| **MaxSize** |  Maximum size of the event log file, in bytes.  | An optional unsigned integer between 0 and 4294967295. | No |  |
| **PrimaryModule** |  The name of the subkey that contains the default values for the entries in the subkey for the event source.  | An optional string between 1 and 2048 characters in length. | No |  |
| **Retention** |  Specifies whether events get overwritten or discarded when the log reaches *MaxSize*. If this value is 0, the records of events are always overwritten. If this value is any nonzero value, records are never overwritten. When the log file reaches its maximum size, you must clear the log manually; otherwise, new events are discarded. The default value is 0.  | An optional unsigned integer between 0 and 4294967295. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop10:CustomEventSources](element-desktop10-customeventsources.md) | Required. Contains 1 to 16,384 event sources registered within this log. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11, version 22H2 (Build 22621) |

## Remarks

For more information on custom event logs, see [Eventlog Key](/windows/win32/eventlog/eventlog-key).

Declare this element inside a `desktop10:Extension` with `Category="windows.customDesktopEventLog"` and `desktop7:Scope="machine"`. Declare the desktop7 namespace (`http://schemas.microsoft.com/appx/manifest/desktop/windows10/7`) along with desktop10. This extension requires the `Microsoft.classicAppCompatElevated_8wekyb3d8bbwe` custom capability. Custom capabilities require authorization; see [Custom capabilities](/windows/uwp/packaging/app-capability-declarations#custom-capabilities).

The extension must be declared under package-level `Extensions`, not under an application's `Extensions`.

`DisplayNameFile` and `DisplayNameID` must either both be present or both be omitted. The manifest is rejected if only one is present. The same pairing rule applies to `CategoryCount` and `CategoryMessageFile` on each [desktop10:CustomEventSource](element-desktop10-customeventsource.md).

## Examples

This extension defines a log and one event source. The example assumes the package contains `ContosoMessages.dll` with the appropriate message resources and is authorized to use the required custom capability.

```xml
<desktop10:Extension Category="windows.customDesktopEventLog"
                     desktop7:Scope="machine">
  <desktop10:CustomDesktopEventLog CustomEventLogName="Contoso Log">
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
  </desktop10:CustomDesktopEventLog>
</desktop10:Extension>
```
