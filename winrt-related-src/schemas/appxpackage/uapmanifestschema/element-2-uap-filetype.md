---
Description: A file type specified as its file type extension.
Search.Product: eADQiWindows 10XVcnh
title: uap:FileType (uap:FileOpenPicker/uap:SupportedFileTypes)
ms.assetid: bc6e06c8-552b-4113-b92f-3f9e7228ebf2
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:FileType (in uap:FileOpenPicker/uap:SupportedFileTypes)


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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-sharetarget.md">&lt;uap:ShareTarget&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:FileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-uap-fileopenpicker.md">&lt;uap:FileOpenPicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-2-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:FileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-uap-filesavepicker.md">&lt;uap:FileSavePicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-3-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:FileType&gt;</b></dd>
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

  A string between 1 and 64 characters in length that must begin with a period ("."), cannot have additional periods, and cannot contain these characters: <, >, :, ", /, \, |, ?, or *.

</uap:FileType>
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
<td><a href="element-2-uap-supportedfiletypes.md">uap:SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[uap:FileType (in type: CT_FTASupportedFileTypes)](element-uap-filetype.md)**

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



