---
title: uap15:DependencyTarget
description: Allows a main package manifest to specify whether the package is a valid target for dynamic dependencies.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, uap15:Package, uap15:Properties, uap15:DependencyTarget]
---

# uap15:DependencyTarget

Allows a main package manifest to specify whether the package is a valid target for [dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Properties>`](element-f-properties.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap15:DependencyTarget>`**  

## Syntax

```xml
<uap15:DependencyTarget>
    <!-- TODO: Add value description -->
</uap15:DependencyTarget>
```

## Value

<!-- TODO: Add value description -->

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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/15` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

For more information on dynamic dependencies, see [Use the dynamic dependency API to reference MSIX packages at run time](/windows/apps/desktop/modernize/framework-packages/use-the-dynamic-dependency-api).

## Examples

<!-- Author content goes here -->

## See also
[App capability declarations](/windows/uwp/packaging/app-capability-declarations)
[MSIX framework packages and dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview)
