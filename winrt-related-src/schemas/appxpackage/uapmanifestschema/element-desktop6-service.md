---
title: desktop6:Service
description: Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop6:Extension, desktop6:Service]
---

# desktop6:Service

Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:Service>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop6:Extension>`](element-desktop6-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop6:Service>`**

## Syntax

```xml
<desktop6:Service
  Name = 'A required value. <!-- TODO: Add description for desktop6:ST_ServiceName -->'
  StartupType = 'A required string that can have one of the following values: "auto", "manual", or "disabled".'
  StartAccount = 'A required string that can have one of the following values: "localSystem", "localService", or "networkService".'
  Arguments = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  desktop6:Dependencies?
  desktop6:TriggerEvents?

</desktop6:Service>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the service. | A value. <!-- TODO: Add data type for desktop6:ST_ServiceName --> | Yes |  |
| **StartupType** | The startup type for the service. | A string that can have one of the following values: *auto*, *manual*, *disabled*. | Yes |  |
| **StartAccount** | The type of account in which to run the service. | A string that can have one of the following values: *localSystem*, *localService*, *networkService*. | Yes |  |
| **Arguments** | Optional arguments to pass to the service. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop6:Dependencies](element-desktop6-dependencies.md) | Specifies one or more dependent services for the current service. |
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Describes one or more trigger events for the current service. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop6:Extension](element-desktop6-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Examples

<!-- Author content goes here -->
