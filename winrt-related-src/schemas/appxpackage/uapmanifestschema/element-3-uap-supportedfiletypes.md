---
Description: Defines the file types that the app can share.
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportedFileTypes (in uap:FileSavePicker)
ms.assetid: 4ee91f62-936f-4ada-b42b-45b36a534e0d
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:SupportedFileTypes (in uap:FileSavePicker)


Defines the file types that the app can share.

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
<dd><b>&lt;uap:SupportedFileTypes&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-uap-fileopenpicker.md">&lt;uap:FileOpenPicker&gt;</a></dt>
<dd><b>&lt;uap:SupportedFileTypes&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-uap-filesavepicker.md">&lt;uap:FileSavePicker&gt;</a></dt>
<dd><b>&lt;uap:SupportedFileTypes&gt;</b></dd>
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
<SupportedFileTypes>

  <!-- Child elements -->
  ( uap:FileType{1,10000}
  | uap:SupportsAnyFileType
  )

</uap:SupportedFileTypes>
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
<td><a href="element-3-uap-filetype.md">uap:FileType (type: ST_FileType)</a> </td>
<td><p>A file type specified as its file type extension. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="even">
<td><a href="element-2-uap-supportsanyfiletype.md">uap:SupportsAnyFileType</a> </td>
<td><p>Indicates whether all file types are supported for sharing.</p></td>
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
<td><a href="element-uap-fileopenpicker.md">uap:FileOpenPicker</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileOpenPicker</strong>. The app lets the user choose and open the specified types of files.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-filesavepicker.md">uap:FileSavePicker</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileSavePicker</strong>. The app lets the user choose the file name, extension, and storage location for the specified types of files.</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap-sharetarget.md">uap:ShareTarget</a> </td>
<td><p>Declares an app extension point of type <strong>windows.shareTarget</strong>. The app can share the specified types of files.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md)**

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

 

 



