---
Description: Declares an app extensibility point of type windows.fileOpenPicker.
Search.Product: eADQiWindows 10XVcnh
title: FileOpenPicker
ms.assetid: 25af7399-25ca-4a8b-a892-396f6b4d170c


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-2-supportedfiletypes.md">SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
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
[Accessing files with file pickers](https://msdn.microsoft.com/library/windows/apps/hh465174)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



