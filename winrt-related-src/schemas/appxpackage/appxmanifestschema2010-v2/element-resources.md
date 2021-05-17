---
description: Declares languages for the resources that the package contains.
Search.Product: eADQiWindows 10XVcnh
title: Resources (Windows 8.1 extensions schema)
ms.assetid: 45ce3dac-3888-452b-bc10-8775b158637a


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Resources (extensions schema for Windows 8.1)

Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Resources&gt;</b></dd>
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
<td><p>Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
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

 

## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



