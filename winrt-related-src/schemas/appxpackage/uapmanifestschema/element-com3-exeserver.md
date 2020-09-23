---
title: com3:ExeServer
description: Registers an ExeServer with one or many class registrations.
ms.date: 04/20/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com3:ExeServer

## Description

Registers an ExeServer with one or many class registrations.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com2-comserver.md">&lt;com2:ComServer&gt;</a></dt>
<dd><b>&lt;com3:ExeServer&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com3:ExeServer
    Executable = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *.
    Arguments? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    DisplayName? = A string between 1 and 256 characters in length. This string is localizable.
    LaunchAndActivationPermission? = [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). >

  <!-- Child elements -->
  Class{1,10000}
</com3:ExeServer>
```

## Key
`?`    optional (zero or one)  
`{}`   specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Executable | A path relative to the package root and must reference a file in the package. This specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. The .exe extension is case sensitive, it must be lowercase. | Yes |
| Arguments | The arguments of the [LocalServer32](/windows/win32/com/localserver32) key. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |
| DisplayName | DisplayName is a localizable string corresponding to the default AppID key value. | A string between 1 and 256 characters in length. | No |
| LaunchAndActivationPermission | An [SDDL string](/windows/win32/secauthz/security-descriptor-string-format) that corresponds to the LaunchPermission value of the AppID key. | [SDDL string](/windows/win32/secauthz/security-descriptor-string-format). | No |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Class](element-com-exeserver-class.md) | Defines an ExeServer class registration. |


## Remarks
An **ExeServer** can have one or more class registrations. Multiple class registrations should share an **ExeServer** if their [LocalServer32 keys](/windows/win32/com/localserver32) match and they have the same [AppID](/windows/win32/com/appid) (or if they don't have an AppID), unless they need to be registered under different Applications/Application manifest elements.

**ExeServer** registrations correspond to [LocalServer32 keys](/windows/win32/com/localserver32) and their associated [AppID key](/windows/win32/com/appid-key).

The **Executable** and **Arguments** attributes correspond to the default value of the [LocalServer32](/windows/win32/com/localserver32) key.

## Requirements
|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/3` |