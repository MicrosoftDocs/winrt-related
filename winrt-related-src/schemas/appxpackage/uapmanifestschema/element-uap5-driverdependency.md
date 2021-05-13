---
description: Contains the driver constraint information for a UWP app.
title: uap5:DriverDependency


keywords: windows 10, uwp, schema, package manifest, driver dependency


ms.topic: reference
ms.date: 10/10/2017
---

# uap5:DriverDependency
Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;uap5:DriverDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap5:DriverDependency>
  <!-- Child elements -->
  uap5:DriverConstraint{1,1000}
</uap5:DriverDependency>
```

## Attributes and Elements
### Attributes
None

### Child Elements
| Child Element | Description |
|---------------|-------------|
| [DriverConstraint](element-uap5-DriverConstraint.md) | Specifies the details of a driver paired with a UWP app. |

## Remarks
If you are pairing a driver with a UWP app, all of the listed `DriverDependency` elements must be met for the app to load. For a `DriverDependency` to be met, at least one of its [`DriverConstraint`](element-uap5-DriverConstraint.md) elements must be met. 

See [Pairing a driver with a Universal Windows Platform (UWP) app](/windows-hardware/drivers/install/pairing-app-and-driver-versions) for more information.

## Examples
See [uap5:DriverConstraint](element-uap5-DriverConstraint.md) for an example. 

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
