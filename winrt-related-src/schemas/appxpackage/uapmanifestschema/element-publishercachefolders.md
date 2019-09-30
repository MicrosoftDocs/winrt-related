---
Description: Declares a package extensibility point of type windows.publisherCacheFolders.
Search.Product: eADQiWindows 10XVcnh
title: PublisherCacheFolders (Windows 10)
ms.assetid: 71425cb8-5f6b-415a-9791-28c7407869dc
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# PublisherCacheFolders (Windows 10)


Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;PublisherCacheFolders&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<PublisherCacheFolders>

  <!-- Child elements -->
  Folder{1,100}

</PublisherCacheFolders>
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
<td><a href="element-folder.md">Folder</a> </td>
<td><p>Specifies a folder that the package shares with other packages from the same publisher.</p></td>
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
<td><a href="element-extension.md">Extension (in type: CT_PackageExtensions)</a> </td>
<td><p>Declares an extensibility point for the package.</p></td>
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
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



