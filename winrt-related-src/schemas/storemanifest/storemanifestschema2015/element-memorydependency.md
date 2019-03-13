---
Description: Identifies the minimum memory that a device must have in order for your package to run properly.
Search.Product: eADQiWindows 10XVcnh
title: MemoryDependency
ms.assetid: f575ea28-e218-4061-b3b8-6cc0cd4d9230
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
---

# MemoryDependency


Identifies the minimum memory that a device must have in order for your package to run properly.

For desktop devices, the value indicates the requirement for installed memory. Available memory is not considered.

For mobile devices, the value indicates the requirements for available memory. The equivalent requirements for installed memory on mobile devices are as follows:

-   300MB = device must have at least 1 GB of installed memory
-   750MB = device must have at least 2 GB of installed memory
-   1000MB = device must have at least 3 GB of installed memory
-   2000MB = device must have at least 4 GB of installed memory

For example, if you specify that your UWP app requires 300 MB to run properly, it will only be able to be installed on mobile devices with &gt;1 GB of RAM or on desktop devices with &gt;300 MB of RAM.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;MemoryDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<MemoryDependency MinForeground = "300MB" | "750MB" | "1000MB" | "2000MB" />
```

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MinForeground</strong></td>
<td><p>The minimum memory that a device must have in order for your package to run properly. Used for applicability at deployment time. If the minimum memory of the system is lower than MinForeground, then the package is not considered applicable.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>300MB</li>
<li>750MB</li>
<li>1000MB</li>
<li>2000MB</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

None.

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
<td><a href="element-dependencies.md">Dependencies</a> </td>
<td><p>Declares requirements that a package depends on to be applicable to a device.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2015/StoreManifest</p></td>
</tr>
</tbody>
</table>

 

 



