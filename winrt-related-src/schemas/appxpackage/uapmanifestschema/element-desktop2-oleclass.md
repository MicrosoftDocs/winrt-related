---
author: laurenhughes
ms.assetid: 6e4f6092-889f-4462-baf5-45ba7ca0359a
title: desktop2:OleClass
description: Enables OLE to get the OLE class registered for a given file extension.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:OleClass


## Description
Enables OLE to get the OLE class registered for a given file extension.

## Element Hierarchy
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
<dt><a href="element-uap-filetypeassociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;desktop2:OleClass&gt;</b></dd>
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
```syntax
<desktop2:OleClass Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The ID of a COM class registered in the [<ComServer>](element-com-comserver.md) element.| A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Remarks
A `<desktop2:OleClass>` element can only exist under a `<FileTypeAssociation>` element that is defined with an `<Application>` element that has: EntryPoint="windows.FullTrustApplication".

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>