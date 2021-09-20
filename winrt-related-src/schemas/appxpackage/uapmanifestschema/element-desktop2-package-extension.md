---

ms.assetid: f082edc4-0add-46b3-a232-17007783ecb2
title: desktop2:Extension (in Package/Extensions)
description: Declares an extensibility point for the app (in Package/Extensions; desktop2:Extension).

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:Extension (in Package/Extensions)

## Description
Declares an extensibility point for the app.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><b>&lt;desktop2:Extension&gt;</b></dd>
</dl>
</dd>
</dl>


## Syntax
``` syntax
<Extension     Category       = "windows.firewallRules" | "windows.desktopEventLogging" 
               Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
               EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
               RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
               StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.  
               uap10:TrustLevel?   = String value. Can be one of the following: "appContainer", "mediumIL".
               uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
               uap10:HostId?       = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
               uap10:Parameters?   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >

  <!-- Child elements -->
  ( desktop2:FirewallRules
  | desktop2:DesktopEventLogging )?

</uap:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following: windows.firewallRules, windows.desktopEventLogging | Yes |
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
| [FirewallRules](element-desktop2-firewallrules.md) | Specifies firewall exception rules used by Windows Desktop Bridge apps. |  
| [DesktopEventLogging](element-desktop2-desktopeventlogging.md) | Enables Windows Desktop Bridge apps to register for Windows event logging. | 


## Requirements

|               |    Value                                                         |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2`<br/><br/>`http://schemas.microsoft.com/appx/manifest/uap/windows10/10` (for the **uap10** attributes) |