---
title: uap5:AppExecutionAlias
description: Specifies the application's execution alias to determine the executable of the app to be activated (uap5:AppExecutionAlias).
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:AppExecutionAlias

Specifies the application's execution alias to determine the executable of the app to be activated.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:AppExecutionAlias\>](element-uap5-appexecutionalias.md)

## Syntax

```xml
<uap5:AppExecutionAlias
    desktop4:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
    uap10:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".' >

    <!-- Child elements -->
    uap5:ExecutionAlias{0,1000}

</uap5:AppExecutionAlias>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **desktop4:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | An optional string that can have one of the following values: "console" or "windows". | No |  |
| **uap10:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | An optional string that can have one of the following values: "console" or "windows". | No |  |

### Child elements

| Child element | Description |
|-|-|
| [ExecutionAlias](element-uap5-ExecutionAlias.md) | The executable of a UWP app to be activated from a command prompt. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **desktop4** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
