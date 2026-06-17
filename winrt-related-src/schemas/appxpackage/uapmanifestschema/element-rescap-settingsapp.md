---
title: rescap:SettingsApp
description: Registers deep link and search information for settings apps.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, rescap:Extension, rescap:SettingsApp]
---

# rescap:SettingsApp

Registers deep link and search information for settings apps.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:Extension>`](element-rescap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap:SettingsApp>`**  

## Syntax

```xml
<rescap:SettingsApp
  SettingsPageUri = 'An optional URI string that starts with `ms-settings:`.'
  Category = 'An optional string that can have one of the following values: "system", "devices", "networking", "personalization", "accounts", "privacy", or "extras".' >

  <!-- Child elements -->
  rescap:AppLinks?
  rescap:SearchTerms?

</rescap:SettingsApp>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **SettingsPageUri** | Thelaunch URI of the settings page. | An optional URI string that starts with `ms-settings:`. | No |  |
| **Category** | The category of the settings app. | An optional string that can have one of the following values: *system*, *devices*, *networking*, *personalization*, *accounts*, *privacy*, *extras*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [rescap:AppLinks](element-rescap-applinks.md) | Registers one or more deep links for a settings app. |
| [rescap:SearchTerms](element-rescap-searchterms.md) | Registers one or more search terms for a settings app. |

## Parent elements

| Parent element | Description |
|-|-|
| [rescap:Extension](element-rescap-extension.md) | Declares an extensibility point for the app. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
