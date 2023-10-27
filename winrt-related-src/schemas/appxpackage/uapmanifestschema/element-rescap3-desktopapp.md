---
ms.assetid: d8525fc0-1289-4134-9d46-d294d39d2690
title: rescap3:DesktopApp
description: Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:DesktopApp

Specifies information for redirecting a Windows Desktop Bridge app's tiles and pins.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap3:Extension\>](element-rescap3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<rescap3:DesktopAppMigration\>](element-rescap3-desktopappmigration.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap3:DesktopApp\>**

## Syntax

```xml
<rescap3:DesktopApp
  AumId = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  ShortcutPath = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **AumId** | The Application User Model ID of the Desktop app. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **ShortcutPath** | A relative shortcut path to migrate from. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [rescap3:DesktopAppMigration](element-rescap3-desktopappmigration.md) | Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
