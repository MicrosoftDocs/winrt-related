---
title: uap5:OutOfProcessServer
description: Declares a package extension point of type windows.activatableClass.outOfProcessServer. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process.
ms.date: 05/26/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:OutOfProcessServer]
---

# uap5:OutOfProcessServer

Declares a package extension point of type *windows.activatableClass.outOfProcessServer*. This enables 3rd party WinRT classes defined in the app package to be called from a Win32 process.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:OutOfProcessServer>`**  

## Syntax

```xml
<uap5:OutOfProcessServer
  ServerName = 'A required alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  RunFullTrust = 'An optional boolean value.' >

  <!-- Child elements -->
  uap5:Path
  uap5:Arguments?
  uap5:Instancing
  uap5:ActivatableClass{1,65535}

</uap5:OutOfProcessServer>
```

### Key

`?` optional (zero or one)
`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServerName** | A string value of the server name. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |  |
| **RunFullTrust** | If true, the server will be launched with a Windows Desktop Bridge token, as opposed to a UWP token. | Boolean. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap5:Path](element-uap5-path.md) | The path to the executable. |
| [uap5:Arguments](element-uap5-arguments.md) | Specifies the list of comma-separated arguments to pass to the executable. |
| [uap5:Instancing](element-uap5-instancing.md) | Specifies whether the executable runs as a single instance or can run as multiple instances. |
| [uap5:ActivatableClass](element-uap5-activatableclass.md) | Declares a runtime class associated with the extensibility point. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

This element is similar to the [OutOfProcessServer](element-f-outofprocessserver.md) element in Package/Extensions. Activate As Package behavior is implied by using this element in the Application/Extensions level of the manifest, indicating that the server token doesn't vary based on the activating process's token. In this context, the application identity claim matches the identity of the application it's contained in.