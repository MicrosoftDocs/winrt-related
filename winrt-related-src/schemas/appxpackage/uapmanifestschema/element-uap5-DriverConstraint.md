---
description: Specifies the details of a driver paired with a UWP app.
title: uap5:DriverConstraint
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/10/2017
---

# uap5:DriverConstraint

Specifies the details of a driver paired with a UWP app.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Dependencies\>](element-dependencies.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:DriverDependency\>](element-uap5-driverdependency.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:DriverConstraint\>**

## Syntax

```xml
<uap5:DriverConstraint
    Name = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' 
    MinVersion = 'A version string in quad notation ("Major.Minor.Build.Revision"), where "Major" cannot be 0.'
    MinDate = 'A date value in the form: "YYYY-MM-DD".' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the driver in the form: \<Provider\>-\<Filename\>.INF. Use Family ID from `InfVerif.exe /info`. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **MinVersion** | The version of the driver package. | A version string in quad notation (`Major.Minor.Build.Revision`), where `Major` cannot be `0`. | No |  |
| **MinDate** | The date of the driver package. | A date value in the form: `YYYY-MM-DD`. | No |  |

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:DriverDependency](element-uap5-DriverDependency.md) | Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
