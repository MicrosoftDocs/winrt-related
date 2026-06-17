---
title: uap5:ActivatableClass
description: Declares a runtime class associated with the extensibility point (uap5:ActivatableClass).
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:OutOfProcessServer, uap5:ActivatableClass]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:ActivatableClass

Declares a runtime class associated with the extensibility point.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:OutOfProcessServer>`](element-uap5-outofprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:ActivatableClass>`**

## Syntax

```xml
<uap5:ActivatableClass
  ActivatableClassId = 'A required string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.' >

  <!-- Child elements -->
  uap5:ActivatableClassAttribute{0,1000}

</uap5:ActivatableClass>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActivatableClassId** | The identifier of the runtime class in the operating system. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | Yes |  |

## Child elements

| Child element | Description |
|-|-|
| [uap5:ActivatableClassAttribute](element-uap5-activatableclassattribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:OutOfProcessServer](element-uap5-outofprocessserver.md) | Declares a package extension point of type *windows.activatableClass.outOfProcessServer*. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
