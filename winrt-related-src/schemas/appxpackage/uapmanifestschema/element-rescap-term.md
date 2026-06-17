---
title: rescap:Term
description: Registers a search term for a settings app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, rescap:Extension, rescap:SettingsApp, rescap:SearchTerms, rescap:Term]
---

# rescap:Term

Registers a search term for a settings app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:Extension>`](element-rescap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:SettingsApp>`](element-rescap-settingsapp.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:SearchTerms>`](element-rescap-searchterms.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap:Term>`**  

## Syntax

```xml
<rescap:Term>
    <!-- TODO: Add value description -->
</rescap:Term>
```

## Value

<!-- TODO: Add value description -->

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Registers one or more search terms for a settings app. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [rescap:SearchTerms](element-rescap-searchterms.md) | Registers one or more search terms for a settings app. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
