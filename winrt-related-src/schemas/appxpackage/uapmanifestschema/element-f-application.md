---
title: Application
description: Represents an app that comprises part of or all of the functionality delivered in the package (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Applications, Application]
---

# Application

Represents an app that comprises part of or all of the functionality delivered in the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Application>`**

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Application
    Id = 'A required value. <!-- TODO: Add description for t:ST_ApplicationId -->'
    Executable = 'An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
    EntryPoint = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
    StartPage = 'An optional value. <!-- TODO: Add description for t:ST_ApplicationStartPage -->'
    ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
    desktop4:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
    iot2:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
    uap10:Subsystem = 'An optional string that can have one of the following values: "console", or "windows".'
    desktop4:SupportsMultipleInstances = 'An optional boolean value.'
    iot2:SupportsMultipleInstances = 'An optional boolean value.'
    uap10:SupportsMultipleInstances = 'An optional boolean value.'
    uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *.'
    uap11:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    previewsecurity:TrustLevel = 'An optional string that can have one of the following values: "appContainer", "mediumIL", or "appSilo".'
    uap10:TrustLevel = 'An optional string that can have one of the following values: "appContainer", or "mediumIL".'
    uap10:RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
    uap10:HostId = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
    uap10:Parameters = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    previewsecurity2:RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", "win32App", or "appSilo".'
    uap16:BaseNamedObjectsIsolation = 'An optional string that can have one of the following values: "none", or "package".'
    uap17:BaseNamedObjectsIsolation = 'An optional string that can have one of the following values: "none", or "package".'
    desktop11:AppLifecycleBehavior = 'An optional string that can have one of the following values: "systemManaged", or "unmanaged".' >

    <!-- Child elements -->
    VisualElementsChoice
    ApplicationContentUriRules?
    Extensions?
    Properties?

  </Application>
</Package>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The unique identifier of the application within the package. This value is sometimes referred to as the package-relative app identifier (PRAID). The ID is unique within the package but not globally. There may be another package on the system that uses the same ID. The same ID cannot be used more than once in the same package. When using a Visual Studio template, the default value of this attribute is *App*. Developers should manually change this in the manifest. The app's identifier should not be changed after the app has been published to the Microsoft Store; doing so will disrupt the tile's position on the Start screen. | A value. <!-- TODO: Add data type for t:ST_ApplicationId --> | Yes |  |
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional value. <!-- TODO: Add data type for t:ST_ApplicationStartPage --> | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **desktop4:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **iot2:Subsystem** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **uap10:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | An optional string that can have one of the following values: *console*, *windows*. | No |  |
| **desktop4:SupportsMultipleInstances** | Indicates support of multiple, separate instances of UWP apps. For more info, see the remarks section. | An optional boolean value. | No |  |
| **iot2:SupportsMultipleInstances** | <!-- TODO: Add description --> | An optional boolean value. | No |  |
| **uap10:SupportsMultipleInstances** | Indicates support of multiple, separate instances of UWP apps. For more info, see the remarks section. | An optional boolean value. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when launching the process. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string that cannot contain these characters: <, >, &#124;, ?, or *. | No |  |
| **uap11:Parameters** | Contains command line parameters to pass to the extension. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **previewsecurity:TrustLevel**| <!-- TODO: Add description --> | An optional string that can have one of the following values: *appContainer*, *mediumIL*, *appSilo*. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string that can have one of the following values: *appContainer*, *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, *win32App*. | No |  |
| **uap10:HostId** | Specifies the ID of the host runtime for the extension. | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have package identity. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **previewsecurity2:RuntimeBehavior** | <!-- TODO: Add description --> | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, *win32App*, *appSilo*. | No |  |
| **uap16:BaseNamedObjectsIsolation** | Enables BaseNameObject (BNO) isolation for the app. | An optional string that can have one of the following values: *none*, *package*. | No |  |
| **uap17:BaseNamedObjectsIsolation** | Enables BaseNameObject (BNO) isolation for the app. | An optional string that can have one of the following values: *none*, *package*. | No |  |
| **desktop11:AppLifecycleBehavior** | Allows an app to override the lifecycle behavior associated with the runtime behavior for the extension. Apps or extensions with a **RuntimeBehavior** of "windowsApp" implicitly have **AppLifecycleBehavior** of "systemManaged" unless otherwise specified. Apps or extensions with **RuntimeBehavior** of "packagedClassicApp" or "win32App" implicitly have **AppLifecycleBehavior** of "unmanaged" unless otherwise specified. | An optional string that can have one of the following values: *systemManaged*, *unmanaged*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |
| [Extensions](element-f-application-extensions.md) | Defines one or more extensibility points for the app. |
| [uap7:Properties](element-uap7-properties.md) | Properties of an application. |

## Parent elements

| Parent element | Description |
|-|-|
| [Applications](element-f-applications.md) | Represents one or more apps that comprise the package. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **desktop11** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/11` |
| **desktop4** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **iot2** | `http://schemas.microsoft.com/appx/manifest/iot/windows10/2` |
| **previewsecurity** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/security` |
| **previewsecurity2** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/security/2` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **uap11** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/11` |
| **uap16** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/16` |
| **uap17** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

