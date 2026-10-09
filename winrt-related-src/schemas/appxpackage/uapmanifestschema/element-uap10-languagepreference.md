---
description: Specifies which Windows language setting an app uses as its language preference.
title: uap10:LanguagePreference
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/09/2026
no-loc: [Package, Applications, Application, uap7:Properties, uap10:LanguagePreference]
---

# uap10:LanguagePreference

Specifies which Windows language setting an app uses as its language preference.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Properties>`](element-uap7-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:LanguagePreference>`**

## Syntax

```xml
<uap10:LanguagePreference>windowsDisplayLanguage</uap10:LanguagePreference>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap7:Properties](element-uap7-properties.md) | Properties of an application. |

## Values

| Value | Description |
|-|-|
| `windowsDisplayLanguage` | Uses the Windows display language as the app's language preference. |
| `userPreferredLanguages` | Uses the user's preferred languages as the app's language preference. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |
