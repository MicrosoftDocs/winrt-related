---
title: uap:AppointmentsProviderLaunchActions
description: Declares actions to take when a appointment is launched (in Package/Applications).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:AppointmentsProvider, uap:AppointmentsProviderLaunchActions]
---

# uap:AppointmentsProviderLaunchActions

Declares actions to take when a appointment is launched.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:AppointmentsProvider>`](element-uap-appointmentsprovider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:AppointmentsProviderLaunchActions>`**  

## Syntax

```xml
<uap:AppointmentsProviderLaunchActions
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".' >

  <!-- Child elements -->
  uap:LaunchAction{0,10}

</uap:AppointmentsProviderLaunchActions>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DesiredView** | The desired amount of screen space to use when the appointment launches. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, *useMinimum*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap:LaunchAction](element-uap-appointmentsproviderlaunchactions-launchaction.md) | Describes an [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) content action. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:AppointmentsProvider](element-uap-appointmentsprovider.md) | Declares an app extensibility point of type **windows.appointmentsProvider**. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

For more info, see [ViewSizePreference](/uwp/api/Windows.UI.ViewManagement.ViewSizePreference) and [DesiredRemainingView](/uwp/api/Windows.System.LauncherOptions).

## Examples

<!-- Author content goes here -->
