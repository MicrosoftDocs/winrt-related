---

title: uap6:SpatialBoundingBox
description: Used to define the center point and the extents for a bounding volume.

ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, extension 
---

# uap6:SpatialBoundingBox

## Description
Used to define the center point and the extents for a bounding volume.

## Element Hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-visualelements.md">&lt;uap:VisualElements&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-defaulttile.md">&lt;uap:DefaultTile&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-mixedrealitymodel.md">&lt;uap5:MixedRealityModel&gt;</a></dt>
<dd><b>&lt;uap6:SpatialBoundingBox&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<uap6:SpatialBoundingBox Center  = Vector coordinates in the form: X, Y, Z. Vectors values must be numeric and can contain decimal and negative values.
                         Extents = Either vector coordinates in the form: X, Y, Z (vectors values must be numeric and can contain decimal and negative values) or the string: "Auto". />
```

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Center | Vector coordinates of the center of the bounding box. | Vector coordinates in the form: X, Y, Z. Vectors values must be numeric and can contain decimal and negative values. | Yes |
| Extents | Either vector coordinates or "Auto" sizing extent of a the bounding box. | Either vector coordinates in the form: X, Y, Z (vectors values must be numeric and can contain decimal and negative values) or the string: "Auto". | Yes |

### Child Elements
None


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