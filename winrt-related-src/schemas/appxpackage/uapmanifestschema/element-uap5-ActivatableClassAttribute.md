---
title: uap5:ActivatableClassAttribute
description: Defines an attribute of the class that is stored in the Windows Runtime property store (in Package/Applications).
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:OutOfProcessServer, uap5:ActivatableClass, uap5:ActivatableClassAttribute]
keywords: windows 10, uwp, schema, package manifest
---

# uap5:ActivatableClassAttribute

Defines an attribute of the class that is stored in the Windows Runtime property store.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:OutOfProcessServer>`](element-uap5-outofprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:ActivatableClass>`](element-uap5-activatableclass.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:ActivatableClassAttribute>`**

## Syntax

```xml
<uap5:ActivatableClassAttribute
  Name = 'A required alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  Type = 'A required string that can have one of the following values: "string", or "integer".'
  Value = 'A required string between 1 and 32767 characters in length.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the attribute. | A alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |  |
| **Type** | The type of the attribute. | A string that can have one of the following values: *string*, *integer*. | Yes |  |
| **Value** | The value of the attribute. | A string between 1 and 32767 characters in length. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:ActivatableClass](element-uap5-activatableclass.md) | Declares a runtime class associated with the extensibility point. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
