---
title: com4:ExeServer
description: Registers an ExeServer with one or many class registrations (com4:ExeServer).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ExeServer

Registers an ExeServer with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ExeServer\>**

## Syntax

```xml
<com4:ExeServer
  Executable = 'A string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  Arguments = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
  LaunchAndActivationPermission = 'A [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value.' />

<!-- Child elements -->
  Class {0, 1000}
  ClassReference {0, 1000}

</com4:ExeServer>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Executable** | A path relative to the package root and must reference a file in the package. This specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | A string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. | Yes |  |
| **Arguments** |  The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **DisplayName** |  DisplayName is a localizable string corresponding to the default AppID key value. | A string with a value between 1 and 256 characters in length. | Yes |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | A [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com4-exeserver-class.md) | Defines an ExeServer class registration. |
| [ClassReference](element-com4-exeserver-classreference.md) | Specifies the class with which the registered ExeServer is associated and sets ExeServer-specific registration details. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