The **Application** element contains attributes that are common to the extensibility points that pertain to the app. This info is used by other extensibility points to get info about the app. **Application** attributes are also used as *activation info* in the startup and management of an instance of the app (in other words, they describe how to start a process, and with what behavior).

The **StartPage** attribute applies only to JavaScript apps. If **StartPage** isn't specified, then both the **Executable** and **EntryPoint** attributes must be specified (and that applies only to C#, C++, or VB apps).

### uap10 was introduced in Windows 10, version 2004 (10.0; Build 19041)

The `uap10` namespace (for `uap10:RuntimeBehavior` and `uap10:TrustLevel`) was introduced in Windows 10, version 2004 (10.0; Build 19041). If your package installs on systems older than that, then you need to provide an equivalent combination of attributes (see the following section), otherwise the activation info will be incomplete, and the install will fail.

But if your package has `<TargetDeviceFamily MinVersion="10.0.19041.0">`, or higher, then it installs only on systems that support the `uap10` namespace. In that case, you should use the `uap10:RuntimeBehavior` and `uap10:TrustLevel` attributes in preference to the older equivalent combinations (see the following section).

### Combinations of activation info attributes

You can specify activation info attributes on the **Application** element; and you can optionally specify them on an app-scope [Extension](/uwp/schemas/appxpackage/uapmanifestschema/element-1-extension) element. If they're not specified on **Extension**, then they're inherited from the parent **Application**. You specify these attributes in combinations&mdash;for example, **EntryPoint**, **RuntimeBehavior**, and **TrustLevel** have overlapping meaning, and they're specified (and/or inherited) in combinations. Here are some valid combinations of activation info attributes.

1. **Executable**, **uap10:RuntimeBehavior**="packagedClassicApp", **uap10:TrustLevel**=["mediumIL", or "appContainer" (the default if omitted)]
1. **Executable**, **uap10:RuntimeBehavior**="win32App", **uap10:TrustLevel**="mediumIL" (for other requirements, see the Description earlier in this topic for **uap10:RuntimeBehavior**).
1. **Executable**, **EntryPoint**="windows.fullTrustApplication" (equivalent to **uap10:RuntimeBehavior**="packagedClassicApp", **uap10:TrustLevel**="mediumIL")
1. **Executable**, **EntryPoint**="windows.partialTrustApplication" (equivalent to **uap10:RuntimeBehavior**="packagedClassicApp", **uap10:TrustLevel**="appContainer")
1. **Executable**, **EntryPoint**="\<anything else>"

As you can see, if your target system doesn't support the `uap10` namespace, then you can specify the **EntryPoint** attribute instead. Similarly, the equivalent of **uap10:TrustLevel**="appContainer"` on older systems is **EntryPoint**="windows.partialTrustApplication".

But it's redundant to specify both **uap10:RuntimeBehavior**/**uap10:TrustLevel** and **EntryPoint** at the same time. But if you do that, then it's an error if they contradict.

Universal Windows Platform (UWP) app activations require **EntryPoint**. So if you specify **Executable** and **uap10:RuntimeBehavior**="windowsApp" (with no **EntryPoint**), then that's an error. In this same case, **EntryPoint** would specify something other than "windows.fullTrustApplication" and "windows.partialTrustApplication"; and values other than those two already say the same thing as **uap10:RuntimeBehavior**="windowsApp". So **uap10:RuntimeBehavior** would be redundant in this case, and you'd specify **Executable** and **EntryPoint**.

Setting **uap10:RuntimeBehavior**="win32App" and **uap10:TrustLevel**="appContainer" isn't supported.

Setting `uap10:TrustLevel="mediumIL"` while `uap10:RuntimeBehavior="windowsApp"` requires the `Microsoft.coreAppActivation_8wekyb3d8bbwe` Custom Capability.

This is also true if `uap10:TrustLevel="mediumIL"` and `EntryPoint` is any other value than `"windows.fullTrustApplication"` or `"windows.partialTrustApplication"`.

You can read more about this custom capability here in [Custom Capabilities](/windows/uwp/packaging/app-capability-declarations#custom-capabilities).

### Important notes about multi-instancing apps

- If an app declares **SupportsMultipleInstances** within the **Application** element, then all foreground extensions will also be multi-instanced.
- If the app declares **SupportsMultipleInstances** within the **Application** element, then it does not need to be declared at the [Extensions](element-f-application-extensions.md) level (for example, in a [BackgroundTasks](element-f-backgroundtasks.md) or [AppService](element-uap3-appservice.md) element).
- The app should only declare **SupportsMultipleInstances** on background tasks, background audio, or app services.
- Console apps will always be multi-instanced and must explicitly declare **SupportsMultipleInstances**.
- Apps can use the **ResourceGroup** declaration in the manifest to group multiple background tasks into the same host. This conflicts with multi-instancing, where each activation goes into a separate host. Therefore, an app cannot declare both **SupportsMultipleInstances** and **ResourceGroup** in the manifest.

For more info about using the **SupportsMultipleInstances** attribute to support multiple, separate instances of UWP apps, see [Create a multi-instance Universal Windows App](/windows/uwp/launch-resume/multi-instance-uwp).

## Examples

<!-- Author content goes here -->
