---
title: uap8:Extension
description: Declares an extensibility point for the app (uap8:Extension).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, uap8:Extension]
---

# uap8:Extension

Declares an extensibility point for the app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap8:Extension>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap8:Extension>`**  

## Syntax

```xml
<uap8:Extension
  Category = 'A required string that can have one of the following values: "windows.posPaymentConnector", or "windows.dataProtection".'
  desktop11:AppLifecycleBehavior = 'An optional string that can have one of the following values: "systemManaged", or "unmanaged".'
  Executable = 'An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  EntryPoint = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  RuntimeType = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  StartPage = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap10:TrustLevel = 'An optional string that can have one of the following values: "appContainer", or "mediumIL".'
  uap10:RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap10:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Id = 'An optional string between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *.'
  uap11:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string that can have one of the following values: "classic", or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine", or "user".' >

  <!-- Child elements -->
  uap8:PosPaymentConnector?
  uap8:DataProtection?

</uap8:Extension>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | A string that must be one of the following values: *windows.posPaymentConnector* (in Application); *windows.dataProtection* (in Package). | Yes |  |
| **desktop11:AppLifecycleBehavior** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *systemManaged*, *unmanaged*. | No |  |
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixed frameworks in an app. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **ResourceGroup** | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-f-application.md)*. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string that can have one of the following values: *appContainer*, *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the runtime behavior of an extension. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, *win32App*. | No |  |
| **uap10:HostId** | Specifies the ID of the host runtime for the extension. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. The ID must be unique for all extensions in a package. | An optional string between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | The subsystem targeted by the extension. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different processes. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-f-application.md). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when the application process is launched. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string that cannot contain these characters: <, >, &#124;, ?, or *. | No |  |
| **uap11:Parameters** | The subsystem targeted by the extension. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether this extension's information is registered with Windows in classic ways (e.g. unpackaged apps register types with COM via the registry) or in new more scoped ways. The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *classic*, *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *machine*, *user*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap8:PosPaymentConnector](element-uap8-pospaymentconnector.md) | Contains device information for Point-of-Sale/Point-of-Service devices. |
| [uap8:DataProtection](element-uap8-dataprotection.md) | Settings to configure data encryption. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extensions (in Package)](element-f-package-extensions.md) | <!-- TODO: Add description --> |
| [Extensions (in Application)](element-f-application-extensions.md) | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **desktop11** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/11` |
| **desktop7** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
