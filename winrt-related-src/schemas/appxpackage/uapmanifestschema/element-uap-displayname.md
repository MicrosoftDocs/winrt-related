---
Description: A friendly name that can be displayed to users.
Search.Product: eADQiWindows 10XVcnh
title: uap:DisplayName (Windows 10)
ms.assetid: c4e698b0-58ac-46d0-8874-f7a062c88343
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:DisplayName (Windows 10)


A friendly name that can be displayed to users.

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
<dd><b>&lt;uap:DisplayName&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-uap-protocol.md">&lt;uap:Protocol&gt;</a></dt>
<dd><b>&lt;uap:DisplayName&gt;</b></dd>
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
<uap:DisplayName>

  A string between 1 and 256 characters in length. This string is localizable. 

</uap:DisplayName>
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

This string is localizable. 

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

 

 



