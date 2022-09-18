---
description: Declares an extensibility point for the app (uap2:Extension).
title: uap2:Extension (Windows 10)
keywords: windows 10, uwp, schema, package, manifest
ms.topic: reference
ms.date: 03/28/2022
---

# uap2:Extension (Windows 10)

Declares an extensibility point for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap2:Extension\>**

## Syntax

```xml
<uap2:Extension
  Category = 'A string that can have one of the following values: "windows.webAccountProvider".'
  Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'A string with an optional value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  StartPage = 'A string with an optional value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:TrustLevel = 'An optional string value. If specified, it must be either "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior  = 'An optional string value. If specified, it must be one of the following values:  "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with an letter.'
  uap10:Parameters = 'A string with an optional value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child Elements -->
  uap2:webAccountProvider?

</uap2:Extension>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data Type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | A string that can have one of the following values: *windows.webAccountProvider*. | Yes |  |
| **EntryPoint** | The activatable class ID. | A string with a value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **Executable** | The default launch executable. | A string with a value between 1 and 256 characters in length, that must end with `.exe`, and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixted frameworks in an app. | A string with a value between 1 and 255 characters in length that cannot start or end with a `.` or contain there characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **StartPage** | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string value. If specified, it can be one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the runtime behavior of an extension. | An optional string value. If specified, it can be one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*. | No |  |
| **uap10:HostId** | Specifies the app ID of the host app for the extension. | An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have a package identity. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap2:WebAccountProvider](element-uap2-webaccountprovider.md) | Declares an app extensibility point of type windows.webAccountProvider. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2`
| **UAP10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10`
