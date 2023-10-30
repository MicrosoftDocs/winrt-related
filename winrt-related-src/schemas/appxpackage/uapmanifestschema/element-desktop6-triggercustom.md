---

title: desktop6:TriggerCustom
description: Describes a trigger event for the current service.

ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:TriggerCustom

## Description

Describes a trigger event for the current service.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:Extension\>](element-desktop6-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:Service\>](element-desktop6-service.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:TriggerEvents\>](element-desktop6-triggerevents.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop6:TriggerCustom\>**

## Syntax

```xml
<desktop6:TriggerCustom
  Action = 'A string that can be one of The following values: "ActionStart" or "ActionStop".'
  Subtype = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  desktop6:StringData{0,1000}
  desktop6:BinaryData{0,1000}
  desktop6:LevelData{0,1000}
  desktop6:KeywordAnyData{0,1000}
  desktop6:KeywordAllData{0,1000}

</desktop6:TriggerCustom>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Action** | The action type for the trigger event. | A string that can be one of The following values: "ActionStart" or "ActionStop". | Yes |  |
| **Subtype** | A GUID that identifies the trigger event subtype. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

| Child element | Description |
|---------------|-------------|
| [desktop6:StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for the trigger event. |  
| [desktop6:BinaryData](element-desktop6-binarydata.md) | Specifies binary data for the trigger event.  |  
| [desktop6:LevelData](element-desktop6-leveldata.md) | Specifies a byte value for the trigger event. |  
| [desktop6:KeywordAnyData](element-desktop6-keywordanydata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  
| [desktop6:KeywordAllData](element-desktop6-keywordalldata.md) | Specifies a 64-bit unsigned integer value for the trigger event. |  

### Parent elements

| Parent element | Description |
|---------------|-------------|
| [TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |  

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |
