---
title: com3:ExeServer
description: Registers an ExeServer with one or many class registrations (com3:ExeServer).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com3:Extension, com3:ComServer, com3:ExeServer]
---

# com3:ExeServer

Registers an **ExeServer** with one or many class registrations.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com3:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com3:ComServer>`](element-com-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com3:ExeServer>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com3:Extension>`](element-com-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com3:ComServer>`](element-com-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com3:ExeServer>`**  


## Syntax

```xml
<com3:ExeServer
  Executable = 'A required string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.'
  Arguments = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  LaunchAndActivationPermission = 'An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).' >

  <!-- Child elements -->
  com3:Class{1,10000}

</com3:ExeServer>
```

### Key

`{}` specific range of occurrences


## Attributes
| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Executable** | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. | Yes |  |
|**Arguments**| The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. |An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.|No||
|**DisplayName**| DisplayName is a localizable string corresponding to the default AppID key value. |An optional string between 1 and 256 characters in length. This string is localizable.|No||
|**LaunchAndActivationPermission**| An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. |An optional [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).|No||

## Child elements
| Child element | Description |
|-|-|
| [com:Class](element-com-exeserver-class.md) | Defines an ExeServer class registration. |

## Parent elements

| Parent element | Description |
|-|-|
| [com:ComServer](element-com-comserver.md) | Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: *ExeServer*, *SurrogateServer*, *ProgId*, or *TreatAsClass*. |


## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |
| **Minimum OS Version** | Windows 10 version 2004 (Build 19041) |


## Remarks

An **ExeServer** can have one or more class registrations. Multiple class registrations should share an **ExeServer** if their [LocalServer32 keys](/windows/win32/com/localserver32) match and they have the same [AppID](/windows/win32/com/appid) (or if they don't have an AppID), unless they need to be registered under different Applications/Application manifest elements.

**ExeServer** registrations correspond to [LocalServer32 keys](/windows/win32/com/localserver32) and their associated [AppID key](/windows/win32/com/appid-key).

The **Executable** and **Arguments** attributes correspond to the default value of the [LocalServer32](/windows/win32/com/localserver32) key.

## Examples

<!-- Author content goes here -->
