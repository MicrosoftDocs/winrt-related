---
description: Declares other packages that a package depends on to complete its software.
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

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Dependencies&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Dependencies>

  <!-- Child elements -->
  TargetDeviceFamily{1,128},
  PackageDependency{0,128},
  uap3:MainPackageDependency{0,1},
  uap5:DriverDependency{0,1000}
  uap7:OSPackageDependency{0,1000}
  uap10:HostRuntimeDependency{0,1000}

</Dependencies>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

None.

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-packagedependency.md">PackageDependency</a> </td>
<td><p>Declares a dependency on another package that is marked as a framework package.</p></td>
</tr>
<tr class="even">
<td><a href="element-targetdevicefamily.md">TargetDeviceFamily</a> </td>
<td><p>Identifies the device family that your package targets. For more info about device families, see <a href="/windows/uwp/get-started/universal-application-platform-guide">Guide to UWP apps</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap3-mainpackagedependency-manual.md">uap3:MainPackageDependency</a> </td>
<td><p>Specifies the main app package to which this supplemental package applies.
</p></td>
</tr>
<tr class="even">
<td><a href="element-uap5-driverdependency.md">uap5:DriverDependency</a> </td>
<td><p>Contains the driver constraint information for a UWP app. If DriverDependency is used, the specified driver must be present for the app to load.
</p></td>
</tr>
<tr class="even">
<td><a href="element-uap7-ospackagedependency.md">uap7:OSPackageDependency</a> </td>
<td><p>CDefines a package dependency for a UWP app.
</p></td>
</tr>
<tr class="even">
<td><a href="element-uap10-hostruntimedependency.md">uap10:HostRuntimeDependency</a> </td>
<td><p>Defines a dependency on a host app package for the current app package.
</p></td>
</tr>
</tbody>
</table>


 

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Dependencies must be explicitly defined. If a dependency cannot be resolved, deployment of the package fails. By default, a package cannot take a dependency on another package if the dependency package is not declared to be a framework or resource package. Set [**Framework**](element-framework.md) to **true** to declare a framework package and [**ResourcePackage**](element-resourcepackage.md) to **true** to declare a resource package.

## Examples

```XML
<Dependencies>
    <PackageDependency Name="Microsoft.WinJS.1.0"
      Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
      MinVersion="1.0.0.0"/>    
</Dependencies>
```

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 
