---
description: Represents an app that comprises part of or all of the functionality delivered in the package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Application (Windows 10)
ms.assetid: 39221d13-bb46-42ac-be51-117357cade81
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 12/16/2022
---

# Application (Windows 10)

Represents an app that comprises part of or all of the functionality delivered in the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Application\>**

## Syntax

```xml
<Application
  EntryPoint? = 'See the Attributes table for more info.'
  Executable?
  uap10:HostId?
  Id
  uap10:Parameters?
  ResourceGroup?
  uap10:RuntimeBehavior?
  StartPage?
  desktop4:Subsystem?
  uap10:Subsystem?
  desktop4:SupportsMultipleInstances?
  uap10:SupportsMultipleInstances?
  uap10:TrustLevel?>

  <!-- Child elements -->
  uap:ApplicationContentUriRules?
  Extensions?
  uap7:Properties
  uap:VisualElements

</Application>
```

### Key

`?`   optional (zero or one)<br/>
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **EntryPoint** | The activatable class ID (for example, "Office.Winword.Class"), or "windows.fullTrustApplication", or "windows.partialTrustApplication". If you specify **EntryPoint**, then you must also specify the **Executable** attribute. If you specify **EntryPoint**, then you must not specify the **StartPage** attribute. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type; but it can be one of the special values "windows.fullTrustApplication" or "windows.partialTrustApplication". If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **Executable** | The default launch executable for the app. The specified file must be present in the package. On older systems (see the remarks section for details), if you specify **Executable**, then you must also specify the **EntryPoint** attribute. If you specify **Executable**, then you must *not* specify the **StartPage** attribute. | A string between 1 and 256 characters in length that must end with `.exe` and can't contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **uap10:HostId** | The app ID of the host app for the current app. This attribute is used for [hosted apps](/windows/uwp/launch-resume/hosted-apps). | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **Id** | The unique identifier of the application within the package. This value is sometimes referred to as the package-relative app identifier (PRAID). The ID is unique within the package but not globally. There may be another package on the system that uses the same ID. The same ID cannot be used more than once in the same package. When using a Visual Studio template, the default value of this attribute is *App*. Developers should manually change this in the manifest. The app's identifier should not be changed after the app has been published to the Microsoft Store; doing so will disrupt the tile's position on the Start screen. | An ASCII string between 1 and 64 characters in length. This string contains alpha-numeric fields separated by periods. Each field must begin with an ASCII alphabetic character. You cannot use these as field values: *CON*, *PRN*, *AUX*, *NUL*, *COM1*, *COM2*, *COM3*, *COM4*, *COM5*, *COM6*, *COM7*, *COM8*, *COM9*, *LPT1*, *LPT2*, *LPT3*, *LPT4*, *LPT5*, *LPT6*, *LPT7*, *LPT8*, and *LPT9*. | Yes |  |
| **uap10:Parameters** | Contains command line parameters to pass to the app. Only supported for [desktop apps](/windows/apps/desktop/) that have package identity (see [Deployment overview](/windows/apps/package-and-deploy/)). | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **ResourceGroup** | A tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the app.<br/><br/>"packagedClassicApp"&mdash;a WinUI 3 app, or a Desktop Bridge app (Centennial). For a WinUI 3 app, usually goes with a **TrustLevel** of "mediumIL" (but "appContainer" is also an option).<br/><br/>"win32App"&mdash;any other kind of Win32 app, including an app packaged with external location. Needs the "Unvirtualized Resources" restricted capability (see [App capability declarations](/windows/uwp/packaging/app-capability-declarations)). Usually goes with a **TrustLevel** of "mediumIL" (but "appContainer" is also an option).<br/><br/>"windowsApp"&mdash;a Universal Windows Platform (UWP) app. Always goes with a **TrustLevel** of "appContainer".<br/><br/>All share common properties (some declared in `appxmanifest.xml`), and run as a process with package identity and application identity. You can think of them as being in two groups. One group is UWP apps ("windowsApp"); the other is Windows `.exe`s with **main** or **WinMain** ("packagedClassicApp" or "win32App"). That second group is also known as *desktop apps*. | A string with one of the following values: "packagedClassicApp", "win32App", or "windowsApp". | No |  |
| **StartPage** | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Any valid URI or IRI (the non-ASCII version of a URI). | No |  |
| **desktop4:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | A string that can be any of the following values: *console* or *windows*. | No |  |
| **uap10:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | A string that can be any of the following values: *console* or *windows*. | No |  |
| **desktop4:SupportsMultipleInstances** | Indicates support of multiple, separate instances of UWP apps. For more info, see the remarks section. | A boolean value. | No |  |
| **uap10:SupportsMultipleInstances** | Indicates support of multiple, separate instances of UWP apps. For more info, see the remarks section. | A boolean value. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the app<br/><br/>"mediumIL"&mdash;the app is *full trust*; its process runs with an integrity level of *medium* (see [Mandatory Integrity Control](/windows/win32/secauthz/mandatory-integrity-control)). Needs the "Full Trust Permission Level" restricted capability (see [App capability declarations](/windows/uwp/packaging/app-capability-declarations)).<br/><br/>"appContainer"&mdash;the app runs in a lightweight app container (see [MSIX AppContainer apps](/windows/msix/msix-container)); its process runs with an integrity level of *low*. It's also possible for an unpackaged app to run in an AppContainer. | A string with one of the following values: "mediumIL" or "appContainer". | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |
| [uap7:Properties](element-uap7-properties.md) | Specifies properties of the app. |
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |

### Parent elements

| Parent element | Description |
|-|-|
| [Applications](element-applications.md) | Represents one or more apps that comprise the package. |

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

### Important notes about multi-instancing apps

- If an app declares **SupportsMultipleInstances** within the **Application** element, then all foreground extensions will also be multi-instanced.
- If the app declares **SupportsMultipleInstances** within the **Application** element, then it does not need to be declared at the [Extensions](element-1-extensions.md) level (for example, in a [BackgroundTasks](element-backgroundtasks.md) or [AppService](element-uap3-appservice-manual.md) element).
- The app should only declare **SupportsMultipleInstances** on background tasks, background audio, or app services.
- Console apps will always be multi-instanced and must explicitly declare **SupportsMultipleInstances**.
- Apps can use the **ResourceGroup** declaration in the manifest to group multiple background tasks into the same host. This conflicts with multi-instancing, where each activation goes into a separate host. Therefore, an app cannot declare both **SupportsMultipleInstances** and **ResourceGroup** in the manifest.

For more info about using the **SupportsMultipleInstances** attribute to support multiple, separate instances of UWP apps, see [Create a multi-instance Universal Windows App](/windows/uwp/launch-resume/multi-instance-uwp).

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **desktop4** attributes | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **uap10** attributes | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
