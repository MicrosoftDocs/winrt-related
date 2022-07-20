---

title: desktop10:PredefinedTriggerEvents
description: Describes predefined trigger events for the current service.
ms.date: 06/10/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop10:PredefinedTriggerEvents

## Description

Describes predefined trigger events for the current service.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop10-extension.md">&lt;desktop10:Extension&gt;</a></dt>
<dd><b>&lt;desktop10:PredefinedTriggerEvents&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```xml
<desktop10:PredefinedTriggerEvents    Action   =  The following values are supported: ActionStart, ActionStop  
                           Subtype  =  A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
                           TriggerType  =  The following values are supported: DeviceInterfaceArrival, DomainJoin, FirewallPortEvent, GroupPolicy, IPAddressAvailability, and NetworkEndpoint >
    ( desktop10:StringData{0,1000}
      desktop10:BinaryData{0,1000}
      desktop10:LevelData{0,1000}
      desktop10:KeywordAnyData{0,1000}
      desktop10:KeywordAllData{0,1000} )
</desktop10:PredefinedTriggerEvents>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Action | The action type for the trigger event. | The following values are supported: **ActionStart**, **ActionStop** | Yes |
| Subtype  | A GUID that identifies the trigger event subtype. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  | Yes |
| TriggerType  | The trigger type. | The following values are supported: **DeviceInterfaceArrival**, **DomainJoin**, **FirewallPortEvent**, **GroupPolicy**, **IPAddressAvailability**, and **NetworkEndpoint**.   | Yes |


### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop6:StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for the trigger event. |  
| [desktop6:BinaryData](element-desktop6-binarydata.md) | Specifies binary data for the trigger event.  |  
| [desktop6:LevelData](element-desktop6-leveldata.md) | Specifies a byte value for the trigger event. |  
| [desktop6:KeywordAnyData](element-desktop6-keywordanydata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  
| [desktop6:KeywordAllData](element-desktop6-keywordalldata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [dekstop10:Extension](element-desktop10-extension.md) | Declares an extensibility point for the app (in Package/Extensions; desktop10:Extension). |  


## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).


## Requirements

| Namespace     |        Value                                                     |
|---------------|-------------------------------------------------------------|
| desktop10 | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |