---
title: uap5:DriverDependency
description: Contains the driver constraint information for a UWP app.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Extensions, uap5:Package, uap5:Dependencies, uap5:DriverDependency]
keywords: windows 10, uwp, schema, package manifest, driver dependency
---

# uap5:DriverDependency

Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:DriverDependency>`**

## Syntax

```xml
<uap5:DriverDependency>

  <!-- Child elements -->
  uap5:DriverConstraint{0,1000}

</uap5:DriverDependency>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap5:DriverConstraint](element-uap5-driverconstraint.md) | Specifies the details of a driver paired with a UWP app. |

## Parent elements

| Parent element | Description |
|-|-|
| [Dependencies](element-f-dependencies.md) | Declares other packages that a package depends on to complete its software. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

If you are pairing a driver with a UWP app, all of the listed `DriverDependency` elements must be met for the app to load. For a `DriverDependency` to be met, at least one of its [`DriverConstraint`](element-uap5-DriverConstraint.md) elements must be met.

See [Pairing a driver with a Universal Windows Platform (UWP) app](/windows-hardware/drivers/install/pairing-app-and-driver-versions) for more information.

## Examples

See [uap5:DriverConstraint](element-uap5-DriverConstraint.md) for an example.
