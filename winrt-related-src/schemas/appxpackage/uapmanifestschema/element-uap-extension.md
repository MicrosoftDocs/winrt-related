---
description: Declares an extensibility point for the app (uap:Extension).
Search.Product: eADQiWindows 10XVcnh
title: uap:Extension (Windows 10)
ms.assetid: b0c2ee51-897b-40be-aa38-372e2f94897f
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 01/16/2020
---

# uap:Extension (Windows 10)

Declares an extensibility point for the app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:Extension\>**

## Syntax

```xml
<uap:Extension
  Category = 'A string that can have one of the following values: "windows.fileTypeAssociation", "windows.protocol", "windows.autoPlayContent", "windows.autoPlayDevice", "windows.shareTarget", "windows.search", "windows.fileOpenPicker", "windows.fileSavePicker", "windows.cachedFileUpdater", "windows.cameraSettings", "windows.accountPictureProvider", "windows.printTaskSettings", "windows.lockScreenCall", "windows.appointmentsProvider", "windows.alarm", "windows.webAccountProvider", "windows.dialProtocol", "windows.appService", "windows.mediaPlayback", "windows.print3DWorkflow", "windows.lockScreen", "windows.aboveLockScreen", "windows.personalAssistantLaunch", or "windows.voipCall".'
  Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'A string with an optional value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  StartPage = 'A string with an optional value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:TrustLevel = 'An optional string value. If specified, it must be either "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior  = 'An optional string value. If specified, it must be one of the following values:  "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with an letter.'
  uap10:Parameters = 'A string with an optional value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Id = 'An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *. >'
  uap11:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string the can have one of the following values: "classic" or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine" or "user".' >

  <!-- Child elements -->
  uap:FileTypeAssociation?
  uap:Protocol?
  uap:AutoPlayContent?
  uap:AutoPlayDevice?
  uap:ShareTarget?
  uap:FileOpenPicker?
  uap:FileSavePicker?
  uap:AppointmentsProvider?
  uap:WebAccountProvider?
  uap:DialProtocol?
  uap:AppService?
  uap:MediaPlayback?
  uap:VoipCall?

</uap:Extension>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data Type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | A string that can have one of the following values: *windows.fileTypeAssociation*, *windows.protocol*, *windows.autoPlayContent*, *windows.autoPlayDevice*, *windows.shareTarget*, *windows.search*, *windows.fileOpenPicker*, *windows.fileSavePicker*, *windows.cachedFileUpdater*, *windows.cameraSettings*, *windows.accountPictureProvider*, *windows.printTaskSettings*, *windows.lockScreenCall*, *windows.appointmentsProvider*, *windows.alarm*, *windows.webAccountProvider*, *windows.dialProtocol*, *windows.appService*, *windows.mediaPlayback*, *windows.print3DWorkflow*, *windows.lockScreen*, *windows.aboveLockScreen*, *windows.personalAssistantLaunch*, or *windows.voipCall*. | Yes |  |
| **EntryPoint** | The activatable class ID. | A string with a value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **Executable** | The default launch executable. | A string with a value between 1 and 256 characters in length, that must end with `.exe`, and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixted frameworks in an app. | A string with a value between 1 and 255 characters in length that cannot start or end with a `.` or contain there characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **StartPage** | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string value. If specified, it can be one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the runtime behavior of an extension. | An optional string value. If specified, it can be one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*. | No |  |
| **uap10:HostId** | Specifies the ID of the host runtime for the extension. | An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps.| A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
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
| [uap:AppService](element-uap-appservice.md) | Declares an app extensibility point of type *windows.appService*. Application Contracts are a way for an app to invoke a background task belonging to another app; or for a background task invoked to service an app contract a way to communicate with its caller. |
| [uap:AppointmentsProvider](element-uap-appointmentsprovider.md) | Declares an app extensibility point of type *windows.appointmentsProvider*. |
| [uap:AutoPlayContent](element-uap-autoplaycontent.md) | Declares an app extensibility point of type *windows.autoPlayContent*. The app provides the specified AutoPlay content actions. |
| [uap:AutoPlayDevice](element-uap-autoplaydevice.md) | Declares an app extensibility point of type **windows.autoPlayDevice*. The app provides the specified AutoPlay device actions. |
| [uap:DialProtocol](element-uap-dialprotocol.md) | Declares an app extensibility point of type *windows.dialProtocol**. |
| [uap:FileOpenPicker](element-uap-fileopenpicker.md) | Declares an app extensibility point of type *windows.fileOpenPicker*. The app lets the user choose and open the specified types of files. |
| [uap:FileSavePicker](element-uap-filesavepicker.md) | Declares an app extensibility point of type *windows.fileSavePicker*. The app lets the user choose the file name, extension, and storage location for the specified types of files. |
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type *windows.fileTypeAssociation*. A file type association indicates that the app is registered to handle files of the specified types. |
| [uap:MediaPlayback](element-uap-mediaplayback.md) | Declares an app extensibility point of type mediaPlayback so that your app can declare that it performs video transcoding. |
| [uap:Protocol](element-uap-protocol.md) | Declares an app extensibility point of type *windows.protocol*. A URI association indicates that the app is registered to handle URIs with the specified scheme. |
| [uap:ShareTarget](element-uap-sharetarget.md) | Declares an app extension point of type *windows.shareTarget*. The app can share the specified types of files. |
| [uap:VoipCall](element-uap-voipcall.md) | Declares an app extensibility point of type *windows.voipCall* so that your app can declare that it can perform an upgrade from a cellular call to a VoIP video call, and/or whether it is a VoIP app that supports dialing phone numbers directly. |
| [uap:WebAccountProvider](element-uap-webaccountprovider.md) | Declares an app extensibility point of type *windows.webAccountProvider*. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type:CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Remarks

For most types of extensions, Extension@ResourceGroup must match Application@ResourceGroup (if Application@ResourceGroup is omitted then Extension@ResourceGroup should be omitted also).

For a UI-based contract: if Extension@ResourceGroup is not specified then it will be implicitly grouped with the Application; if Extension@ResourceGroup does not match Application@ResourceGroup then the manifest will fail schema validation.

If Extension@ResourceGroup is not specified for a background task, or for a contract that is based on a background task, it will be associated with a default group for all background tasks. Background task contracts are allowed to specify the same values as Application@ResourceGroup.

For the following Extensions, Extension@ResourceGroup allows the background task that is run to be grouped into different processes which will be resource- and lifecycle-managed independently of other groups: *windows.backgroundTasks*, *windows.appServices*, *windows.preinstalledConfigTask*, and *windows.updateTask*.

For example, if the manifest had these three entries.

```xml
<Extension Category="windows.backgroundTasks" EntryPoint="Fabrikam.BackgroundTask" ResourceGroup="Group1">
  <BackgroundTasks>
    <Task Type="timer"/>
  </BackgroundTasks>
</Extension>
<Extension Category="windows.backgroundTasks" EntryPoint="Fabrikam.BackgroundTask2" ResourceGroup="Group2">
  <BackgroundTasks>
    <Task Type="controlChannel"/>
  </BackgroundTasks>
</Extension>
<Extension Category="windows.backgroundTasks" EntryPoint="Fabrikam.BackgroundTask3" ResourceGroup="Group2">
  <BackgroundTasks>
    <Task Type="pushNotification"/>
  </BackgroundTasks>
</Extension>
```

Then the last two background tasks would be activated into the same instance of `backgroundtaskhost.exe` if they were activated concurrently. However, a separate instance of backgroundtaskhost.exe would be spun up for the first entry because it has a different ResourceGroup.

If no ResourceGroup is specified for an extension then all background tasks are activated into the same instance of `backgroundtaskhost.exe`.

Additionally if one of these extensions(*windows.backgroundTasks*, *windows.appServices*, *windows.preinstalledConfigTask*, or *windows.updateTask*) specifies the same value of the ResourceGroup attribute of the parent Application element they will be activated in the same process as the UI.

The following extensions can be found in the declarations tab of the package designer UI - see the descriptions for each of these elements:

- **Search**: Registers the app as a search provider. The app's indexed content can appear as search results in the global search experience launched via the Search charm. Only one instance of this declaration is allowed per app.
- **CachedFileUpdater**: Registers the app as a cached file updater, allowing the app to provider updates to files that are accessed by other Microsoft Store apps. Only one instance of this declaration is allowed per app.
- **Camera Settings**: Enables the app to provide custom control panels for web camera devices. Only one instance of this declaration is allowed per app.
- **AccountPictureProvider**: Registers the app as an account pciture provider, allowing it to be launched in an account picture mode and to set the user's picture without additional prompting. Only one instance of this declaration is allowed per app.
- **PrintTaskSettings**: Enables the app to replace the basic print settings experience. Only one instance of this declaration is allowed per app.
- **LockScreen**: If a phone is locked, there is a limited amount of interaction that the user can perform. In some cases, a user would like to be able to answer a VoIP call without unlocking the phone. This contract makes that possible. Only one instance of this declaration is allowed per app.
- **Alarm**: An application can declare itself as the System Alarm App. When a user goes through the selection UI to set their System Alarm, only applications that are declared as System Alarm Apps can be selected. Only one instance of this declaration is allowed per app.
- **BackgroundTasks**: Background tasks enable applications to communicate with each other and enable one application to call another. In order to use contracts to provide or launch these background tasks, an application need to be declared as an app service. Multiple instances of this declaration are allowed in each app.
- **Print3DWorkFlow**: Manufacturers of 3D printers can provide a Universal Windows app to provide a unique experience in the 3D print dialog. If they do not, Windows provides a default 3D printing experience. Only one instance of this declaration is allowed per app.
- **PersonalAssistantLaunch**: Allows an app to integrate with Cortana. Only one instance of this declaration is allowed per app.

## Requirements

| Item | Value |
|--|--|
| **rescap4** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
