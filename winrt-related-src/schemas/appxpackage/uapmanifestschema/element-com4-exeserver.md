---
title: com4:ExeServer
description: Registers an ExeServer with one or many class registrations (com4:ExeServer).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com4:ExeServer]
---

# com4:ExeServer

Registers an ExeServer with one or many class registrations.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ExeServer>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com4:ExeServer>`**

## Syntax

```xml
<com4:ExeServer
  Executable = 'A required string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  Arguments = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  LaunchAndActivationPermission = 'An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).' >

  <!-- Child elements -->
  com4:Class{0,10000}
  com4:ClassReference{0,10000}

</com4:ExeServer>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Executable** | A path relative to the package root and must reference a file in the package. This specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
| **Arguments** | The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **DisplayName** | DisplayName is a localizable string corresponding to the default AppID key value. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com4:Class](element-com4-exeserver-class.md) | Defines an ExeServer class registration. |
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
