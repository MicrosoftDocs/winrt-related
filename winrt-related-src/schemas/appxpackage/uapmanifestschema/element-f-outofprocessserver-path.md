---
title: Path (in OutOfProcessServer)
description: The path to the executable (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, OutOfProcessServer, Path]
---

# Path (in OutOfProcessServer)

The path to the executable.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<OutOfProcessServer>`](element-f-outofprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Path>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Path>
      <!-- TODO: Add value description -->
  </Path>
</Package>
```

## Value

<!-- TODO: Add value description -->

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |  |  |  |
|  | Value |  |  |  |
|  | -- |  |  |  |
|  | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |  |  |  |
|  | <!-- TODO: Add minimum OS version --> |  |  |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [OutOfProcessServer](element-f-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->

## See also
The following elements have the same name as this one, but different content or attributes:

- **[Path (type: ST_FileName)](element-f-outofprocessserver-path.md)**
