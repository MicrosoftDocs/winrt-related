---
Description: 'SupportedFileTypes (type: CT\_FTASupportedFileTypes)'
MS-HAID: AppxManifestSchema2010\_v2.element\_SupportedFileTypes
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: 'SupportedFileTypes (type: CT\_FTASupportedFileTypes)'
ms.assetid: b231434d-8bd1-47c4-8330-fb289be5894f
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# SupportedFileTypes (type: CT\_FTASupportedFileTypes)

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
<td>[FileType (in type: CT_FTASupportedFileTypes)](element-filetype.md)</td>
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
<td>[FileTypeAssociation](element-filetypeassociation.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[SupportedFileTypes (type: CT\_CharmsSupportedFileTypes)](element-1-supportedfiletypes.md)**

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

 

 



