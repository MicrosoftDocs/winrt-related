---
title: uap4:ContactPanel
description: Enables the contacts panel in a Windows app.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap4:Extension, uap4:ContactPanel]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap4:ContactPanel

Enables the contacts panel in a Windows app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:Extension>`](element-uap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:ContactPanel>`**

## Syntax

```xml
<uap4:ContactPanel
  SupportsUnknownContacts = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **SupportsUnknownContacts** | True if the contact panel supports unknown contacts, otherwise false. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
