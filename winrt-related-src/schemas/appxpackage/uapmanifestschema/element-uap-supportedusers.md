---
title: uap:SupportedUsers
description: Indicates whether or not the package is multi-user aware.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap:Package, uap:Properties, uap:SupportedUsers]
---

# uap:SupportedUsers

Indicates whether or not the package is multi-user aware. This setting is used at install time to determine whether the package can be installed on the system.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:SupportedUsers>`**  

## Syntax

```xml
<uap:SupportedUsers>
    <!-- TODO: Add value description -->
</uap:SupportedUsers>
```

## Value

A string that can have one of the following values: "single" or "multiple".

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.


## Examples

```xml
<Properties>
    <uap:SupportedUsers>single</uap:SupportedUsers>
</Properties>
```
