---
description: Declares requirements that a package depends on to be applicable to a device
Search.Product: eADQiWindows 10XVcnh
title: Dependencies
ms.assetid: a1e745c9-a804-42cf-a107-7fb860cc8289


keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
---

# Dependencies


Declares requirements that a package depends on to be applicable to a device.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd><b>&lt;Dependencies&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Dependencies>

  <!-- Child elements -->
  ( TargetDeviceFamily*
  | MemoryDependency?
  | DirectXDependency?
  )+

</Dependencies>
```

### Key

`?`   optional (zero or one)
`*`   optional (zero or more)
`+`   required (one or more)

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
<td><a href="element-directxdependency.md">DirectXDependency</a> </td>
<td><p>Identifies the minimum DirectX level that a device must support in order for your package to run properly.</p></td>
</tr>
<tr class="even">
<td><a href="element-memorydependency.md">MemoryDependency</a> </td>
<td><p>Identifies the minimum memory that a device must have in order for your package to run properly.</p>
<p>For desktop devices, the value indicates the requirement for installed memory. Available memory is not considered.</p>
<p>For mobile devices, the value indicates the requirements for available memory. The equivalent requirements for installed memory on mobile devices are as follows:</p>
<ul>
<li>300MB = device must have at least 1 GB of installed memory</li>
<li>750MB = device must have at least 2 GB of installed memory</li>
<li>1000MB = device must have at least 3 GB of installed memory</li>
<li>2000MB = device must have at least 4 GB of installed memory</li>
</ul>
<p>For example, if you specify that your UWP app requires 300 MB to run properly, it will only be able to be installed on mobile devices with &gt;1 GB of RAM or on desktop devices with &gt;300 MB of RAM.</p></td>
</tr>
<tr class="odd">
<td><a href="element-targetdevicefamily.md">TargetDeviceFamily</a> </td>
<td><p>Identifies the device family that your package targets.</p>
<div class="alert">
<strong>Important</strong>  In most cases, you should simply specify your device families in the [<strong>TargetDeviceFamily</strong>](../../appxpackage/uapmanifestschema/element-targetdevicefamily.md) element of your AppxManifest. Values here should only be used if you need to override that info (using a subset of the values provided there).
</div>
<div>
 
</div></td>
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
<td><a href="element-storemanifest.md">StoreManifest</a> </td>
<td><p>Root node for the StoreManifest schema (for Windows 10).</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2015/StoreManifest` |

 

 
