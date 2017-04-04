---
Description: Declares an app extensibility point of type windows.fileSavePicker.
Search.Product: eADQiWindows 10XVcnh
title: FileSavePicker
ms.assetid: c2d3002e-69e1-479c-a0ec-9facf5bc7142
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# FileSavePicker




Declares an app extensibility point of type **windows.fileSavePicker**. The app lets the user choose the file name, extension, and storage location for the specified types of files.

## Element hierarchy

<h2>Element hierarchy</h2>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;FileSavePicker&gt;</b></dd>
</dl>

## Syntax

``` syntax
<FileSavePicker>

  <!-- Child elements -->
  SupportedFileTypes

</FileSavePicker>
```

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
<td>[SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-3-supportedfiletypes.md)</td>
<td><p>Defines the file types that the app can share.</p></td>
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
<td>[Extension (type: CT_ApplicationExtension)](element-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## See also


**Tasks**
[Accessing files with file pickers](https://msdn.microsoft.com/library/windows/apps/hh465174)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

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

 

 



