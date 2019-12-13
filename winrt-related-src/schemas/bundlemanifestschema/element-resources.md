---
Description: Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains.
Search.Product: eADQiWindows 10XVcnh
title: Resources
ms.assetid: 45ce3dac-3888-452b-bc10-8775b158637a


keywords: windows 10, uwp, schema, bundle manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Resources

Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains.

## Element hierarchy

<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-packages.md">&lt;Packages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Resources&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Resources>

  <!-- Child elements -->
  Resource{1,200}

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
<td><a href="element-resource.md">Resource</a> </td>
<td><p>Declares language, resolution scale, and DirectX feature level for a resource in the package.</p></td>
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

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2013/bundle</p></td>
</tr>
</tbody>
</table>

 

 



