---
Description: FileOpenPicker
MS-HAID: AppxManifestSchema2010\_v2.element\_FileOpenPicker
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: FileOpenPicker
ms.assetid: 25af7399-25ca-4a8b-a892-396f6b4d170c
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# FileOpenPicker




Declares an app extensibility point of type **windows.fileOpenPicker**. The app lets the user choose and open the specified types of files.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;FileOpenPicker&gt;</b></dd>
</dl>

## Syntax

``` syntax
<FileOpenPicker>

  <!-- Child elements -->
  SupportedFileTypes

</FileOpenPicker>
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
<td>[SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-2-supportedfiletypes.md)</td>
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

 

 



