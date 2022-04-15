---
title: desktop:Extension
description: Declares an extensibility point for the app (desktop:Extension).
ms.date: 05/10/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop:Extension

## Description

Declares an extensibility point for the app.

## Element Hierarchy

[ < Package > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Extensions > ](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< Desktop:Extension >**

## Syntax
```syntax
<desktop:Extension Category                              = A string value that can be one of the following: "windows.fullTrustProcess", "windows.startupTask", "windows.toastNotificationActivation", or "windows.searchProtocolHandler" 
                   Executable?                           = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                   EntryPoint?                           = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                   RuntimeType?                          = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                   StartPage?                            = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                   ResourceGroup?                        =  An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
                   uap10:TrustLevel?                     = String value. Can be one of the following: "appContainer", "mediumIL".
                   uap10:RuntimeBehavior?                = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
                   uap10:HostId?                         = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
                   uap10:Parameters?                     = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                   previewappcompat:CompatMode?          = A string value that can be one of the following: "classic", "modern".
                   previewappcompat:Scope?               = A string value that can be one of the following: "user", "machine".
                   uap11:Id?                             = A string between 1 and 256 characters in length.
                   uap11:Subsystem?                      = A string value. Can be one of the following: "console", "windows".
                   uap11:SupportsMultipleInstances?      = A boolean value.
                   uap11:ResourceGroup?                  = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
                   uap11:CurrentDirectoryPath?           = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
                   uap11:Parameters?                     = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                   desktop7:CompatMode                   = A string value that can be one of the following: "classic", "modern".
                   desktop7:Scope                        = A string value that can be one of the following: "user", "machine".
                   >

  <!-- Child elements -->
  ( desktop:FullTrustProcess )?
  ( desktop:StartupTask )?
  ( desktop:ToastNotificationActivation )?
  ( desktop:SearchProtocolHandler )?

</desktop:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | The following string value is supported: **windows.fullTrustProcess** | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |
| uap10:TrustLevel | Specifies the trust level of the extension. | String value. Can be one of the following: "appContainer", "mediumIL".  | No |
| uap10:RuntimeBehavior | Specifies the run time behavior of the extension. | String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".  | No |
| uap10:HostId | Specifies the app ID of the host app for the extension. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.  | No |
| uap10:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.  | No |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [FullTrustProcess](element-desktop-fulltrustprocess.md) | Represents a desktop process that runs in full-trust. |
| [StartupTask](element-desktop-startuptasks.md) | Represents a desktop process that runs during app startup. |
| [ToastNotificationActivation](element-desktop-toastnotificationactivation.md) | Allows toast notification to be received within the app. |
| [SearchProtocolHandler](element-desktop-searchprotocolhandler.md) | Represents a desktop process handles the search protocol for the app. |   

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10`<br/><br/>`http://schemas.microsoft.com/appx/manifest/uap/windows10/10` (for the **uap10** attributes) |