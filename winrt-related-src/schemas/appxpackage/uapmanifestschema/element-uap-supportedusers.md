---
description: Indicates whether or not the package is multi-user aware.
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportedUsers (Windows 10)
ms.assetid: 5be5aec1-f253-4e1f-b386-8e9ae815a4e9
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:SupportedUsers (Windows 10)

Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:SupportedUsers\>**

## Syntax

```xml
<uap:SupportedUsers>
  A string that can have one of the following values: "single" or "multiple".
</uap:SupportedUsers>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Examples

```xml
<Properties>
    <uap:SupportedUsers>single</uap:SupportedUsers>
</Properties>
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
