---
description: A supported file type specified as its file type extension.
Search.Product: eADQiWindows 10XVcnh
title: 'FileType (Windows 8.1 extensions schema, descendant of FileTypeAssociation)'
ms.assetid: ee9a5cc3-18aa-458e-88aa-b1000c35abd3


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# FileType (extensions schema for Windows 8.1, descendant of FileTypeAssociation)




A supported file type specified as its file type extension.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-filetypeassociation.md">&lt;FileTypeAssociation&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;FileType&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<FileType ContentType? = A string that contains two components between 1 and 127 characters in length, separated by a forward slash ("/"). It follows the RFC 4288 naming requirements.  >

  A string between 1 and 64 characters in length that includes a period (".").

</FileType>
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
<td><strong>ContentType</strong></td>
<td><p>The content type.</p></td>
<td>A string that contains two components between 1 and 127 characters in length, separated by a forward slash (&quot;/&quot;). It follows the RFC 4288 naming requirements.</td>
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
<td><a href="element-supportedfiletypes.md">SupportedFileTypes (type: CT_FTASupportedFileTypes)</a> </td>
<td><p>Defines the file types associated with the app. They are unique per package and are case sensitive.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[FileType (type: ST_FileType)](element-1-filetype.md)**

## Requirements

|               |    Value                                                         |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



