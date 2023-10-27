---
description: Declares an app extensibility point of type windows.appointmentsProvider (in Package/Applications).
Search.Product: eADQiWindows 10XVcnh
title: uap:AppointmentsProvider (Windows 10)
ms.assetid: 017359a9-e1c5-4b47-8598-bc8c49a67e4a
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:AppointmentsProvider (Windows 10)

Declares an app extensibility point of type **windows.appointmentsProvider**.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:AppointmentsProvider\>**

## Syntax

```xml
<uap:AppointmentsProvider>

  <!-- Child elements -->
  uap:AppointmentsProviderLaunchActions?

</uap:AppointmentsProvider>
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) | Declares actions to take when a appointment is launched. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-extension.md) | Declares an extensibility point for the app. |

## Remarks

For info about appointments and the appointments provider, see [Windows.ApplicationModel.Appointments](/uwp/api/Windows.ApplicationModel.Appointments) and [Windows.ApplicationModel.Appointments.AppointmentsProvider](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
