---
title: uap5:ActivatableClass
description: Declares a runtime class associated with the extensibility point (uap5:ActivatableClass).
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:ActivatableClass

Declares a runtime class associated with the extensibility point.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:OutOfProcessServer\>](element-uap5-outofprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:ActivatableClass\>**

## Syntax

```xml
<uap5:ActivatableClass
  ActivatableClassId = 'A string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.' >

  <!-- Child elements -->
  ActivatableClassAttribute{0,1000}

</uap5:ActivatableClass>
```

## Attrbutes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| ActivatableClassId | The identifier of the runtime class in the operating system. | A string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [ActivatableClassAttribute](element-uap5-ActivatableClassAttribute.md) | Defines an attribute of the class that is stored in the Windows Runtime property store. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:OutOfProcessServer](element-uap5-outofprocessserver.md) | Declares a package extension point of type *windows.activatableClass.outOfProcessServer*. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| Minimum OS Version | Windows 10 version 1709 (Build 16299) |
