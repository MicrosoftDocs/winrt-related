---
title: rescap:AppLinks
description: Registers one or more deep links for a settings app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, rescap:Extension, rescap:SettingsApp, rescap:AppLinks]
---

# rescap:AppLinks

Registers one or more deep links for a settings app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:Extension>`](element-rescap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:SettingsApp>`](element-rescap-settingsapp.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap:AppLinks>`**  

## Syntax

```xml
<rescap:AppLinks>

  <!-- Child elements -->
  rescap:Link{1,5}

</rescap:AppLinks>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Registers a deep link from the settings page to the settings app. |  |  |  |
|  | Description |  |  |  |
|  | - |  |  |  |
|  | Registers deep link and search information for settings apps. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

| Child element | Description |
|-|-|
| [rescap:Link](element-rescap-link.md) | Registers a deep link from the settings page to the settings app. |

## Parent elements

| Parent element | Description |
|-|-|
| [rescap:SettingsApp](element-rescap-settingsapp.md) | Registers deep link and search information for settings apps. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
