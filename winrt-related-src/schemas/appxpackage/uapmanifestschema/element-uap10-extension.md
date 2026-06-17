---
title: uap10:Extension
description: Declares an extensibility point for the app (uap10:Extension).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, uap10:Extension]
---

# uap10:Extension

Declares an extensibility point for the app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:Extension>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap10:Extension>`**  

## Syntax

```xml
<uap10:Extension
  Category = 'A required string that can have one of the following values: "windows.protocol", "windows.hostRuntime", "windows.installedLocationVirtualization", or "windows.mediaContentDecryptionModule".'
  desktop11:AppLifecycleBehavior = 'An optional string that can have one of the following values: "systemManaged", or "unmanaged".'
  Executable = 'An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  EntryPoint = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  RuntimeType = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  StartPage = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  TrustLevel = 'An optional string that can have one of the following values: "appContainer", or "mediumIL".'
  RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  HostId = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Id = 'An optional string between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *.'
  uap11:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string that can have one of the following values: "classic", or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine", or "user".' >

  <!-- Child elements -->
  uap10:HostRuntime?
  uap10:InstalledLocationVirtualization?
  uap10:MediaContentDecryptionModule?
  uap10:Protocol?

</uap10:Extension>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of extension. | A string that must be one of the following values: *windows.protocol* (in Application); *windows.hostRuntime*, *windows.installedLocationVirtualization*, *windows.mediaContentDecryptionModule* (in Package). | Yes |  |
| **desktop11:AppLifecycleBehavior** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *systemManaged*, *unmanaged*. | No |  |
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixed frameworks in an app. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **TrustLevel** | Specifies the trust level of the extension. | An optional string that can have one of the following values: *appContainer*, *mediumIL*. | No |  |
| **RuntimeBehavior** | Specifies the runtime behavior of an extension. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, *win32App*. | No |  |
| **HostId** | Specifies the ID of the host runtime for the extension. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. The ID must be unique for all extensions in a package. | An optional string between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is useful for non-UWP processes that need to be started with a specific subsystem. In most cases this should be left as the default. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether the extension supports multiple instances. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when launching the process. | An optional string that cannot contain these characters: <, >, &#124;, ?, or *. | No |  |
| **uap11:Parameters** | Contains command line parameters to pass to the extension. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies the compatibility mode for the extension. | An optional string that can have one of the following values: *classic*, *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the extension is per-user or per-machine. | An optional string that can have one of the following values: *machine*, *user*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap10:HostRuntime](element-uap10-hostruntime.md) | Defines a package-wide extension that defines the runtime information to be used when activating a [hosted app](/windows/uwp/launch-resume/hosted-apps). |
| [uap10:InstalledLocationVirtualization](element-uap10-installedlocationvirtualization.md) | Defines an extension for a desktop app in an MSIX package that redirects any writes to the app's installation directory to a location in the [app data](/windows/uwp/design/app-settings/store-and-retrieve-app-data). For more details, see the [remarks](#remarks). |
| [uap10:MediaContentDecryptionModule](element-uap10-mediacontentdecryptionmodule.md) | Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files. |
| [uap10:Protocol](element-uap10-protocol.md) | Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extensions (in Package)](element-f-package-extensions.md) | <!-- TODO: Add description --> |
| [Extensions (in Application)](element-f-application-extensions.md) | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **desktop11** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/11` |
| **desktop7** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
