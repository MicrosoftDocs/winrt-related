---
title: com4:ServiceServer
description: Registers a ServiceServer with one or many class registrations. (com4:ServiceServer)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com4:ServiceServer]
---

# com4:ServiceServer

Registers a ServiceServer with one or many class registrations.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ServiceServer>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ServiceServer>`**

## Syntax

```xml
<com4:ServiceServer
  ServiceName = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Arguments = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  LaunchAndActivationPermission = 'An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).' >

  <!-- Child elements -->
  com4:Class{0,10000}
  com4:ClassReference{0,10000}

</com4:ServiceServer>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServiceName** | The name of the Windows service that hosts the COM server. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Arguments** | The command-line parameters of the service. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **DisplayName** | A localizable string corresponding to the default AppID key value. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com4:Class](element-com4-exeserver-class.md) | <!-- TODO: Add description --> |
| [com4:ClassReference](element-com4-exeserver-classreference.md) | Specifies the class with which the registered ExeServer is associated and sets ExeServer-specific registration details. |

## Parent elements

| Parent element | Description |
|-|-|
| [com4:ComServer](element-com4-comserver.md) | Declares a package extension point of type windows.comServer. The comServer extension may include class registrations, including activation details for the servers that implement these classes, and ProgId and TreatAsClass registrations, which provide additional identifiers used to reference these classes at runtime. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
