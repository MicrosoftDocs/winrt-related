---
Description: Package block map schema reference
MS-HAID: BlockMapSchema.Schema\_Root
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Package block map schema reference
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, package manifest
---

# Package block map schema reference


This reference provides details for each element, attribute, and data type that defines the schema for the package block map that is stored in the file AppxBlockMap.xml as part of a Windows Store app. The schema definition file is BlockMapSchema.xsd.

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
<td>[Block](element-block.md)</td>
<td><p>Represents a block of binary data contained in a file.</p></td>
</tr>
<tr class="even">
<td>[BlockMap](element-blockmap.md)</td>
<td><p>Defines the root element of the app package block map. The [<strong>BlockMap</strong>](element-blockmap.md) element specifies the algorithm that is used to compute cryptographic hashes and contains a sequence of [<strong>File</strong>](element-file.md) child elements that are associated with each file that is stored in the package.</p></td>
</tr>
<tr class="odd">
<td>[File](element-file.md)</td>
<td><p>Represents a file contained in the package.</p></td>
</tr>
</tbody>
</table>

 

 

 



