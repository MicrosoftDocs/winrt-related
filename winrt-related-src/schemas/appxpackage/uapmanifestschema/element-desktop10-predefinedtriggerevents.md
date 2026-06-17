---
title: desktop10:PredefinedTriggerEvents
description: Describes predefined trigger events for the current service.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:Service, desktop10:TriggerEvents, desktop10:PredefinedTriggerEvents]
---

# desktop10:PredefinedTriggerEvents

Describes predefined trigger events for the current service.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:Service>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:TriggerEvents>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:PredefinedTriggerEvents>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:Service>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:TriggerEvents>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:PredefinedTriggerEvents>`**

## Syntax

```xml
<desktop10:PredefinedTriggerEvents
  Action = 'A required string that can have one of the following values: "ActionStart", or "ActionStop".'
  Subtype = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  TriggerType = 'A required string that can have one of the following values: "deviceInterfaceArrival", "domainJoin", "firewallPortEvent", "groupPolicy", "ipAddressAvailability", or "networkEndpoint".' >

  <!-- Child elements -->
  desktop10:StringData{0,10000}
  desktop10:BinaryData{0,10000}
  desktop10:LevelData{0,10000}
  desktop10:KeywordAnyData{0,10000}
  desktop10:KeywordAllData{0,10000}

</desktop10:PredefinedTriggerEvents>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Action** |  The action type for the trigger event.  | A string that can have one of the following values: *ActionStart*, *ActionStop*. | Yes |  |
| **Subtype** |  A GUID that identifies the trigger event subtype.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **TriggerType** |  The trigger type.  | A string that can have one of the following values: *deviceInterfaceArrival*, *domainJoin*, *firewallPortEvent*, *groupPolicy*, *ipAddressAvailability*, *networkEndpoint*. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| **desktop10:StringData** | <!-- TODO: Add description --> |
| **desktop10:BinaryData** | <!-- TODO: Add description --> |
| **desktop10:LevelData** | <!-- TODO: Add description --> |
| **desktop10:KeywordAnyData** | <!-- TODO: Add description --> |
| **desktop10:KeywordAllData** | <!-- TODO: Add description --> |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
