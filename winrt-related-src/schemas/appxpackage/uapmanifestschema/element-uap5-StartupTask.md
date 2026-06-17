---
title: uap5:StartupTask
description: Specifies a startup task for your application.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:StartupTask]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:StartupTask

Specifies a startup task for your application.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:StartupTask>`**

## Syntax

```xml
<uap5:StartupTask
  TaskId = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Enabled = 'An optional boolean value.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  uap11:UserConfigurable = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **TaskId** | A unique identifier for your task. Using this identifier, your app can call the APIs in the Windows.ApplicationModel.StartupTask class to programmatically enable or disable a startup task. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Enabled** | Indicates whether the task first starts enabled or disabled. Enabled tasks will run the next time the user logs on (unless it has been disabled by the user). | An optional boolean value. | No |  |
| **DisplayName** | The name of the task that appears in the Task Manager. This string is localizable using ms-resource. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **uap11:UserConfigurable** | Indicates whether the task is user configurable. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
