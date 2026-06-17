---
title: rescap:Link
description: Registers a deep link from the settings page to the settings app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, rescap:Extension, rescap:SettingsApp, rescap:AppLinks, rescap:Link]
---

# rescap:Link

Registers a deep link from the settings page to the settings app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:Extension>`](element-rescap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:SettingsApp>`](element-rescap-settingsapp.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:AppLinks>`](element-rescap-applinks.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap:Link>`**  

## Syntax

```xml
<rescap:Link
  AppActivationMode = 'An optional string value.'
  DisplayName = 'An optional string value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AppActivationMode** | A deep link into the settings app in the form "uri://yourapp#deeplink" | An optional string value. | No |  |
| **DisplayName** | The display text for the deep link into the settings app. | An optional string value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [rescap:AppLinks](element-rescap-applinks.md) | Registers one or more deep links for a settings app. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
