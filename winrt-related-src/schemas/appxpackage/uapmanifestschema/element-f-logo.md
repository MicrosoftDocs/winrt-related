---
title: Logo
description: A path to a file that contains an image (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Properties, Logo]
---

# Logo

A path to a file that contains an image.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Logo>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Logo>
      <!-- TODO: Add value description -->
  </Logo>
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

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

The logo image can be given as either a direct path to an image file or as a resource.By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

## Examples

<!-- Author content goes here -->
