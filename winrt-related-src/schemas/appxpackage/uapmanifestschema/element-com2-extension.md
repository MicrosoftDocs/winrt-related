---
title: com2:Extension (Windows 10)
description: Provides functionality to expose COM registrations to clients outside of the app package (com2:Extension).
ms.date: 04/20/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com2:Extension (Windows 10)

Provides functionality to expose COM registrations to clients outside of the app package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com2:Extension\>**

## Syntax

```xml
<com2:Extension
  Category = 'A string that can have one of the following values: "windows.comServer" or "windows.comInterface".' 
  uap10:TrustLevel = 'An optional string value that can be one of the following values: "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior = 'An optional string value that can be one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:Parameters = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' 
  uap11:Id = 'An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *. >'
  uap11:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string the can have one of the following values: "classic" or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine" or "user".' >

  <!-- Child elements -->
  com2:ComServer
  com2:ComInterface

</com2:Extension>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of app extensibility point. | A string that can have one of the following values: *windows.comServer* or *windows.comInterface*.| Yes |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string value that can be one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. | An optional string value that can be one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*.  | No |  |
| **uap10:HostId** | Specifies the ID of the host runtime for the extension. | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. The ID must be unique for all extensions in a package.| An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored.  | An optional string that can have one of the following values: *console* or *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different processes. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md).  | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when the application process is launched.  | An optional string that cannot contain these characters: `<`, `>`, `|`, `?`, or `*`. > | No |  |
| **uap11:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether this extension's information is registered with Windows in classic ways (e.g. unpackaged apps register types with COM via the registry) or in new more scoped ways. The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | An optional string the can have one of the following values: *classic* or *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *machine* or *user*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [com2:ComServer](element-com2-comserver.md) | Declares a package extension point of type **windows.comServer**. |
| [com2:ComInterface](element-com2-cominterface.md) | Declares a package extension point of type **windows.comInterface**. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/2` |
| **uap10 elements** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
