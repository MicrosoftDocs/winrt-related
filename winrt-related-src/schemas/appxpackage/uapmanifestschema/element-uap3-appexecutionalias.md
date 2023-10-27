---
title: uap3:AppExecutionAlias
description: Specifies the application's execution alias to determine the executable of the app to be activated (uap3:AppExecutionAlias).
ms.date: 04/04/2004
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:AppExecutionAlias

Specifies the application's execution alias to determine the executable of the app to be activated.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extension\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap3:AppExecutionAlias\>**

## Syntax

```xml
<uap3:AppExecutionAlias
    desktop4:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".' >

    uap3:ExecutionAlias{0,1000}

</uap3:AppExecutionAlias>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop:ExecutionAlias](element-desktop-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |
| [uap8:ExecutionAlias](element-uap8-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| Minimum OS Version | Windows 10 version 1607 (Build 14393) |
