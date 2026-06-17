---
title: uap:LaunchAction (in AutoPlayDevice)
description: Describes an AutoPlay device action (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:AutoPlayDevice, uap:LaunchAction]
---

# uap:LaunchAction (in AutoPlayDevice)

Describes an AutoPlay device action.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:AutoPlayDevice>`](element-uap-autoplaydevice.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:LaunchAction>`**  

## Syntax

```xml
<uap:LaunchAction
  Verb = 'A required string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only.'
  ActionDisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  DeviceEvent = 'A required string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Verb** | A unique identifier passed to the app when it's launched. The app uses this string to determine which AutoPlay handler triggered its launch. It's unique per app in the package and is case sensitive. | A string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only. | Yes |  |
| **ActionDisplayName** | The name displayed to the user in the AutoPlay flyout for the handler. This string is localizable. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **DeviceEvent** | The name of a device-related event that the extensibility point handles. For more info, see **Remarks**. | A string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:AutoPlayDevice](element-uap-autoplaydevice.md) | Declares an app extensibility point of type **windows.autoPlayDevice**. The app provides the specified AutoPlay device actions. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

**ContentEvent** can be a custom event defined for the device. For WPD devices, **ContentEvent** can be one of the following well-known events:

- **WPD\\AudioSource**
- **WPD\\ImageSource**
- **WPD\\VideoSource**

## Examples

```xml
<uap:Extension Category="windows.autoPlayDevice">
  <uap:AutoPlayContent>
    <uap:LaunchAction Verb="import" ActionDisplayName="Import" ContentEvent="WPD\ImageSource"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

## See also
The following elements have the same name as this one, but different content or attributes:

- **[uap:LaunchAction (type: CT_AutoPlayContent)](element-uap-autoplaycontent-launchaction.md)**
- **[uap:LaunchAction (global)](element-uap-appointmentsproviderlaunchactions-launchaction.md)**
