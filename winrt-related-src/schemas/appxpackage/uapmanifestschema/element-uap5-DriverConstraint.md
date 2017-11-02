---
Description: Specifies the details of a driver paired with a UWP app.
title: uap5:DriverConstraint
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 10/10/17
---

# uap5:DriverConstraint
Specifies the details of a driver paired with a UWP app.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-DriverDependency.md">&lt;uap5:DriverDependency&gt;</a></dt>
<dd><b>&lt;uap5:DriverConstraint&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap5:DriverConstraint Name        = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. 
                       MinVersion? = A version string in quad notation, "Major.Minor.Build.Revision".
                       MinDate?    = The date in the form: YYYY-MM-DD  />
```

## Attributes and Elements
### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the driver in the form: &lt;Provider&gt;_&lt;Filename&gt;.INF. Use Family ID from `InfVerif.exe /info`. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| MinVersion | The version of the driver package. | A version string in quad notation, "Major.Minor.Build.Revision". | No |
| MinDate | The date of the driver package. | The date in the form: YYYY-MM-DD | No |

### Child Elements
None

## Examples
See [Pairing a driver with a Universal Windows Platform (UWP) app](/windows-hardware/drivers/install/pairing-app-and-driver-versions) for more information.

This example shows multiple `DriverDependency` and `DriverConstraint` elements paired with a UWP app.

```xml
<Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" MinVersion="10.0.0.0" MaxVersionTested="10.0.10586.0"/>
    <PackageDependency Name="Microsoft.VCLibs" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" MinVersion="1.0.0.0" MaxMajorVersionTested="5"/>
        
        <DriverDependency>
            <DriverConstraint Name="Microsoft_HoloLens.INF" MinVersion="1.0.0.0" MinDate="2017-05-20"/>
            <DriverConstraint Name="Microsoft_HoloLensCamera.INF" MinVersion="1.0.0.0" MinDate="2017-05-10"/>
        </DriverDependency>
        
        <DriverDependency>
            <DriverConstraint Name="Acer_HMDDevice.INF" MinDate="2017-05-10"/>
        <DriverDependency>
</Dependencies>

```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>

 

 



