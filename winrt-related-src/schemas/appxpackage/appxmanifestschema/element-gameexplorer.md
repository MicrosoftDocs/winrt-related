---
Description: GameExplorer
MS-HAID: AppxManifestSchema.element\_GameExplorer
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: GameExplorer
ms.assetid: a5c4d94a-de5d-4f41-8d32-9233d9e4e7fa
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# GameExplorer


Declares a package extensibility point of type **windows.gameExplorer**.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;GameExplorer&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<GameExplorer GameDefinitionContainer = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *. />
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
<td><strong>GameDefinitionContainer</strong></td>
<td><p>The path to the file that contains the game definition.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, %, &quot;, |, ?, or *.</td>
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
<td>[Extension (in type: CT_PackageExtensions)](element-extension.md)</td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

**Note**  The **GameExplorer** extension is deprecated in Windows 8.1. To view the package manifest schema for Windows 8.1, see [Package manifest schema with Windows 8.1 minor extensions reference](https://msdn.microsoft.com/library/windows/apps/dn423313) and [Package manifest schema with Windows 8.1 feature extensions reference](https://msdn.microsoft.com/library/windows/apps/dn391692).

 

## Examples

```XML
<Extension Category="windows.gameExplorer">
      <GameExplorer GameDefinitionContainer="GDFExampleBinary.dll"/>      
</Extension>
```

## See also

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



