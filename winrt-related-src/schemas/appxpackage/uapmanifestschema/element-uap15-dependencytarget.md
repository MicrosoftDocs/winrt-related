---
description: Allows a main package manifest to specify whether the package is a valid target for dynamic dependencies.
title: uap15:DependencyTarget
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 09/22/2022
---

# uap15:DependencyTarget

Allows a main package manifest to specify whether the package is a valid target for [dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview).

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<uap15:DependencyTarget\>**

## Syntax

```xml
<uap15:DependencyTarget>
  A boolean value.
</uap15:DependencyTarget>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| Properties | Defines additional metadata about the package including attributes that describe how the package appears to users. |

## Remarks

For more information on dynamic dependencies, see [Use the dynamic dependency API to reference MSIX packages at run time](/windows/apps/desktop/modernize/framework-packages/use-the-dynamic-dependency-api).



## See also

[App capability declarations](/windows/uwp/packaging/app-capability-declarations)
[MSIX framework packages and dynamic dependencies](/windows/apps/desktop/modernize/framework-packages/framework-packages-overview)

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/15` |
