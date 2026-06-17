---
title: uap:AppointmentsProvider
description: Declares an app extensibility point of type windows.appointmentsProvider (in Package/Applications).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:AppointmentsProvider]
---

# uap:AppointmentsProvider

Declares an app extensibility point of type **windows.appointmentsProvider**.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:AppointmentsProvider>`**  

## Syntax

```xml
<uap:AppointmentsProvider>

  <!-- Child elements -->
  uap:AppointmentsProviderLaunchActions?

</uap:AppointmentsProvider>
```

### Key

`?` optional (zero or one)

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) | Declares actions to take when a appointment is launched. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

For info about appointments and the appointments provider, see [Windows.ApplicationModel.Appointments](/uwp/api/Windows.ApplicationModel.Appointments) and [Windows.ApplicationModel.Appointments.AppointmentsProvider](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider).

## Examples

<!-- Author content goes here -->
