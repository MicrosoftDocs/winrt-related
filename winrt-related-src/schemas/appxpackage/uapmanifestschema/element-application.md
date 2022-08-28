---
description: Represents an app that comprises part of or all of the functionality delivered in the package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Application (Windows 10)
ms.assetid: 39221d13-bb46-42ac-be51-117357cade81
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 03/21/2019
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
  Id = 'An ASCII string between 1 and 64 characters in length. See the Attributes table for more information on character restrictions.'
  Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used.'
  EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
  StartPage = 'Any valid URI or IRI (the non-ASCII version of a URI). See below for more details.' 
  ResourceGroup = 'An alphanumeric string between 1 and 255 characters in length. Must begin with an letter.'
  desktop4:Subsystem = 'A string that can have one of the following values: "console" or "windows".'
  uap10:Subsystem = 'A string that can have one of the following values: "console" or "windows".'
  desktop4:SupportsMultipleInstances = 'An optional boolean value.'
  uap10:SupportsMultipleInstances = 'An optional boolean value.'
  uap10:TrustLevel = 'A string that can have one of the following values: "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior  = 'A string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string between 1 and 255 characters in length. Must begin with a letter.'
  uap10:Parameters   = 'A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  uap:VisualElements
  uap:ApplicationContentUriRules?
  Extensions?

</Application>
```

### Key

`?`   optional (zero or one)
`&`   interleave connector (may occur in any order)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The unique identifier of the application within the package. This value is sometimes referred to as the package-relative app identifier (PRAID). The ID is unique within the package but not globally. There may be another package on the system that uses the same ID. The same ID cannot be used more than once in the same package. When using a Visual Studio template, the default value of this attribute is *App*. Developers should manually change this in the manifest. The app's identifier should not be changed after the app has been published to the Microsoft Store; doing so will disrupt the tile's position on the Start screen. | An ASCII string between 1 and 64 characters in length. This string contains alpha-numeric fields separated by periods. Each field must begin with an ASCII alphabetic character. You cannot use these as field values: *CON*, *PRN*, *AUX*, *NUL*, *COM1*, *COM2*, *COM3*, *COM4*, *COM5*, *COM6*, *COM7*, *COM8*, *COM9*, *LPT1*, *LPT2*, *LPT3*, *LPT4*, *LPT5*, *LPT6*, *LPT7*, *LPT8*, and *LPT9*. | Yes |  |
| **EntryPoint** | The activatable class ID (for example, "Office.Winword.Class"). If you specify this attribute, you must also specify the **Executable** attribute. If you specify this attribute you must not specify the **StartPage** attribute. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| **Executable** | The default launch executable for the app. This file must be present in the package. If you specify this attribute you must specify the **EntryPoint** attribute. If you specify this attribute you must not specify the **StartPage** attribute. | A string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |  |
| **StartPage** | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| **ResourceGroup** | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **desktop4:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | A string that can be any of the following values: *console* or *windows*. | No |  |
| **uap10:Subsystem** | Indicates whether the app is a standard UWP app or a UWP console app. | A string that can be any of the following values: *conole* or *windows*. | No |  |
| **desktop4:SupportsMultipleInstances** | Indicates support of multiple, separate instances of UWP apps. For more information, see the remarks section. | An optional boolean value | No |  |
| **uap10:SupportsMultipleInstances** | Indicates support of multiple, separate instances of UWP apps. For more information, see the remarks section. | An optional boolean value. | No |  |
| **uap10:TrustLevel** | Specifies the trust level of the app. | A string that can be any of the following values: "appContainer" or "mediumIL". | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the app. | A string that can be any of the following values: "windowsApp", "packagedClassicApp", or "win32App". | No |  |
| **uap10:HostId** | This value specifies the app ID of the host app for the current app. This attribute is used for [hosted apps](/windows/uwp/launch-resume/hosted-apps). | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap10:Parameters** | Contains command line parameters to pass to the app. Only supported for desktop apps that have package identity. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Extensions (type: CT_ApplicationExtensions)](element-1-extensions.md) | Defines one or more extensibility points for the app. |
| [uap:ApplicationContentUriRules](element-uap-applicationcontenturirules.md) | Specifies which pages in the web context have access to the system's geolocation devices (if the app has permission to access this capability) and access to the clipboard. |
| [uap:VisualElements](element-uap-visualelements.md) | Describes the visual aspects of the app: its default tile, logo images, text and background colors, initial screen orientation, splash screen, and lock screen tile appearance. |
| [uap7:Properties](element-uap7-properties.md) | Specifies properties of the app. |

### Parent elements

| Parent element | Description |
|-|-|
| [Applications](element-applications.md) | Represents one or more apps that comprise the package. |

## Remarks

The **Application** element contains attributes that are common to the extensibility points that pertain to the app. This information is used by other extensibility points to get information about the app. Also, **Application** attributes are used in the start and management of an instance of the app.

The **StartPage** applies only to a JavaScript app. If **StartPage** is not specified, then both the **Executable** and **EntryPoint** attributes must be specified, and this applies only to a C#, C++, or VB app.

Important notes about multi-instancing apps:

- If an app declares **SupportsMultipleInstances** within the **Application** element, then all foreground extensions will also be multi-instanced.
- If the app declares **SupportsMultipleInstances** within the **Application** element, then it does not need to be declared at the [Extensions](element-1-extensions.md) level (for example, in a [BackgroundTasks](element-backgroundtasks.md) or [AppService](element-uap3-appservice-manual.md) element).
- The app should only declare **SupportsMultipleInstances** on background tasks, background audio, or app services.
- Console apps will always be multi-instanced and must explicitly declare **SupportsMultipleInstances**.
- Apps can use the **ResourceGroup** declaration in the manifest to group multiple background tasks into the same host. This conflicts with multi-instancing, where each activation goes into a separate host. Therefore, an app cannot declare both **SupportsMultipleInstances** and **ResourceGroup** in the manifest.

For more information about using the **SupportsMultipleInstances** attribute to support multiple, separate instances of UWP apps, see [Create a multi-instance Universal Windows App](/windows/uwp/launch-resume/multi-instance-uwp).

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **desktop4** attributes | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |
| **uap10** attributes | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
