---
description: Defines the file types associated with the app.
Search.Product: eADQiWindows 10XVcnh
title: 'SupportedFileTypes (type: CT_FTASupportedFileTypes)'
ms.assetid: b231434d-8bd1-47c4-8330-fb289be5894f


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# SupportedFileTypes (type: CT_FTASupportedFileTypes)

Defines the file types associated with the app. They are unique per package and are case sensitive.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-filetypeassociation.md">&lt;FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;SupportedFileTypes&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<SupportedFileTypes>

  <!-- Child elements -->
  FileType{1,1000}

</SupportedFileTypes>
```

### Key

`{}`   specific range of occurrences
## Attributes and Elements


### Attributes

None.

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
<td><a href="element-filetype.md">FileType (in type: CT_FTASupportedFileTypes)</a> </td>
<td><p>A supported file type specified as its file type extension.</p></td>
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
<td><a href="element-filetypeassociation.md">FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-1-supportedfiletypes.md)**

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



