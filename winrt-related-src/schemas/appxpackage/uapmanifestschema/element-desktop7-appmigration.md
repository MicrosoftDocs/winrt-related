---
title: desktop7:AppMigration
description: Specifies the target of a deactivated shortcut that should be updated as part of the migration of a recently uninstalled app.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:Shortcut, desktop7:AppMigrations, desktop7:AppMigration]
---

# desktop7:AppMigration

Specifies the target of a deactivated shortcut that should be updated as part of the migration of a recently uninstalled app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Shortcut>`](element-desktop7-shortcut.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:AppMigrations>`](element-desktop7-appmigrations.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:AppMigration>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Shortcut>`](element-desktop7-shortcut.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:AppMigrations>`](element-desktop7-appmigrations.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:AppMigration>`**

## Syntax

```xml
<desktop7:AppMigration
  Executable = 'An optional string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: <, >, :, ", |, ?, or *.'
  AumId = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **AumId** | The Application User Model ID of the Desktop app for which shortcuts should be migrated from. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop7:AppMigrations](element-desktop7-appmigrations.md) | Specifies a set of app migration entries for a deactivated shortcut for a recently uninstalled app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
