---
ms.assetid: 00fa8e21-6613-4eea-a5ff-a4dc4741d5bb
title: com:ExeServer
description: Registers an ExeServer with one or many class registrations (com:ExeServer).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:ExeServer

Registers an ExeServer with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComServer\>](element-com-comserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:ExeServer\>**

## Syntax

```xml
<com:ExeServer
    Executable = 'A string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
    Arguments = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
    LaunchAndActivationPermission = '[Optional SDDL string](/windows/win32/secauthz/security-descriptor-string-format).' >

  <!-- Child elements -->
  Class{1,10000}

</com:ExeServer>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required |
|-|-|-|-|
| **Executable** | A path relative to the package root and must reference a file in the package. This specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | A string with a value between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. | Yes |  |
| **Arguments** | The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **DisplayName** | DisplayName is a localizable string corresponding to the default AppID key value. | A string with a value between 1 and 256 characters in length. | No |  |
| **LaunchAndActivationPermission** | An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com-exeserver-class.md) | Defines an ExeServer class registration. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:ComServer](element-com-comserver.md) | Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*. |

## Remarks

An **ExeServer** can have one or more class registrations. Multiple class registrations should share an **ExeServer** if their [LocalServer32 keys](/windows/win32/com/localserver32) match and they have the same [AppID](/windows/win32/com/appid) (or if they don't have an AppID), unless they need to be registered under different Applications/Application manifest elements.

**ExeServer** registrations correspond to [LocalServer32 keys](/windows/win32/com/localserver32) and their associated [AppID key](/windows/win32/com/appid-key).

The **Executable** and **Arguments** attributes correspond to the default value of the [LocalServer32](/windows/win32/com/localserver32) key.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |