---
title: Dependencies
description: Declares other packages that a package depends on to complete its software (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Dependencies]
---

# Dependencies

Declares other packages that a package depends on to complete its software.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<Dependencies>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Dependencies>

    <!-- Child elements -->
    TargetDeviceFamily{1,128}
    PackageDependency{0,129}
    HostRuntimeDependency{0,129}
    PackageDependency{0,129}
    MainPackageDependencyChoice?
    MainPackageDependencyChoice2{0,1000}
    DriverDependency{0,1000}
    OSPackageDependency{0,1000}
    HostRuntimeDependency?

  </Dependencies>
</Package>
```

### Key

`?` optional (zero or one)
`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
|  | Identifies the device family that your package targets. For more info about device families, see [Programming with extension SDKs](/uwp/extension-sdks/device-families-overview). |  |  |  |
|  | Declares a dependency on another package that is marked as a framework package. |  |  |  |
|  | Declares publisher information for the app. |  |  |  |
|  | Declares other packages that a package depends on. This dependency can be specified as required for both install time and runtime or just install time but not runtime. |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
|  | <!-- TODO: Add description --> |  |  |  |
|  | Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load. |  |  |  |
|  | Defines a package dependency for a UWP app. |  |  |  |
|  | Defines a dependency on a host app for the current app. For more information, see [Create hosted apps](/windows/uwp/launch-resume/hosted-apps). |  |  |  |
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
| [TargetDeviceFamily](element-f-targetdevicefamily.md) | Identifies the device family that your package targets. For more info about device families, see [Programming with extension SDKs](/uwp/extension-sdks/device-families-overview). |
| [PackageDependency](element-f-packagedependency.md) | Declares a dependency on another package that is marked as a framework package. |
| [uap13:HostRuntimeDependency](element-uap13-hostruntimedependency.md) | Declares publisher information for the app. |
| [uap17:PackageDependency](element-uap17-packagedependency.md) | Declares other packages that a package depends on. This dependency can be specified as required for both install time and runtime or just install time but not runtime. |
| [uap5:DriverDependency](element-uap5-driverdependency.md) | Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load. |
| [uap7:OSPackageDependency](element-uap7-ospackagedependency.md) | Defines a package dependency for a UWP app. |
| [uap10:HostRuntimeDependency](element-uap10-hostruntimedependency.md) | Defines a dependency on a host app for the current app. For more information, see [Create hosted apps](/windows/uwp/launch-resume/hosted-apps). |

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

Dependencies must be explicitly defined. If a dependency cannot be resolved, deployment of the package fails. By default, a package cannot take a dependency on another package if the dependency package is not declared to be a framework or resource package. Set [Framework](element-f-framework.md) to **true** to declare a framework package and [ResourcePackage](element-f-resourcepackage.md) to **true** to declare a resource package.

The total count of `uap7:OSPackageDependency` and `uap10:HostRuntimeDependency` elements must not exceed 128.

## Examples

```XML
<Dependencies>
  <PackageDependency Name="Microsoft.WinJS.1.0"
    Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
    MinVersion="1.0.0.0"/>    
</Dependencies>
```
