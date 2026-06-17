---
title: uap5:AppExecutionAlias
description: Specifies the application's execution alias to determine the executable of the app to be activated (uap5:AppExecutionAlias).
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:AppExecutionAlias]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:AppExecutionAlias

Specifies the application's execution alias to determine the executable of the app to be activated.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:AppExecutionAlias>`**

## Syntax

```xml
<uap5:AppExecutionAlias
  desktop4:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
  iot2:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
  uap10:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".' >

  <!-- Child elements -->
  uap5:ExecutionAlias{0,1000}
  uap5:ExecutionAlias{0,1000}

</uap5:AppExecutionAlias>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **desktop4:Subsystem** | Indicates whether the app uses the Windows subsystem or the console subsystem. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **iot2:Subsystem** | Indicates whether the app uses the Windows subsystem or the console subsystem. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **uap10:Subsystem** | Indicates whether the app uses the Windows subsystem or the console subsystem. | An optional string that can have one of the following values: *console*, *windows*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap5:ExecutionAlias](element-uap5-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |
| [uap8:ExecutionAlias](element-uap8-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **desktop4** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **iot2** | `http://schemas.microsoft.com/appx/manifest/iot/windows10/2` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
