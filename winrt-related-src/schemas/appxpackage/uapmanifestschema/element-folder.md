---
Description: Specifies a folder that the package shares with other packages from the same publisher.
Search.Product: eADQiWindows 10XVcnh
title: Folder (Windows 10)
ms.assetid: b412b98e-130a-4152-a264-49a42ef2d97c


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Folder (Windows 10)


Specifies a folder that the package shares with other packages from the same publisher.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-publishercachefolders.md">&lt;PublisherCacheFolders&gt;</a></dt>
<dd><b>&lt;Folder&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Folder Name = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. />
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
<td><strong>Name</strong></td>
<td><p>The folder name, which must be string valid for a folder name. Sub-folders in the folder name are not allowed (no / or \ characters).</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
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
<td><a href="element-publishercachefolders.md">PublisherCacheFolders</a> </td>
<td><p>Declares a package extensibility point of type <strong>windows.publisherCacheFolders</strong>. This specifies one or more folders that the package shares with other packages from the same publisher.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XML
    <Extension Category="windows.publisherCacheFolders">
        <Folder Name="Folder1"/>
        <Folder Name="Folder2"/>
    </Extension>
```

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

 

 



