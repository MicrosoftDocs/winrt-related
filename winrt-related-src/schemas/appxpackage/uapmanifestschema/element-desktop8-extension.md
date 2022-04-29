---
title: desktop8:Extension (in Package/Extensions)
description: Declares an extensibility point for the app (in Package/Extensions; desktop8:Extension).
keywords: windows 10, uwp, schema, manifest, desktop, extension
ms.date: 04/27/2022
ms.topic: reference
---

# desktop8:Extension (in Package/Extensions)

## Description

Declares an extensibility point for the app.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd><strong>&lt;desktop8:Extension&gt;</strong></dd>
</dl>
</dd>
</dl>

## Syntax

```xml
<desktop8:Extension
            Category       = A string value that can be one of the following: "windows.mutablePackageDirectories", "windows.userMutablePackageDirectories", or "windows.eventTracing"
            Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", \|, ?, or *. It specifies the default executable for the extension. If specified, the EntryPoint property is also used.
            EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
            RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
            StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
            ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
            uap10:TrustLevel?   = String value. Can be one of the following: "appContainer", "mediumIL".
            uap10:RuntimeBehavior?  = String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".
            uap10:HostId?       = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.
            uap10:Parameters?   = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
            >

  <!-- Child Elements -->
  desktop8:MutablePackageDirectories
  desktop8:UserMutablePackageDirectories
  desktop8:EventTracing

</desktop8:Extension>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | The following are supported: "windows.mutablePackageDirectories", "windows.userMutablePackageDirectories", "windows.eventTracing" | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: &lt:, &gt;, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | No |
| ResourceGroup | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md).| An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |
| uap10:TrustLevel | Specifies the trust level of the extension. | String value. Can be one of the following: "appContainer", "mediumIL".  | No |
| uap10:RuntimeBehavior | Specifies the run time behavior of the extension. | String value. Can be one of the following: "windowsApp", "packagedClassicApp", "win32App".  | No |
| uap10:HostId | Specifies the app ID of the host app for the extension. | An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.  | No |
| uap10:Parameters | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.  | No |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop8:MutablePackageDirectories](element-desktop8-mutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where you can modify the installation files for your application. |
| [desktop8:UserMutablePackageDirectories](element-desktop8-usermutablepackagedirectories.md) | Enables your desktop application to specify one or more folders where users can modify the installation files for your application (for example, to install mods). |
| [desktop8:EventTracing](element-desktop8-eventtracing.md) | Enables your desktop application to log application-defined events to be consumed in real time or saved to a log file. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [Extensions (in Package/Application)](element-1-extensions.md) | Defines one or more extensibility points for the application. |

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **desktop8** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/8` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |