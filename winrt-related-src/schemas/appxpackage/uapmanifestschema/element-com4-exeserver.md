---
title: com4:ExeServer
description: Registers an ExeServer with one or many class registrations (com4:ExeServer).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ExeServer



## Description

Registers an ExeServer with one or many class registrations.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:ExeServer&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:ExeServer     Executable = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.
    Arguments = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    LaunchAndActivationPermission = [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).
>
<!-- Child elements -->
  Class {0, 1000}
  ClassReference {0, 1000}
</com4:ExeServer>
```

### Key

`{}`   specific range of occurrences


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Executable | A path relative to the package root and must reference a file in the package. This specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | One of the following values: A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| Arguments |  The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.| Yes |
| DisplayName |  DisplayName is a localizable string corresponding to the default AppID key value. | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| LaunchAndActivationPermission | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format).| Yes |


## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-exeserver-class.md) | Defines an ExeServer class registration. |
| [ClassReference](element-com4-exeserver-classreference.md) | Specifies the class with which the registered ExeServer is associated and sets ExeServer-specific registration details. |

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
