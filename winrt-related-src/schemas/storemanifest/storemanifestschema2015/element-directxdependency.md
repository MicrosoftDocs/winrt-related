---
Description: Identifies the minimum DirectX level that a device must support in order for your package to run properly.
Search.Product: eADQiWindows 10XVcnh
title: DirectXDependency
ms.assetid: 6034e4ef-8a4d-4cdd-8e18-df026a35f4e7
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
---

# DirectXDependency


Identifies the minimum DirectX level that a device must support in order for your package to run properly.

## Element hierarchy

<dl>
<dt><a href="element-storemanifest.md">&lt;StoreManifest&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;DirectXDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DirectXDependency Name = "D3D11_HWFL_9_3" | "D3D11_HWFL_10_0" | "D3D11_HWFL_11_0" | "D3D12_HWFL_11_0" | "D3D12_HWFL_12_0" />
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
<td><strong>Name</strong></td>
<td><p>The minimum DirectX level that a device must support in order for your package to run properly. Used for applicability at deployment time. If the minimum DirectX level of the system is lower than Name, then the package is not considered applicable.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>D3D11_HWFL_9_3</li>
<li>D3D11_HWFL_10_0</li>
<li>D3D11_HWFL_11_0</li>
<li>D3D12_HWFL_11_0</li>
<li>D3D12_HWFL_12_0</li>
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
<td>[Dependencies](element-dependencies.md)</td>
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

 

 



