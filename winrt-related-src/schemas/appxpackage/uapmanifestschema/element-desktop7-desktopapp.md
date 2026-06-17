---
title: desktop7:DesktopApp
description: Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:DesktopAppMigration, desktop7:DesktopApp]
---

# desktop7:DesktopApp

Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:DesktopAppMigration>`](element-desktop7-desktopappmigration.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:DesktopApp>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:DesktopAppMigration>`](element-desktop7-desktopappmigration.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:DesktopApp>`**

## Syntax

```xml
<desktop7:DesktopApp
  AumId = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  ShortcutPath = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Executable = 'An optional string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: <, >, :, ", |, ?, or *.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AumId** | The Application User Model ID of the Desktop app to be migrated from. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **ShortcutPath** | The relative shortcut path (.lnk) to migrate from. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop7:DesktopAppMigration](element-desktop7-desktopappmigration.md) | Specifies a set of app migration entries for tiles and pins. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
