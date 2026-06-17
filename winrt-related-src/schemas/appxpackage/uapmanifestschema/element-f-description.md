---
title: Description
description: A friendly description that can be displayed to users (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Properties, Description]
---

# Description

A friendly description that can be displayed to users.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Description>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Description>
      <!-- TODO: Add value description -->
  </Description>
</Package>
```

## Value

<!-- TODO: Add value description -->

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Defines additional metadata about the package including attributes that describe how the package appears to users. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-f-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

This string is localizable.

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Examples

<!-- Author content goes here -->
