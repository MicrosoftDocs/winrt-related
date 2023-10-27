---
title: com3:ExeServer
description: Registers an ExeServer with one or many class registrations (com3:ExeServer).
ms.date: 04/20/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com3:ExeServer

Registers an **ExeServer** with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com2:Extension\>](element-com2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com2:ComServer\>](element-com2-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com3:ExeServer\>**

## Syntax

```xml
<com3:ExeServer
    Executable = 'A string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
    Arguments = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
    LaunchAndActivationPermission = 'An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value.' >

  <!-- Child elements -->
  Class{1,10000}

</com3:ExeServer>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Executable** | A path relative to the package root and must reference a file in the package. This specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | A string with a value between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: `<`, `>`, `:`, `"`, `|`, `?`, or `*`. The `.exe` extension is case sensitive and must be lowercase. | Yes |  |
| **Arguments** | The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **DisplayName** | DisplayName is a localizable string corresponding to the default AppID key value. | A string with a value between 1 and 256 characters in length. | No |  |
| **LaunchAndActivationPermission** | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) value. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com-exeserver-class.md) | Defines an ExeServer class registration. |

### Parent elements

| Parent element | Description |
|-|-|
| [com2:ComServer](element-com2-comserver.md) | Declares a package extension point of type **windows.comServer**. The **comServer** extension may include the following types of registrations: *ServiceServer*, *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*. |

## Remarks

An **ExeServer** can have one or more class registrations. Multiple class registrations should share an **ExeServer** if their [LocalServer32 keys](/windows/win32/com/localserver32) match and they have the same [AppID](/windows/win32/com/appid) (or if they don't have an AppID), unless they need to be registered under different Applications/Application manifest elements.

**ExeServer** registrations correspond to [LocalServer32 keys](/windows/win32/com/localserver32) and their associated [AppID key](/windows/win32/com/appid-key).

The **Executable** and **Arguments** attributes correspond to the default value of the [LocalServer32](/windows/win32/com/localserver32) key.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |
| Minimum OS Version | Windows 10 version 2004 (Build 19041) |
