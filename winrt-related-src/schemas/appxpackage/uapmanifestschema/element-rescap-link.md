---
title: rescap:Link
description: Registers a deep link from the settings page to the settings app.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# rescap:Link

Registers a deep link from the settings page to the settings app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap:Extension\>](element-rescap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [rescap:SettingsApp](element-rescap-settingsapp.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [rescap:AppLinks](element-rescap-applinks.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **\<rescap:Link\>**

## Syntax

```xml
<rescap:Link 
    AppActivationMode = 'A string.'
    DisplayName = 'A string
/>
```


## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AppActivationMode** | A deep link into the settings app in the form "uri://yourapp#deeplink" | A string. | Yes |  |
| **DisplayName** | The display text for the deep link into the settings app. | A string. | Yes |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [rescap:AppLinks](element-rescap-applinks.md) | Registers one or more deep links for a settings app. |

### Remarks

For information about creating and registering a settings app, see [Create a partner settings app](/windows-hardware/drivers/partnerapps/create-a-system-settings-application).

## Requirements

| Item | Value |
|--|--|
| **rescap** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
