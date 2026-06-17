---
title: desktop6:TriggerCustom
description: Describes a trigger event for the current service.

ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop6:Extension, desktop6:Service, desktop6:TriggerEvents, desktop6:TriggerCustom]
---

# desktop6:TriggerCustom

Describes a trigger event for the current service.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Service>`](element-desktop6-service.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:TriggerEvents>`](element-desktop6-triggerevents.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:TriggerCustom>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Service>`](element-desktop6-service.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:TriggerEvents>`](element-desktop6-triggerevents.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:TriggerCustom>`**

## Syntax

```xml
<desktop6:TriggerCustom
  Action = 'A required string that can have one of the following values: "ActionStart", or "ActionStop".'
  Subtype = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  desktop6:StringData{1,10000}
  desktop6:BinaryData{1,10000}
  desktop6:LevelData{1,10000}
  desktop6:KeywordAnyData{1,10000}
  desktop6:KeywordAllData{1,10000}

</desktop6:TriggerCustom>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Action** | The action type for the trigger event. | A string that can have one of the following values: *ActionStart*, *ActionStop*. | Yes |  |
| **Subtype** | A GUID that identifies the trigger event subtype. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop6:StringData](element-desktop6-stringdata.md) | Specifies one or more string data values for a trigger event of a service. |
| [desktop6:BinaryData](element-desktop6-binarydata.md) | Specifies binary data for a trigger event of a service. |
| [desktop6:LevelData](element-desktop6-leveldata.md) | Specifies a byte value for a trigger event of a service. |
| [desktop6:KeywordAnyData](element-desktop6-keywordanydata.md) | Specifies a 64-bit unsigned integer value for a trigger event of a service. |
| [desktop6:KeywordAllData](element-desktop6-keywordalldata.md) | Specifies a 64-bit unsigned integer value for a trigger event of a service. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
