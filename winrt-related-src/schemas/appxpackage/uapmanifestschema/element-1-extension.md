---
description: Declares an extensibility point for the package (in Application/Extensions).
Search.Product: eADQiWindows 10XVcnh
title: Extension (in Application/Extensions) (Windows 10)
ms.assetid: e25d664a-67e8-4a22-a666-1b11286b58f3
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 05/01/2023
---

# Extension (in Application/Extensions) (Windows 10)

Declares an extensibility point for the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Extension\>**

## Syntax

```xml
<Extension
  Category = 'One of the following values: "windows.backgroundTasks", "windows.preInstalledConfigTask", "windows.updateTask", or "windows.restrictedLaunch".'
  Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  RuntimeType = 'A string with an optional value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
  StartPage = 'A string with an optional value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:TrustLevel = 'An optional string value. If specified, it must be either "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior  = 'An optional string value. If specified, it must be one of the following values:  "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with an letter.'
  uap10:Parameters = 'A string with an optional value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
/>

  <!-- Child elements -->
  BackgroundTasks?

</Extension>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | Can be one of the following values: *windows.backgroundTasks*, *windows.preInstalledConfigTask*, *windows.updateTask*, or *windows.restrictedLaunch*. | Yes |  |
| **EntryPoint** | The activatable class ID. | A string with a value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **Executable** | The default launch executable. | A string with a value between 1 and 256 characters in length, that must end with `.exe`, and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixted frameworks in an app. | A string with a value between 1 and 255 characters in length that cannot start or end with a `.` or contain there characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **StartPage** | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string value. If specified, it can be one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the runtime behavior of an extension. <br/><br/> For more info and requirements, see `uap10:RuntimeBehavior` in the topic for the [Application (Windows 10)](/uwp/schemas/appxpackage/uapmanifestschema/element-application) element. | An optional string value. If specified, it can be one of the following values: "packagedClassicApp", "win32App", or "windowsApp". | No |  |
| **uap10:HostId** | Specifies the app ID of the host app for the extension. | An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the extension. Only supported for desktop apps that have a package identity. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [BackgroundTasks](element-backgroundtasks.md) | Defines an app extensibility point of type **windows.backgroundTasks**. Background tasks run in a dedicated background host; that is, without a UI. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[Extension (in type: CT_PackageExtensions)](element-extension.md)**

## Remarks

If activation info attributes aren't specified on **Extension**, then they're inherited from the parent [Application](/uwp/schemas/appxpackage/uapmanifestschema/element-application). See the remarks section for the **Application** element.

Extensibility points are a mechanism by which a package can add functionality in a manner defined by the operating system. An extensibility point is a location where an app can register to execute code or use resources of the current package. To add functionality for a particular app, use the [Application](element-application.md) child element of the [Applications](element-applications.md) element.

The **windows.certificates** extensibility point can't be declared multiple times in a manifest.

> [!NOTE]
> Either the **EntryPoint** or **StartPage** attribute is required if the **Category** attribute is `windows.UpdateTask` or `windows.preInstalledConfigTask` for versions of Windows 10 before Windows 10, version 1607. Starting with Windows 10, version 1607, you no longer need to specify a value for **EntryPoint** or **StartPage** when **Category** is `windows.Use`, **UpdateTask**, or `windows.preInstalledConfigTask` to target only devices that run Windows 10, version 1607 or later.

## See also

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
