---
Description: Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.
Search.Product: eADQiWindows 10XVcnh
title: Resource
ms.assetid: 445e7de7-e778-4666-b099-3d7f6f0125c7
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 10/26/2017
---
<link rel="stylesheet" href="https://az835927.vo.msecnd.net/sites/uwp/Resources/css/custom.css">

# Resource

Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.

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

```
<Resource Language?           = a valid BCP-47 language tag (such as "en", or "en-us")
          uap:Scale?          = "80" | "100" | "120" | "125" | "140" | "150" | "160" | "175" | "180" | "200" | "225" | "250" | "300" | "350" | "400" | "450"
          uap:DXFeatureLevel? = "dx9" | "dx10" | "dx11" | "dx12" />
```

See [BCP-47 language tag](https://go.microsoft.com/fwlink/p/?linkid=227302).

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
<td><p>The language for the resource contained in the package. The syntax of this attribute is defined by the IETF's <a href="https://www.rfc-editor.org/rfc/bcp/bcp47.txt">BCP47: Tags for Identifying Languages</a> .</p></td>
<td>language</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap:DXFeatureLevel</strong></td>
<td><p>The DirectX <a href="https://msdn.microsoft.com/library/windows/desktop/ff476876#overview">feature level</a>  of the resource from the manifest's Resources\Resource field.</p></td>
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
<td><p>The <a href="https://msdn.microsoft.com/library/windows/apps/br226165"><strong>resolution scale</strong></a>  of the resource.</p></td>
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
<td><a href="element-resources.md">Resources</a> </td>
<td><p>Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package.</p></td>
</tr>
</tbody>
</table>

## Remarks

If you have string/image/file resources in your Visual Studio project that have language qualifiers in their names (see [Tailor your resources for language, scale, high contrast, and other qualifiers](/windows/uwp/app-resources/tailor-resources-lang-scale-contrast?branch=live)), then you can put the following in your app package manifest source file (`Package.appxmanifest`).

```xml
  <Resources>
    <Resource Language="x-generate" />
  </Resources>
```

When Visual Studio builds your package manifest file (`AppxManifest.xml`), it expands that single `Resource` element into a union of all the language qualifiers that it finds in your project. For example, if you have string, image, and/or file resources whose folder or file names include "en-US", "ja-JP", and "fr-FR", then your built `AppxManifest.xml` file will contain the following.

```xml
  <Resources>
    <Resource Language="EN-US" />
    <Resource Language="JA-JP" />
    <Resource Language="FR-FR" />
  </Resources>
```

The first entry in the list is the default language for the app, which you can set in Visual Studio. With your solution open in Visual Studio, open `Package.appxmanifest` and, on the Application tab, set **Default language**.

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
