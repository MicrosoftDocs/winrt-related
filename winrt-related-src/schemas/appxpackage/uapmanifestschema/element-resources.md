---
Description: Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains.
Search.Product: eADQiWindows 10XVcnh
title: Resources
ms.assetid: 45ce3dac-3888-452b-bc10-8775b158637a
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 10/26/2017
---

# Resources

Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains. For details and examples, see [Resource](element-resource.md).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Resources&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Resources Default = Boolean>

  <!-- Child elements -->
  Resource{0,200}

</Resources>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Default | The name of the capability. | Boolean | No |

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
<td><p>Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.</p><p>Note: Beginning in Windows 10, version 1803, the Resource element can be omitted. </p></td>
</tr>
</tbody>
</table>

### Parent elements

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
The **Default** attribute is not 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>
