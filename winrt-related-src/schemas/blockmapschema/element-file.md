---
Description: Represents a file contained in the package.
Search.Product: eADQiWindows 10XVcnh
title: File
ms.assetid: ea222abe-8c05-4f31-b494-be5459bd7620
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/17
---

# File

Represents a file contained in the package.

## Element hierarchy

<dl>
<dt><a href="element-blockmap.md">&lt;BlockMap&gt;</a></dt>
<dd><b>&lt;File&gt;</b></dd>
</dl>

## Syntax

``` syntax
<File Name    = The name of the file must be non-empty and no more than 260 (MAX_PATH) characters supported by the APPX package format (even though ZIP format supports up to 65535 bytes).
      Size    = nonNegativeInteger
      LfhSize = The size of the Local File Header for a file must be at least 30 bytes and no more than 64KB as required by the ZIP format. >

  <!-- Child elements -->
  Block*

</File>
```

### Key

`*`   optional (zero or more)

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
<td><strong>LfhSize</strong></td>
<td><p>Size, in bytes, of the file's Local File Header (LFH) structure in the package. For more info about file headers, see [ZIP file format specification](http://www.pkware.com/documents/casestudies/APPNOTE.TXT).</p></td>
<td>The size of the Local File Header for a file must be at least 30 bytes and no more than 64KB as required by the ZIP format.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Name</strong></td>
<td><p>Root path and file name.</p></td>
<td>The name of the file must be non-empty and no more than 260 (MAX_PATH) characters supported by the APPX package format (even though ZIP format supports up to 65535 bytes).</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Size</strong></td>
<td><p>Size, in bytes, of the file's uncompressed data.</p></td>
<td>nonNegativeInteger</td>
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
<td>[Block](element-block.md)</td>
<td><p>Represents a block of binary data contained in a file.</p></td>
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
<td>[BlockMap](element-blockmap.md)</td>
<td><p>Defines the root element of the app package block map. The [<strong>BlockMap</strong>](element-blockmap.md) element specifies the algorithm that is used to compute cryptographic hashes and contains a sequence of [<strong>File</strong>](element-file.md) child elements that are associated with each file that is stored in the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The order of the [**Block**](element-block.md) child elements must correspond to the order of the data blocks as they appear in the file being represented.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/blockmap</p></td>
</tr>
</tbody>
</table>

 

 



