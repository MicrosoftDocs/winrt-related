---
title: desktop10:PredefinedTriggerEvents
description: Describes predefined trigger events for the current service.
ms.date: 06/10/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop10:PredefinedTriggerEvents

Describes predefined trigger events for the current service.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop10:Extension\>](element-desktop10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop10:PredefinedTriggerEvents\>**

## Syntax

```xml
<desktop10:PredefinedTriggerEvents
  Action = 'A string that can have one of the following values: "ActionStart" or "ActionStop".'  
  Subtype = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  TriggerType = 'A string that can have one of the following values: "DeviceInterfaceArrival", "DomainJoin", "FirewallPortEvent", "GroupPolicy", "IPAddressAvailability", or "NetworkEndpoint".' >

  desktop10:StringData{0,1000}
  desktop10:BinaryData{0,1000}
  desktop10:LevelData{0,1000}
  desktop10:KeywordAnyData{0,1000}
  desktop10:KeywordAllData{0,1000}

</desktop10:PredefinedTriggerEvents>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Action** | The action type for the trigger event. | A string that can have one of the following values: *ActionStart* or *ActionStop*. | Yes |  |
| **Subtype**  | A GUID that identifies the trigger event subtype. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  | Yes |  |
| **TriggerType**  | The trigger type. | A string that can have one of the following values: *DeviceInterfaceArrival*, *DomainJoin*, *FirewallPortEvent*, *GroupPolicy*, *IPAddressAvailability*, or *NetworkEndpoint*. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop6:StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for the trigger event. |  
| [desktop6:BinaryData](element-desktop6-binarydata.md) | Specifies binary data for the trigger event.  |  
| [desktop6:LevelData](element-desktop6-leveldata.md) | Specifies a byte value for the trigger event. |  
| [desktop6:KeywordAnyData](element-desktop6-keywordanydata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  
| [desktop6:KeywordAllData](element-desktop6-keywordalldata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  

### Parent elements

| Parent element | Description |
|-|-|
| [dekstop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app (in Package/Extensions; desktop10:Extension). |  

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Item  | Value  |
|--|--|
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |
