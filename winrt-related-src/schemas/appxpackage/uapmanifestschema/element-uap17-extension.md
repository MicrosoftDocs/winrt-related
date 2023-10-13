---
title: uap17:Extension
description: Declares an extensibility point for the app. (uap17:Extension).
ms.date: 10/12/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# uap17:Extension

## Description

Declares an extensibility point for the app.

## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;uap17:Extension&gt;</b></dd></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap17:Extension     Category = "windows.packageExtensionHost" | "windows.packageExtension"
    desktop11:AppLifecycleBehavior = "systemManaged" | "unmanaged"
    Executable? = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.
    EntryPoint? = A string between 1 and 256 characters in length that cannot start or end with a whitespace character.
    RuntimeType? = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
    StartPage? = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
    uap10:TrustLevel? = "appContainer" | "mediumIL"
    uap10:RuntimeBehavior? = "windowsApp" | "packagedClassicApp" | "win32App"
    uap10:HostId? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
    uap10:Parameters? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    uap11:Id? = A string between 1 and 255 characters in length with a non-whitespace character at its beginning and end.
    uap11:Subsystem? = "console" | "windows"
    uap11:SupportsMultipleInstances? = Boolean.
    uap11:ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
    uap11:CurrentDirectoryPath? = A string that cannot contain these characters: <, >, |, ?, or *. >
    uap11:Parameters? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    desktop7:CompatMode? = "classic" | "modern"
    desktop7:Scope? = "machine" | "user"
>
<!-- Child elements -->
  PackageExtensionHost
  PackageExtension
</uap17:Extension>
```

## Key
`?`    optional (zero or one) 


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Category | The type of package extensibility point. | One of the following values: "windows.packageExtensionHost" , "windows.packageExtension"| Yes |
| desktop11:AppLifecycleBehavior | Allows an app to override the lifecycle behavior associated with the runtime behavior for the extension. Apps or extensions with a **RuntimeBehavior** of "windowsApp" implicitly have **AppLifecycleBehavior** of "systemManaged". Apps or extensions with **RuntimeBehavior** of "packagedClassicApp" or "win32App" implicitly have **AppLifecycleBehavior** of "unmanaged" | One of the following values: "systemManaged" , "unmanaged".| No |
| Executable | The default launch executable. | One of the following values: A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", ,, ?, or *.| No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length that cannot start or end with a whitespace character.| No |
| RuntimeType | The runtime provider. | One of the following values: A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, ,, ?, or *.| No |
| StartPage | The web page that handles the extensibility point. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| No |
| ResourceGroup | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.| No |
| uap10:TrustLevel | Specifies the trust level of the extension. | One of the following values: "appContainer" , "mediumIL"| No |
| uap10:RuntimeBehavior | Specifies the runtime behavior of an extension. | One of the following values: "windowsApp" , "packagedClassicApp" , "win32App"| No |
| uap10:HostId | Specifies the app ID of the host app for the extension. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.| No |
| uap10:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have a package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| No |
| uap11:Id | An identifier for the extension. | A string between 1 and 255 characters in length with a non-whitespace character at its beginning and end.| No |
| uap11:Subsystem | This attribute is inherited from the base extension syntax. Other than syntactic validation, this value is ignored. | One of the following values: "console" , "windows"| No |
| uap11:SupportsMultipleInstances | Specifies whether instances should run in different job object and process. The default value is false. | Boolean.| No |
| uap11:ResourceGroup | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.| No |
| uap11:CurrentDirectoryPath | Specifies the initial directory when the application process is launched. | One of the following values: A string that cannot contain these characters: <, >, ,, ?, or *. >| No |
| uap11:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have a package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| No |
| desktop7:CompatMode | Specifies whether the registrations in this extension are only visible to other applications via COM activation and other COM/OLE APIs (modern), or whether they should also be written to the registry in the classic format (classic). The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | One of the following values: "classic" , "modern"| No |
| desktop7:Scope | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | One of the following values: "machine" , "user"| No |


## Child Elements

| Element | Description |
| -----------| -------------|
| [PackageExtensionHost](element-uap17-packageextensionhost.md) | Declares an app extensibility point of type windows.appExtensionHost. |
| [PackageExtension](element-uap17-packageextension.md) | Declares an app extensibility point of type windows.appExtension. |

## Remarks



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| uap17 | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| uap10 | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| uap11 | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| desktop7 | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
