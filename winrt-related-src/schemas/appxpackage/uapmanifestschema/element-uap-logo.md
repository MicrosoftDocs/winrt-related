---
description: A path to a file that contains an image (Windows 10, child of uap:FileTypeAssociation).
Search.Product: eADQiWindows 10XVcnh
title: uap:Logo (Windows 10, child of uap:FileTypeAssociation)
ms.assetid: e82d1f5f-e1c8-469c-8568-0736c2a96554


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:Logo (Windows 10, child of uap:FileTypeAssociation)


A path to a file that contains an image.

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
<dt><a href="element-uap-filetypeassociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;uap:Logo&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-uap-protocol.md">&lt;uap:Protocol&gt;</a></dt>
<dd><b>&lt;uap:Logo&gt;</b></dd>
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
<Logo>

  A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.

</uap:Logo>
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
<td><a href="element-uap-filetypeassociation.md">uap:FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-protocol.md">uap:Protocol</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.protocol</strong>. A URI association indicates that the app is registered to handle URIs with the specified scheme.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The logo image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 
