---
title: rescap:SettingsApp
description: Registers deep link and search information for settings apps.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# rescap:SettingsApp

Registers deep link and search information for settings apps.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap:Extension\>](element-rescap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **\<rescap:SettingsApp\>**

## Syntax

```xml
<rescap:SettingsApp
       Category = 'A string that can have one of the following values: "system", "devices", "networking", "personalization", "accounts", "privacy", or "extras.'
       SettingsPageUri = 'A URI string that starts with "ms-settings:".'>

  <!-- Child elements -->
  rescap:AppLinks?
  rescap:SearchTerms?   

</rescap:SettingsApp>
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The category of the settings app. | A string that can have one of the following values: "system", "devices", "networking", "personalization", "accounts", "privacy", or "extras. | No |  |
| **SettingsPageUri** | Thelaunch URI of the settings page. | A URI string that starts with "ms-settings:" | No |  |


### Child elements

| Child element | Description |
|-|-|
| [rescap:AppLinks](element-rescap-applinks.md) | Registers one or more deep links for a settings app. |
| [rescap:SearchTerms](element-rescap-searchterms.md) | Specifies search terms associated with the settings app. |

### Parent elements

| Parent element | Description |
|-|-|
| [rescap:Extension](element-rescap-extension.md) | Declares an extensibility point for the app. |

### Remarks

For information about creating and registering a settings app, see [Create a partner settings app](/windows-hardware/drivers/partnerapps/create-a-system-settings-application).

## Requirements

| Item | Value |
|--|--|
| **rescap** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
