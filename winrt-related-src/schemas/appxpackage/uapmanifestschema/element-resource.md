---
Description: Resource (Windows 10)
MS-HAID: UapManifestSchema.element\_Resource
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Resource (Windows 10)
ms.assetid: 445e7de7-e778-4666-b099-3d7f6f0125c7
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# Resource (Windows 10)


Declares a language for the resource contained in the package. The scale and DirectX feature level attributes are common for all resources in the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-resources.md">&lt;Resources&gt;</a></dt>
<dd><b>&lt;Resource&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Resource Language?           = language
          uap:Scale?          = "100" | "120" | "125" | "140" | "150" | "160" | "180" | "200" | "225" | "250" | "300" | "400"
          uap:DXFeatureLevel? = "dx9" | "dx10" | "dx11" />
```

### Key

`?`   optional (zero or one)

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
<td><strong>Language</strong></td>
<td><p>The language for the resource contained in the package. The syntax of this attribute is defined by the IETF's [BCP47: Tags for Identifying Languages](http://www.rfc-editor.org/rfc/bcp/bcp47.txt).</p></td>
<td>language</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap:DXFeatureLevel</strong></td>
<td><p>The DirectX [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) of the resource from the manifest's Resources\Resource field.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>dx9</li>
<li>dx10</li>
<li>dx11</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap:Scale</strong></td>
<td><p>The [<strong>resolution scale</strong>](https://msdn.microsoft.com/library/windows/apps/br226165) of the resource.</p></td>
<td>&quot;100&quot; | &quot;120&quot; | &quot;125&quot; | &quot;140&quot; | &quot;150&quot; | &quot;160&quot; | &quot;180&quot; | &quot;200&quot; | &quot;225&quot; | &quot;250&quot; | &quot;300&quot; | &quot;400&quot;</td>
<td>No</td>
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
<td>[Resources](element-resources.md)</td>
<td><p>Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
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
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



