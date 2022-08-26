---
description: Describes an uap:AppointmentsProviderLaunchActions content action.
Search.Product: eADQiWindows 10XVcnh
title: uap:LaunchAction (in AppointmentsProviderLaunchActions)
ms.assetid: 1058a98d-10a0-4ce2-8b10-84d5c8fb9da6
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:LaunchAction (in AppointmentsProviderLaunchActions)

Describes an [**uap:AppointmentsProviderLaunchActions**](element-uap-appointmentsproviderlaunchactions.md) content action.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:AppointmentsProvider\>](element-uap-appointmentsprovider.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:AppointmentsProviderLaunchActions\>](element-uap-appointmentsproviderlaunchactions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:LaunchAction\>**

## Syntax

```xml
<LaunchAction
    EntryPoint = 'A string with an optional value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead.'
    Executable = 'A string with an optional value between 1 and 256 characters in length, that must end with ".exe", and cannot contain the following characters: <, >, :, ", |, ?, or *. Specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If the EntryPoint property is not specified, the EntryPoint defined for the app is used'
    RuntimeType = 'A string with an optional value between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.'
    StartPage = 'A string with an optional value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.'
    ResourceGroup = 'An alphanumeric string with an optional value between 1 and 255 characters in length. Must begin with a letter.'
    Verb = 'A string that can have any of the following values: "addAppointment", "removeAppointment", "replaceAppointment", "showTimeFrame", or "showAppointmentDetails".'
    DesiredView = 'A string that can have any of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum". />
```

### Key

`?`   optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| EntryPoint | The activatable class ID. | A string with a value between 1 and 256 characters in length. Represents the task handling the extension (normally the fully namespace-qualified name of a Windows Runtime type). If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |  |
| Executable | The default launch executable. | A string with a value between 1 and 256 characters in length, that must end with `.exe`, and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. Specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |  |
| RuntimeType | The runtime provider. Typically used when there are mixted frameworks in an app. | A string with a value between 1 and 255 characters in length that cannot start or end with a `.` or contain there characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| StartPage | The web page that handles the extensibility point. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | No |  |
| ResourceGroup | An optional tag used to group extension activations together for resource management purposes (for example, CPU and memory). See the **Remarks** section in *[Application@ResourceGroup](element-application.md)*. | An alphanumeric string between 1 and 255 characters in length. Must begin with a letter. | No |  |
| Verb | A unique identifier that is passed to the app when it is launched. The app can use this string to determine which **[uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md)**  handler triggered its launch. It is unique per application in the package and is case sensitive. | A string that can have any of the following values: *addAppointment*, *removeAppointment*, *replaceAppointment*, *showTimeFrame*, or *showAppointmentDetails*. | No |  |
| DesiredView | The desired amount of screen space to use when the appointment launches. | A string that can have any of the following values: *default*, *useLess*, *useHalf*, *useMore*, or *useMinimum*. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:AppointmentsProviderLaunchActions](element-uap-appointmentsproviderlaunchactions.md) | Declares actions to take when a appointment is launched. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[uap:LaunchAction (in type: *CT_AutoPlayContent*)](element-uap-launchaction.md)**
- **[uap:LaunchAction (in type: *CT_AutoPlayDevice*)](element-1-uap-launchaction.md)**

## Remarks

For more info about launch actions that an appointments provider takes, see [**AppointmentsProviderLaunchActionVerbs**](/uwp/api/Windows.ApplicationModel.Appointments.AppointmentsProvider.AppointmentsProviderLaunchActionVerbs).

**LaunchAction (in *AppointmentsProviderLaunchActions*)** has these semantic validations:

- [**Extension**](../appxmanifestschema2010-v2/element-extension.md) base attributes must follow these rules:

  - If the **StartPage** attribute is specified, fail if the **EntryPoint**, **Executable**, or **RuntimeType** attribute is specified.
  - Otherwise, fail if the **Executable** or **RuntimeType** attribute is specified without an **EntryPoint** specified.

- If **LaunchAction (in *AppointmentsProviderLaunchActions*)** defines the **EntryPoint** attribute, either this **LaunchAction (in *AppointmentsProviderLaunchActions*)** or the parent [**uap:Extension**](element-uap-extension.md) or [**Application**](element-application.md) element must specify an **Executable** attribute.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |