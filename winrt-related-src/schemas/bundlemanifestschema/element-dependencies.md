---
description: Declares dependencies that will be installed if required. (descendant of Packages).
Search.Product: eADQiWindows 10XVcnh
title: Dependencies (Bundle schema, descendant of Packages)
ms.assetid: 45ce3dac-3888-452b-bc10-8775b158637a


keywords: windows 10, uwp, schema, bundle manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Dependencies (Bundle schema, descendant of Packages)

Declares dependencies that will be installed if required.

## Element hierarchy

<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-packages.md">&lt;Packages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Dependencies&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Dependencies>

  <!-- Child elements -->
  TargetDeviceFamily{0,128}

</Resources>
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
<td><a href="element-targetdevicefamily.md">TargetDeviceFamily</a> </td>
<td><p>Identifies the device family that a package targets. For more info about device families, see [Programming with extension SDKs](../../../extension-sdks/device-families-overview.md).</p></td>
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
<td><p>Defines one of the app packages or resource packages in the bundle.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2018/bundle` |

 

 



