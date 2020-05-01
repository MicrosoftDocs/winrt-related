---

title: uap5:MixedRealityModel
description: An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:MixedRealityModel

## Description
An element used to define a 3D model as the default representation of an app. When launched from a virtual or mixed reality device, this model will represent the app in the virtual setting.

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
<dd><b>&lt;uap5:MixedRealityModel&gt;</b></dd>
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
<uap5:MixedRealityModel Path =  A string between 1 and 256 characters in length that ends with ".glb" and cannot contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both. >

<!-- Child elements -->
uap6:SpatialBoundingBox?
</uap5:MixedRealityModel>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Path | The path to the 3D asset to be used. | A string between 1 and 256 characters in length that ends with ".glb" and cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. In this string, the / and \ characters cannot be the first or last characters. Also, the string can contain / or \ but not both. | Yes |

### Child Elements
| Child Element | Description |
|---------------|-------------|
| [SpatialBoundingBox](element-uap6-spatialboundingbox.md) | Used to define the center point and the extents for a bounding volume. |


## Requirements
|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
