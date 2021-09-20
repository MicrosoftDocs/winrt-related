---
description: Declares an app extensibility point of type windows.fileSavePicker (Windows 8.1).
Search.Product: eADQiWindows 10XVcnh
title: FileSavePicker (Windows 8.1 extensions schema)
ms.assetid: c2d3002e-69e1-479c-a0ec-9facf5bc7142


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# FileSavePicker (extensions schema for Windows 8.1)




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
<td><a href="element-3-supportedfiletypes.md">SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
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
<td><a href="element-extension.md">Extension (type: CT_ApplicationExtension)</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## See also


**Tasks**
[Accessing files with file pickers](/previous-versions/windows/apps/hh465174(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|               |   Value                                                          |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
