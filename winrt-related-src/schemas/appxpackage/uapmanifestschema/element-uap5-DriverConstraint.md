---
title: uap5:DriverConstraint
description: Specifies the details of a driver paired with a UWP app.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Extensions, uap5:Package, uap5:Dependencies, uap5:DriverDependency, uap5:DriverConstraint]
keywords: windows 10, uwp, schema, package manifest
---

# uap5:DriverConstraint

Specifies the details of a driver paired with a UWP app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Dependencies>`](element-f-dependencies.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:DriverDependency>`](element-uap5-driverdependency.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:DriverConstraint>`**

## Syntax

```xml
<uap5:DriverConstraint
  Name = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  MinVersion = 'An optional value. <!-- TODO: Add description for t:ST_VersionQuadNoneZero -->'
  MinDate = 'An optional value. <!-- TODO: Add description for t:ST_Date -->' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the driver in the form: \<Provider\>-\<Filename\>.INF. Use Family ID from `InfVerif.exe /info`. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **MinVersion** | The version of the driver package. | An optional value. <!-- TODO: Add data type for t:ST_VersionQuadNoneZero --> | No |  |
| **MinDate** | The date of the driver package. | An optional value. <!-- TODO: Add data type for t:ST_Date --> | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:DriverDependency](element-uap5-driverdependency.md) | Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

See [Pairing a driver with a Universal Windows Platform (UWP) app](/windows-hardware/drivers/install/pairing-app-and-driver-versions) for more information.

This example shows multiple `DriverDependency` and `DriverConstraint` elements paired with a UWP app.

```xml
<Dependencies>
    <TargetDeviceFamily
        Name="Windows.Universal"
        MinVersion="10.0.0.0"
        MaxVersionTested="10.0.10586.0"/>
    <PackageDependency
        Name="Microsoft.VCLibs"
        Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
        MinVersion="1.0.0.0"
        MaxMajorVersionTested="5"/>
        
    <uap5:DriverDependency>
        <uap5:DriverConstraint
            Name="Microsoft-HoloLens.INF"
            MinVersion="1.0.0.0"
            MinDate="2017-05-20"/>
        <uap5:DriverConstraint
            Name="Microsoft-HoloLensCamera.INF"
            MinVersion="1.0.0.0"
            MinDate="2017-05-10"/>
    </uap5:DriverDependency>
        
    <uap5:DriverDependency>
        <uap5:DriverConstraint
            Name="Acer-HMDDevice.INF"
            MinDate="2017-05-10"/>
    </uap5:DriverDependency>
</Dependencies>

```
