---
title: rescap:SearchTerms
description: Registers one or more search terms for a settings app.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# rescap:SearchTerms

Registers one or more search terms for a settings app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap:Extension\>](element-rescap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [rescap:SettingsApp](element-rescap-settingsapp.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **\<rescap:SearchTerms\>**

## Syntax

```xml
<rescap:SearchTerms>

  <!-- Child elements -->
  rescap:Term {0,5}

</rescap:SearchTerms>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [rescap:Term](element-rescap-applinks.md) | Registers a search term from the settings page to the settings app. |

### Parent elements

| Parent element | Description |
|-|-|
| [rescap:SettingsApp](element-rescap-settingsapp.md) | Registers deep link and search information for settings apps. |

### Remarks

For information about creating and registering a settings app, see [Create a partner settings app](/windows-hardware/drivers/partnerapps/create-a-system-settings-application).

## Requirements

| Item | Value |
|--|--|
| **rescap** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
