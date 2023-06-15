---
title: rescap4:Extension
description: Declares an extensibility point for the app (rescap4:Extension).
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# rescap4:Extension

Declares an extensibility point for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap4:Extension\>**

## Syntax

```xml
<rescap4:Extension
  Category = 'A string that can have one of the following values: "windows.classicAppCompatKeys" or "windows.primaryInteropAssemblies".'
  Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'A string with an optional value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  StartPage = 'A string with an optional value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:TrustLevel = 'An optional string value. If specified, it must be either "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior  = 'An optional string value. If specified, it must be one of the following values:  "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with an letter.'
  uap10:Parameters = 'A string with an optional value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Id = 'An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *. >'
  uap11:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string the can have one of the following values: "classic" or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine" or "user".' >

  <!-- Child elements -->
  rescap4:PrimaryInteropAssemblies?
  rescap4:ClassicAppCompatKeys? 

</rescap4:Extension>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data Type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | Can be one of the following values: *windows.backgroundTasks*, *windows.preInstalledConfigTask*, *windows.updateTask*, or *windows.restrictedLaunch*. | Yes |  |
| **EntryPoint** | The activatable class ID. | A string with a value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **Executable** | The default launch executable. | A string with a value between 1 and 256 characters in length, that must end with `.exe`, and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixted frameworks in an app. | A string with a value between 1 and 255 characters in length that cannot start or end with a `.` or contain there characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **StartPage** | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string value. If specified, it can be one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the runtime behavior of an extension. | An optional string value. If specified, it can be one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*. | No |  |
| **uap10:HostId** | Specifies the app ID of the host app for the extension. | An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have a package identity. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. | An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored.  | An optional string that can have one of the following values: *console* or *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different job object and process. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md).  | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when the application process is launched.  | An optional string that cannot contain these characters: `<`, `>`, `|`, `?`, or `*`. > | No |  |
| **uap11:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether the registrations in this extension are only visible to other applications via COM activation and other COM/OLE APIs (modern), or whether they should also be written to the registry in the classic format (classic). The default value is "modern". For more information, see the Remarks section. | An optional string the can have one of the following values: *classic* or *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". For more information, see the Remarks section. | An optional string that can have one of the following values: *machine* or *user*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [PrimaryInteropAssemblies](element-rescap4-primaryinteropassemblies.md) | Defines package assembly configuration. |
| [ClassicAppCompatKeys](element-rescap4-ClassicAppCompatKeys.md) | Contains registry keys for discovering classic app installations and launching executables. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item | Value |
|--|--|
| **rescap4** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
