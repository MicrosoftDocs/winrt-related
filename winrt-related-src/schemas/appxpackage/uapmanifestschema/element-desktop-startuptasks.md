---
title: desktop:StartupTasks
description: Represents a desktop process that runs during app startup.
ms.date: 05/10/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop:StartupTasks

Represents a desktop process that runs during app startup.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Desktop:Extension\>](element-desktop-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**<\Desktop:StartupTasks\>**

## Syntax

```xml
<desktop:StartupTasks
  TaskId = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Enabled = 'A boolean value.'
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
  rescap5:ImmediateRegistration =  'A boolean value.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **TaskId** | A unique identifier for the task. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Enabled** | Indicates whether or not the task is enabled. | A boolean value. | No |  |
| **DisplayName** | A user-friendly name to display to users. | A string between 1 and 256 characters in length. This string is localizable. | No |  |
| **rescap5:ImmediateRegistration** | Indicates whether the task should be registered immediately. | A boolean value | No |  |

## Child elements

None

## Parent elements

| Parent element | Description |
|-|-|
| [desktop:Extension](element-desktop-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value  |
|--|--|
| **Desktop** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |
| **Rescap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/5`
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
