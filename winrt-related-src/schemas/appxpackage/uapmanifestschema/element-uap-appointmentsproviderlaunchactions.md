---
description: Declares actions to take when a appointment is launched (in Package/Applications).
Search.Product: eADQiWindows 10XVcnh
title: uap:AppointmentsProviderLaunchActions (Windows 10)
ms.assetid: cc9178da-2a91-4c00-8af1-6c86a54cc7e3
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:AppointmentsProviderLaunchActions (Windows 10)

Declares actions to take when a appointment is launched.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:AppointmentsProvider\>](element-uap-appointmentsprovider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:AppointmentsProviderLaunchActions\>**

## Syntax

```xml
<uap:AppointmentsProviderLaunchActions
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".' >

  <!-- Child elements -->
  uap:LaunchAction{0,10}

</uap:AppointmentsProviderLaunchActions>
```

### Key

`{}`  specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DesiredView** | The desired amount of screen space to use when the appointment launches. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, or *useMinimum*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [uap:LaunchAction (global)](element-2-uap-launchaction.md) | Describes an [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) content action. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:AppointmentsProvider](element-uap-appointmentsprovider.md) | Declares an app extensibility point of type *windows.appointmentsProvider*. |

## Remarks

For more info, see [ViewSizePreference](/uwp/api/Windows.UI.ViewManagement.ViewSizePreference) and [DesiredRemainingView](/uwp/api/Windows.System.LauncherOptions).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
