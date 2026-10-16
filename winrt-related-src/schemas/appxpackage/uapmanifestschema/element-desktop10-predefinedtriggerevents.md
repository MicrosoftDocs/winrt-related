---
title: desktop10:PredefinedTriggerEvents
description: Describes predefined trigger events for the current service.
ms.date: 10/12/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop6:Extension, desktop6:Service, desktop6:TriggerEvents, desktop7:Extension, desktop7:Service, desktop7:TriggerEvents, desktop10:PredefinedTriggerEvents]
---

# desktop10:PredefinedTriggerEvents

Describes predefined trigger events for the current service.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Service>`](element-desktop6-service.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:TriggerEvents>`](element-desktop6-triggerevents.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:PredefinedTriggerEvents>`**

This element can also appear in `desktop7:TriggerEvents` within a [desktop7:Service](element-desktop7-service.md). In that case, the enclosing extension and service use the desktop7 namespace; `PredefinedTriggerEvents` still uses desktop10.

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

The data elements form a choice: any combination of the five child types is allowed, with a combined total of zero to 10,000 children.

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Action** |  The action type for the trigger event.  | A string that can have one of the following values: *ActionStart*, *ActionStop*. | Yes |  |
| **Subtype** | A GUID that identifies the trigger event subtype. Its meaning depends on `TriggerType`; for example, a device interface class GUID for `deviceInterfaceArrival`, or `DOMAIN_JOIN_GUID` or `DOMAIN_LEAVE_GUID` for `domainJoin`. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes | |
| **TriggerType** |  The trigger type.  | A string that can have one of the following values: *deviceInterfaceArrival*, *domainJoin*, *firewallPortEvent*, *groupPolicy*, *ipAddressAvailability*, *networkEndpoint*. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| **desktop10:StringData** | Supplies string data for the trigger. Contains 1 to 10,000 [desktop6:DataItem](element-desktop6-dataitem.md) children, each with a required `Value` attribute. |
| **desktop10:BinaryData** | Supplies binary data for the trigger. Its required `File` attribute identifies the file containing the data. |
| **desktop10:LevelData** | Supplies a byte value for the trigger. Its required `Value` attribute is an unsigned integer from 0 to 255. |
| **desktop10:KeywordAnyData** | Supplies an any-keyword mask for the trigger. Its required `Value` attribute is an unsigned 64-bit integer. |
| **desktop10:KeywordAllData** | Supplies an all-keyword mask for the trigger. Its required `Value` attribute is an unsigned 64-bit integer. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |
| **desktop7:TriggerEvents** | Describes one or more trigger events within a [desktop7:Service](element-desktop7-service.md). |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11, version 22H2 (Build 22621) |

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

Declare the enclosing `windows.service` extension under the application's `Extensions` element, not under package-level `Extensions`.

The schema reuses the desktop6 data types, but the immediate data children of `PredefinedTriggerEvents` use the desktop10 namespace. In particular, `desktop10:StringData` contains `desktop6:DataItem` children.

The trigger type determines which subtype and data are meaningful. Not every schema-valid combination represents a valid service trigger. For the subtype GUIDs and trigger-specific data requirements, see [SERVICE_TRIGGER](/windows/win32/api/winsvc/ns-winsvc-service_trigger).

## Examples

This application-level service extension configures a trigger to start a service when the computer joins a domain. The subtype is `DOMAIN_JOIN_GUID`; this trigger does not use data children. The package must supply `ContosoService.exe` and declare the appropriate service capability.

```xml
<desktop6:Extension Category="windows.service"
                    Executable="ContosoService.exe"
                    EntryPoint="Windows.FullTrustApplication">
  <desktop6:Service Name="ContosoService"
                    StartupType="manual"
                    StartAccount="localService">
    <desktop6:TriggerEvents>
      <desktop10:PredefinedTriggerEvents
        Action="ActionStart"
        Subtype="1ce20aba-9851-4421-9430-1ddeb766e809"
        TriggerType="domainJoin" />
    </desktop6:TriggerEvents>
  </desktop6:Service>
</desktop6:Extension>
```
