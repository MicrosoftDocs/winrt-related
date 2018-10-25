---
Description: Represents a block of binary data contained in a file.
Search.Product: eADQiWindows 10XVcnh
title: Block
ms.assetid: 7b4a9f58-a370-41f1-9234-004fc8ba425b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Block

Represents a block of binary data contained in a file.

## Element hierarchy

<dl>
<dt><a href="element-blockmap.md">&lt;BlockMap&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-file.md">&lt;File&gt;</a></dt>
<dd><b>&lt;Block&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Block Hash  = base64Binary
       Size? = positiveInteger />
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
<td><strong>Hash</strong></td>
<td><p>The hash value of the uncompressed data block.</p></td>
<td>base64Binary</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Size</strong></td>
<td><p>The size, in bytes, of the data block when stored in the package. If the file data is compressed, the size of each compressed block potentially varies in size.</p></td>
<td>positiveInteger</td>
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
<td>[File](element-file.md)</td>
<td><p>Represents a file contained in the package.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Except for the last block of a file, **Block** elements represent a 64-KB (65536 bytes) block of uncompressed data within a file that is stored in the app package. Each **Block** element specifies a cryptographic “hash” value that is used to validate the block data. For files that are stored in the package with DEFLATE-compression, **Block** elements specify a **Size** attribute that defines to the number of compressed bytes that are used to store the compressed data sequence for the block.

The **Hash** attribute value is the base64 encoded value of the hash of the data represented by the **Block** element. When an app file is added to the app package, it is first divided into 64-KB blocks, and each block is hashed using the algorithm specified by the **HashMethod** attribute on the [**BlockMap**](element-blockmap.md) element. If the size of the file is not an even multiple of 64 KB, the size of the final block is inferred as the remainder of the file size divided by 64 KB.

The **Size** attribute value is the size of the data block as stored in the app package. This is usually smaller than 64 KB because each block is commonly compressed before being stored in the app package. Because data compression (Deflate algorithm) produces a variable-length result, the **Size** attribute must be specified for all blocks of a file stored in compressed form within the package. The **Size** attribute isn't specified if the file is not compressed; if the **Size** attribute isn't specified, the value defaults to 64 KB, or the remainder of the file size divided by 64 KB if the block is the last block.

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

 

 



