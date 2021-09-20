---

ms.assetid: c589d7a3-8588-4dbd-bc8b-9fd54c639e01
title: uap4:Extension
description: Declares an extensibility point for the app (uap4:Extension).

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, extension 
---

# uap4:Extension

## Description
Declares an extensibility point for the app.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;uap4:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<uap4:Extension Category       = "windows.sharedFonts" | "windows.userDataTaskDataProvider" | "windows.mediaCodec" | "windows.contactPanel" | "windows.loopbackAccessRules" | "windows.devicePortalProvider" | "windows.printWorkflowBackgroundTask"
                   Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                   EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                   RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                   StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. 
                   ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. 
                   uap10:TrustLevel?       = String value. Can be one of the following: "appContainer", "mediumIL".
                   uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
                   uap10:HostId?           = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
                   uap10:Parameters?       = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( uap4:SharedFonts
  | uap4:UserDataTaskDataProvider
  | uap4:MediaCodec 
  | uap4:ContactPanel
  | uap4:LoopbackAccessRules
  | uap4:DevicePortalProvider )?

</uap4:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following:<ul><li>windows.sharedFonts</li><li>windows.userDataTaskDataProvider</li><li>windows.mediaCodec</li><li>windows.contactPanel</li><li>windows.loopbackAccessRules</li><li>windows.devicePortalProvider</li><li>windows.printWorkflowBackgroundTask</li></ul> | Yes |
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
| [SharedFonts](element-uap4-sharedFonts.md) | Contains the locations of shared fonts to be used with the app. |  
| [UserDataTaskDataProvider](element-uap4-userDataTaskDataProvider.md) | Enables an app to become a DataProvider for a task. | 
| [MediaCodec](element-uap4-mediacodec.md) | Defines an extension that enables an app to install media codecs from the Microsoft Store. |
| [ContactPanel](element-uap4-contactpanel.md) | Enables the contacts panel in a Windows app. |
| [LoopbackAccessRules](element-uap4-loopbackAccessRules.md) | Contains rules for a loopback filter that enables communication between an app and a service. |
| [DevicePortalProvider](element-uap4-devicePortalProvider.md) | Defines a Device Portal provider for deployment. |

## Remarks
**windows.printWorkflowBackgroundTask** is an empty extension declaration that provides support for print scenarios. The background task entry point will initially be called by the print system to start handling print data, and the foreground task will be activated when requesting more information from the user.

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4`<br/><br/>`http://schemas.microsoft.com/appx/manifest/uap/windows10/10` (for the **uap10** attributes) |
