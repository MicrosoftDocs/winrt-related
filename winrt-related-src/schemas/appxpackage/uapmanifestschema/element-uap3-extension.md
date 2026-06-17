---
title: uap3:Extension
description: Declares an extensibility point for the app (uap3:Extension).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap3:Extension]
---

# uap3:Extension

Declares an extensibility point for the app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap3:Extension>`**  

## Syntax

```xml
<uap3:Extension
  Category = 'A required string that can have one of the following values: "windows.appExtensionHost", "windows.appExtension", "windows.appUriHandler", "windows.appointmentDataProvider", "windows.emailDataProvider", "windows.contactDataProvider", "windows.appExecutionAlias", "windows.appService", "windows.protocol", or "windows.fileTypeAssociation".'
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
  uap3:AppExtensionHost?
  uap3:AppExtension?
  uap3:AppUriHandler?
  uap3:AppointmentDataProvider?
  uap3:EmailDataProvider?
  uap3:ContactDataProvider?
  uap3:AppExecutionAlias?
  uap3:AppService?
  uap3:Protocol?
  uap3:FileTypeAssociation?

</uap3:Extension>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of extension. | A string that must be one of the following values: *windows.appExtensionHost*, *windows.appExtension*, *windows.appUriHandler*, *windows.appointmentDataProvider*, *windows.emailDataProvider*, *windows.contactDataProvider*, *windows.appExecutionAlias*, *windows.appService*, *windows.protocol*, *windows.fileTypeAssociation*. | Yes |  |
| **desktop11:AppLifecycleBehavior** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *systemManaged*, *unmanaged*. | No |  |
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixed frameworks in an app. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string that can have one of the following values: *appContainer*, *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, *win32App*. | No |  |
| **uap10:HostId** | Specifies the ID of the host runtime for the extension. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
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
| [uap3:AppExtensionHost](element-uap3-appextensionhost.md) | Declares an app extensibility point of type *windows.appExtensionHost*. This element indicates which categories of extensions the app can host. |
| [uap3:AppExtension](element-uap3-appextension.md) | Declares an app extensibility point of type *windows.appExtension*. This element indicates which categories of extensions the app intends to consume and/or host. |
| [uap3:AppUriHandler](element-uap3-appurihandler.md) | Declares an app extensibility point of type *windows.appUriHandler*. |
| [uap3:AppointmentDataProvider](element-uap3-appointmentdataprovider.md) | Declares an app extensibility point of type *windows.appointmentDataProvider*. |
| [uap3:EmailDataProvider](element-uap3-emaildataprovider.md) | Declares an app extensibility point of type *windows.emailDataProvider*. |
| [uap3:ContactDataProvider](element-uap3-contactdataprovider.md) | Declares an app extensibility point of type *windows.contactDataProvider*. |
| [uap3:AppExecutionAlias](element-uap3-appexecutionalias.md) | Specifies the application's execution alias to determine the executable of the app to be activated. |
| [uap3:AppService](element-uap3-appservice.md) | Declares an app extensibility point of type *windows.appService*. Application Contracts are a way for an app to invoke a background task belonging to another app, or for a background task invoked to service an app contract a way to communicate with its caller. |
| [uap3:Protocol](element-uap3-protocol.md) | Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme. |
| [uap3:FileTypeAssociation](element-uap3-filetypeassociation.md) | Defines the types of files used within the application. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-f-application-extensions.md) | <!-- TODO: Add description --> |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |
| **desktop11** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/11` |
| **desktop7** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

<!-- Author content goes here -->

## Examples

```xml
<Package
    xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
    IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension
                    Category="windows.appointmentDataProvider" 
                    EntryPoint="UserDataProvider.AppointmentDataProviderTask">  
                    <uap3:AppointmentDataProvider
                        ServerName="MyDataProvider.PPLE" />  
                </uap3:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```
