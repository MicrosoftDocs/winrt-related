---
description: Declares other packages that a package depends on to complete its software (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Dependencies (Windows 10)
ms.assetid: a1e745c9-a804-42cf-a107-7fb860cc8289
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Dependencies (Windows 10)

Declares other packages that a package depends on to complete its software.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<Dependencies\>**

## Syntax

```xml
<Dependencies>

  <!-- Child elements -->
  TargetDeviceFamily{1,128},
  PackageDependency{0,128},
  uap3:MainPackageDependency{0,1},
  uap5:DriverDependency{0,1000}
  uap7:OSPackageDependency{0,1000}
  uap10:HostRuntimeDependency{0,128}

</Dependencies>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [PackageDependency](element-packagedependency.md) | Declares a dependency on another package that is marked as a framework package. |
| [TargetDeviceFamily](element-targetdevicefamily.md) | Identifies the device family that your package targets. For more info about device families, see the [Guide to UWP apps](/windows/uwp/get-started/universal-application-platform-guide). |
| [uap3:MainPackageDependency](element-uap3-mainpackagedependency-manual.md) | Specifies the main app package to which this supplemental package applies. |
| [uap5:DriverDependency](element-uap5-driverdependency.md) | Contains the driver constraint information for a UWP app. If DriverDependency is used, the specified driver must be present for the app to load. |
| [uap7:OSPackageDependency](element-uap7-ospackagedependency.md) | Defines a package dependency for a UWP app. |
| [uap10:HostRuntimeDependency](element-uap10-hostruntimedependency.md) | Defines a dependency on a host app package for the current app package. |
| [win32dependencies:ExternalDependency](element-win32dependencies-externaldependency.md) | Specifies an external dependency that is not included in the MSIX but will be chain installed as part of the app installation. |

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Remarks

Dependencies must be explicitly defined. If a dependency cannot be resolved, deployment of the package fails. By default, a package cannot take a dependency on another package if the dependency package is not declared to be a framework or resource package. Set [Framework](element-framework.md) to **true** to declare a framework package and [ResourcePackage](element-resourcepackage.md) to **true** to declare a resource package.

The total count of `uap7:OSPackageDependency` and `uap10:HostRuntimeDependency` elements must not exceed 128.

## Examples

```XML
<Dependencies>
  <PackageDependency Name="Microsoft.WinJS.1.0"
    Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
    MinVersion="1.0.0.0"/>    
</Dependencies>
```

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
