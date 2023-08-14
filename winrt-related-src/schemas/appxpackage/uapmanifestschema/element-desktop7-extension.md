---
title: desktop7:Extension (in Package/Applications)
description: Declares an extensibility point for the app (in Package/Applications; desktop7:Extension).
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:Extension (in Package/Applications)

Declares an extensibility point for the app.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:Extension\>**

## Syntax

```xml
<desktop7:Extension
  Category = 'A string that can have one of the following values: "windows.approvedShellExtension", "windows.controlPanelItem", "windows.service", "windows.mailProvider", "windows.shortcut", "windows.applicationRegistration", "windows.desktopAppMigration", "windows.systemFileAssociation", "windows.shadowCopyExcludeFiles", or "windows.errorReporting".'
  Executable = 'An optional string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isnt specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'An optional string with a value between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'An optional string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  StartPage = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  uap10:TrustLevel = 'An optional string that can have one of the following values: "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' 
  uap11:Id = 'An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *. >'
  uap11:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string the can have one of the following values: "classic" or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine" or "user".'>

  <!-- Child elements -->
  desktop7:ApprovedShellExtension?
  desktop7:ControlPanelItem?
  desktop7:Service?
  desktop7:MailProvider?
  desktop7:Shortcut?
  desktop7:ApplicationRegistration?
  desktop7:DesktopAppMigration?
  desktop7:SystemFileAssociation?
  desktop7:ShadowCopyExcludeFiles?
  desktop7:ErrorReporting?

</desktop7:Extension>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The category of the extension. | A string that can have one of the following values: *windows.approvedShellExtension*, *windows.controlPanelItem*, *windows.service*, *windows.mailProvider*, *windows.shortcut*, *windows.applicationRegistration*, *windows.desktopAppMigration*, *windows.systemFileAssociation*, *windows.shadowCopyExcludeFiles*, or *windows.errorReporting*. | Yes |  |
| **Executable** | The default launch executable. | An optional string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isnt specified, the EntryPoint defined for the app is used. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string with a value between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **RuntimeType** | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | An optional string with a value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, or `*`. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string that can have one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*. | No |  |
| **uap10:HostId** | Specifies the app ID of the host app for the extension. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. | An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored.  | An optional string that can have one of the following values: *console* or *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different job object and process. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md).  | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when the application process is launched.  | An optional string that cannot contain these characters: `<`, `>`, `|`, `?`, or `*`. > | No |  |
| **uap11:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether the registrations in this extension are only visible to other applications via COM activation and other COM/OLE APIs (modern), or whether they should also be written to the registry in the classic format (classic). The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | An optional string the can have one of the following values: *classic* or *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *machine* or *user*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop7:ApprovedShellExtension](element-desktop7-approvedshellextension.md) | Specifies that a shell extension should be added to the approved shell extensions list when installed. |  
| [desktop7:ControlPanelItem](element-desktop7-controlpanelitem.md) | Registers an extension as a control panel item. |  
| [desktop7:Service](element-desktop7-service.md) | Specifies a service that is installed and registered along with the app. |  
| [desktop7:MailProvider](element-desktop7-mailprovider.md) | Specifies a service that is installed and registered along with the app. |  
| [desktop7:Shortcut](element-desktop7-shortcut.md) | Creates a shortcut to a file. |
| [desktop7:ApplicationRegistration](element-desktop7-applicationregistration.md) | Registers an application. |
| [desktop7:DesktopAppMigration](element-desktop7-desktopappmigration.md) | Specifies a set of app migration entries for tiles and pins. |
| [desktop7:SystemFileAssociation](element-desktop7-systemfileassociation.md) | Registers system file associations for an app.  |
| [desktop7:ShadowCopyExcludeFiles](element-desktop7-shadowcopyexcludefiles.md) | Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).  |
| [desktop7:ErrorReporting](element-desktop7-shadowcopyexcludefiles.md) | Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).  |


### Parent Elements

| Parent Element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the application. |  

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
