---
description: Specifies the type of info the user sees when opening a file associated to the extensibility point (Windows 8).
Search.Product: eADQiWindows 10XVcnh
title: EditFlags (package schema for Windows 8)
ms.assetid: 0f77fddc-bb6d-4d5e-9d15-577a2e5fcfff


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# EditFlags (package schema for Windows 8)


Specifies the type of info the user sees when opening a file associated to the extensibility point.

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
<dt><a href="element-filetypeassociation.md">&lt;FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;EditFlags&gt;</b></dd>
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
<EditFlags OpenIsSafe?   = boolean
           AlwaysUnsafe? = boolean />
```

### Key

`?`   optional (zero or one)

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
<td><strong>AlwaysUnsafe</strong></td>
<td><p>A dialog box with a security warning is displayed.</p></td>
<td>boolean</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>OpenIsSafe</strong></td>
<td><p>A dialog box with a standard warning is displayed.</p></td>
<td>boolean</td>
<td>No</td>
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
<td><a href="element-filetypeassociation.md">FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



