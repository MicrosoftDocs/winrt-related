---
title: rescap3:DesktopApp
description: Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, rescap3:Extension, rescap3:DesktopAppMigration, rescap3:DesktopApp]
---

# rescap3:DesktopApp

Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:Extension>`](element-rescap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:DesktopAppMigration>`](element-rescap3-desktopappmigration.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap3:DesktopApp>`**  

## Syntax

```xml
<rescap3:DesktopApp
  AumId = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  ShortcutPath = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AumId** | The Application User Model ID of the Desktop app. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **ShortcutPath** | A relative shortcut path to migrate from. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [rescap3:DesktopAppMigration](element-rescap3-desktopappmigration.md) | Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
