---
Description: Provides details for each element, attribute, and data type that defines the schema for the package block map that is stored in the file AppxBlockMap.xml as part of a UWP app.
Search.Product: eADQiWindows 10XVcnh
title: Package block map schema reference
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Package block map schema reference


This reference provides details for each element, attribute, and data type that defines the schema for the package block map that is stored in the file AppxBlockMap.xml as part of a UWP app. The schema definition file is BlockMapSchema.xsd.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-block.md">Block</a> </td>
<td><p>Represents a block of binary data contained in a file.</p></td>
</tr>
<tr class="even">
<td><a href="element-blockmap.md">BlockMap</a> </td>
<td><p>Defines the root element of the app package block map. The <a href="element-blockmap.md"><strong>BlockMap</strong></a>  element specifies the algorithm that is used to compute cryptographic hashes and contains a sequence of <a href="element-file.md"><strong>File</strong></a> child elements that are associated with each file that is stored in the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-file.md">File</a> </td>
<td><p>Represents a file contained in the package.</p></td>
</tr>
</tbody>
</table>

 

 

 



