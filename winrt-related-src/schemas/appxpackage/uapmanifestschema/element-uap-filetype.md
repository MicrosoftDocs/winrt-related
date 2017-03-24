---
Description: A supported file type specified as its file type extension.
Search.Product: eADQiWindows 10XVcnh
title: uap:FileType (in uap:FileTypeAssociation/uap:SupportedFileTypes)
ms.assetid: 9a872ee1-03fa-48f0-bc13-e35c7a22820e
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# uap:FileType (in uap:FileTypeAssociation/uap:SupportedFileTypes) 


A supported file type specified as its file type extension.

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
<dd>
<dl>
<dt><a href="element-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:FileType&gt;</b></dd>
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
</dd>
</dl>

## Syntax

``` syntax
<uap:FileType ContentType? = A string that contains two components between 1 and 127 characters in length, separated by a forward slash ("/"). It follows the RFC 4288 naming requirements. 
              uap4:ShellNewFileName? = A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", |, ?, or *.
              uap4:ShellNewDisplayName? = A string between 1 and 256 characters in length. This string is localizable. >

  This element has no child elements.

</uap:FileType>
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
<td><strong>ContentType</strong></td>
<td><p>The content type.</p></td>
<td>A string that contains two components between 1 and 127 characters in length, separated by a forward slash (&quot;/&quot;). It follows the RFC 4288 naming requirements.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>uap4:ShellNewFileName</strong></td>
<td><p>The file from the package to be copied to the location where the user initiated the Shell New command.</p></td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap4:ShellNewDisplayName</strong></td>
<td><p>The display name of the file type that shows when a user hovers over the "New" submenu in the Windows explorer.</p></td>
<td>A string between 1 and 256 characters in length. This string is localizable.</td>
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
<td>[uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md)</td>
<td><p>Defines the file types associated with the app. They are unique per package and are case sensitive.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[uap:FileType (type: ST_FileType)](element-1-uap-filetype.md)**

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

 

 



