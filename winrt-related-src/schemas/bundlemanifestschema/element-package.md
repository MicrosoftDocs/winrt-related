---
Description: Defines one of the app packages or resource packages in the bundle.
Search.Product: eADQiWindows 10XVcnh
title: Package
ms.assetid: ea0f5af0-8191-4ce0-9594-c647f800bd53
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, bundle manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Package

Defines one of the app packages or resource packages in the bundle.

## Element hierarchy

<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-packages.md">&lt;Packages&gt;</a></dt>
<dd><b>&lt;Package&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Package Type?         = Specifies the package type as app or resource. : "resource"
         Version       = A version string in quad notation, "Major.Minor.Build.Revision".
         Architecture? = "x86" | "x64" | "arm" | "neutral" : "neutral"
         ResourceId?   = A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters.
         FileName      = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
         Offset        = unsignedLong
         Size          = unsignedLong >

  <!-- Child elements -->
  Resources

</Package>
```

### Key

`?`   optional (zero or one)
`:`   default value
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
<td><strong>Architecture</strong></td>
<td><p>Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>x86</li>
<li>x64</li>
<li>arm</li>
<li>neutral</li>
</ul></td>
<td>No</td>
<td>neutral</td>
</tr>
<tr class="even">
<td><strong>FileName</strong></td>
<td><p>Describes the file name of the package.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Offset</strong></td>
<td><p>Describes the offset in bytes into the bundle to the package.</p></td>
<td>unsignedLong</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ResourceId</strong></td>
<td><p>Describes the type of resource in the package.</p></td>
<td>A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Size</strong></td>
<td><p>Describes the size in bytes of the package.</p></td>
<td>unsignedLong</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Type</strong></td>
<td><p>Defines the type of package in the bundle.</p></td>
<td>Specifies the package type as app or resource.</td>
<td>No</td>
<td>resource</td>
</tr>
<tr class="odd">
<td><strong>Version</strong></td>
<td><p>Defines the version number of the package.</p></td>
<td>A version string in quad notation, &quot;Major.Minor.Build.Revision&quot;.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td>[Resources](element-resources.md)</td>
<td><p>Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains.</p></td>
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
<td>[Packages](element-packages.md)</td>
<td><p>Defines the app packages and resource packages that are contained in the bundle.</p></td>
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

 

 



