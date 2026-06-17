---
title: Resources
description: Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Resources]
---

# Resources

Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains. For details and examples, see [Resource](element-f-resource.md).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Resources>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Resources>

    <!-- Child elements -->
    Resource{0,200}

  </Resources>
</Package>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package. |  |  |  |
|  | Description |  |  |  |
|  | - |  |  |  |
|  | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

| Child element | Description |
|-|-|
| [Resource](element-f-resource.md) | Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package. |

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

> [!NOTE]
> Beginning in Windows 10, version 1803, the Resource element can be omitted.

## Examples

<!-- Author content goes here -->
