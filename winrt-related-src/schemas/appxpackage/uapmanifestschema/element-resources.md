---
description: Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains.
Search.Product: eADQiWindows 10XVcnh
title: Resources (Windows 10 package schema)
ms.assetid: 45ce3dac-3888-452b-bc10-8775b158637a
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/26/2017
---

# Resources (package schema for Windows 10)

Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains. For details and examples, see [Resource](element-resource.md).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Resources\>**

## Syntax

```xml
<Resources>

  <!-- Child elements -->
  Resource{0,200}

</Resources>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Resource](element-resource.md) | Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package. |

> [!NOTE]
> Beginning in Windows 10, version 1803, the Resource element can be omitted.

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
