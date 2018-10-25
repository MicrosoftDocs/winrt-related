---
Description: A file type specified as its file type extension.
Search.Product: eADQiWindows 10XVcnh
title: 'FileType (type: ST_FileType)'
ms.assetid: a3792047-9fbf-42d5-b629-0025717d0323
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# FileType (type: ST_FileType)


A file type specified as its file type extension. It is unique per application in the package and is case sensitive.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-sharetarget.md">&lt;ShareTarget&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;FileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-fileopenpicker.md">&lt;FileOpenPicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-2-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;FileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-filesavepicker.md">&lt;FileSavePicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-3-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;FileType&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<FileType>

  A string between 1 and 64 characters in length that must begin with a period ("."), cannot have additional periods, and cannot contain these characters: <, >, :, %, ", /, \, |, ?, or *.

</FileType>
```

## Attributes and Elements


### Attributes

None.

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
<td>[SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-2-supportedfiletypes.md)</td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[FileType (in type: CT_FTASupportedFileTypes)](element-filetype.md)**

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

 

 



