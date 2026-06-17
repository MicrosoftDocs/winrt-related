---
title: uap:LaunchAction (in AppointmentsProviderLaunchActions)
description: Describes an uap:AppointmentsProviderLaunchActions content action.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:AppointmentsProvider, uap:AppointmentsProviderLaunchActions, uap:LaunchAction]
---

# uap:LaunchAction (in AppointmentsProviderLaunchActions)

Describes an [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) content action.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:AppointmentsProvider>`](element-uap-appointmentsprovider.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:AppointmentsProviderLaunchActions>`](element-uap-appointmentsproviderlaunchactions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:LaunchAction>`**  

## Syntax

```xml
<uap:LaunchAction
  Verb = 'A required string that can have one of the following values: "addAppointment", "removeAppointment", "replaceAppointment", "showTimeFrame", or "showAppointmentDetails".'
  DesiredView = 'An optional string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  Executable = 'An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  EntryPoint = 'An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character.'
  RuntimeType = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  StartPage = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
  ResourceGroup = 'An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Verb** | A unique identifier that is passed to the app when it is launched. The app can use this string to determine which [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) handler triggered its launch. It is unique per application in the package and is case sensitive. | A string that can have one of the following values: *addAppointment*, *removeAppointment*, *replaceAppointment*, *showTimeFrame*, *showAppointmentDetails*. | Yes |  |
| **DesiredView** | The desired amount of screen space to use when the appointment launches. | An optional string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, *useMinimum*. | No |  |
| **Executable** | The default launch executable. | An optional string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **EntryPoint** | The activatable class ID. | An optional string between 1 and 256 characters in length that cannot start or end with a whitespace character. | No |  |
| **RuntimeType** | The runtime provider. Typically used when there are mixed frameworks in an app. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **StartPage** | The web page that handles the extensibility point. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |
| **ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). | An optional alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) | Declares actions to take when a appointment is launched. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

For more info about launch actions that an appointments provider takes, see [AppointmentsProviderLaunchActionVerbs](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider.AppointmentsProviderLaunchActionVerbs).

**LaunchAction (in AppointmentsProviderLaunchActions)** has these semantic validations:

- [Extension](../appxmanifestschema2010-v2/element-extension.md) base attributes must follow these rules:

  - If the **StartPage** attribute is specified, fail if the **EntryPoint**, **Executable**, or **RuntimeType** attribute is specified.
  - Otherwise, fail if the **Executable** or **RuntimeType** attribute is specified without an **EntryPoint** specified.

- If **LaunchAction (in AppointmentsProviderLaunchActions)** defines the **EntryPoint** attribute, either this **LaunchAction (in AppointmentsProviderLaunchActions)** or the parent [uap:Extension](element-uap-extension.md) or [Application](element-f-application.md) element must specify an **Executable** attribute.

## Examples

<!-- Author content goes here -->

## See also
The following elements have the same name as this one, but different content or attributes:

- **[uap:LaunchAction (in type: CT_AutoPlayContent)](element-uap-autoplaycontent-launchaction.md)**
- **[uap:LaunchAction (in type: CT_AutoPlayDevice)](element-uap-autoplaydevice-launchaction.md)**
