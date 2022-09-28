---
ms.assetid: c589d7a3-8588-4dbd-bc8b-9fd54c639e01
title: uap4:Extension
description: Declares an extensibility point for the app (uap4:Extension).
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# uap4:Extension

Declares an extensibility point for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:Extension\>**

## Syntax

```xml
<uap4:Extension
  Category = 'A string that can have one of the following values: "windows.sharedFonts", "windows.userDataTaskDataProvider", "windows.mediaCodec", "windows.contactPanel", "windows.loopbackAccessRules", "windows.devicePortalProvider", "windows.printWorkflowBackgroundTask", or "windows.printWorkflowForegroundTask".'
  Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'A string with an optional value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  StartPage = 'A string with an optional value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:TrustLevel = 'An optional string value. If specified, it must be either "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior  = 'An optional string value. If specified, it must be one of the following values:  "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with an letter.'
  uap10:Parameters = 'A string with an optional value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  uap4:SharedFonts
  uap4:UserDataTaskDataProvider
  uap4:MediaCodec 
  uap4:ContactPanel
  uap4:LoopbackAccessRules
  uap4:DevicePortalProvider?

</uap4:Extension>
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data Type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | A string that can have one of the following values: *windows.sharedFonts*, *windows.userDataTaskDataProvider*, *windows.mediaCodec*, *windows.contactPanel*, *windows.loopbackAccessRules*, *windows.devicePortalProvider*, *windows.printWorkflowBackgroundTask*, or *windows.printWorkflowForegroundTask*. | Yes |  |
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
| [SharedFonts](element-uap4-sharedFonts.md) | Contains the locations of shared fonts to be used with the app. |  
| [UserDataTaskDataProvider](element-uap4-userDataTaskDataProvider.md) | Enables an app to become a DataProvider for a task. |
| [MediaCodec](element-uap4-mediacodec.md) | Defines an extension that enables an app to install media codecs from the Microsoft Store. |
| [ContactPanel](element-uap4-contactpanel.md) | Enables the contacts panel in a Windows app. |
| [LoopbackAccessRules](element-uap4-loopbackAccessRules.md) | Contains rules for a loopback filter that enables communication between an app and a service. |
| [DevicePortalProvider](element-uap4-devicePortalProvider.md) | Defines a Device Portal provider for deployment. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the package. |

## Remarks

*windows.printWorkflowBackgroundTask* and *windows.printWorkflowForegroundTask* are empty extension declarations that provide support for print scenarios. The background task entry point will initially be called by the print system to start handling print data, and the foreground task will be activated when requesting more information from the user. The background entry point must be a class implementing [IBackgroundTask](/uwp/api/Windows.ApplicationModel.Background.IBackgroundTask).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
