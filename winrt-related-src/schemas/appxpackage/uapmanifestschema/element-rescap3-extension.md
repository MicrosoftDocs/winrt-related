---
ms.assetid: d90b7275-21bd-46c7-89a7-c832a95186c6
title: rescap3:Extension
description: Declares an extensibility point for the app (rescap3:Extension).
ms.date: 04/10/2018
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:Extension

Declares an extensibility point for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap3:Extension\>**

## Syntax

```xml
<rescap3:Extension
  Category = 'A string that can have one of the following values: "windows.desktopAppMigration" or "windows.lockScreenComponent".'
  Executable = 'An optional string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isnt specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'An optional string with a value between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'An optional string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  StartPage = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' 
  uap11:Id = 'An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *. >'
  uap11:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string the can have one of the following values: "classic" or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine" or "user".' >

  <!-- Child elements -->
  rescap3:DesktopAppMigration
  rescap3:LockScreenComponent?

</rescap3:Extension>
```

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of app extensibility point. | A string that can have one of the following values: *windows.desktopAppMigration* or *windows.lockScreenComponent*. | Yes |  |
| **Executable** | The default launch executable. | An optional string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isnt specified, the EntryPoint defined for the app is used. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string with a value between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **RuntimeType** | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | An optional string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md). | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **uap11:Id** | An identifier for the extension. The ID must be unique for all extensions in a package.| An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. The ID must be unique for all extensions in a package.| An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored.  | An optional string that can have one of the following values: *console* or *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different processes. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md).  | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when the application process is launched. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string that cannot contain these characters: `<`, `>`, `|`, `?`, or `*`. > | No |  |
| **uap11:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether this extension's information is registered with Windows in classic ways (e.g. unpackaged apps register types with COM via the registry) or in new more scoped ways. The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | An optional string the can have one of the following values: *classic* or *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *machine* or *user*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [DesktopAppMigration](element-rescap3-desktopappmigration.md) | Specifies where to redirect user tiles and pins to a Windows Desktop Bridge app. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-extensions.md) | Defines one or more extensibility points for the package. |

## Remarks

*windows.lockScreenComponent* is an empty extension declaration that supports hosting UWP apps inside the welcome screen.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
