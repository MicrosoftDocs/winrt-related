---
description: Defines a string that provides additional info to the user about the file type.
Search.Product: eADQiWindows 10XVcnh
title: InfoTip (Windows 8.1 extensions schema)
ms.assetid: 62db4269-58c1-4327-9115-103c6ce7774d


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# InfoTip (extensions schema for Windows 8.1)




Defines a string that provides additional info to the user about the file type.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-filetypeassociation.md">&lt;FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;InfoTip&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<InfoTip>

  A string between 1 and 1024 characters in length.

</InfoTip>
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
<td><a href="element-filetypeassociation.md">FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This string is localizable. 

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



