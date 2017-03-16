---
Description: uap:FileType (in uap:FileTypeAssociation/uap:SupportedFileTypes) (Windows 10)
MS-HAID: UapManifestSchema.element\_uap\_FileType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: uap:FileType (in uap:FileTypeAssociation/uap:SupportedFileTypes) (Windows 10)
ms.assetid: 9a872ee1-03fa-48f0-bc13-e35c7a22820e
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# uap:FileType (in uap:FileTypeAssociation/uap:SupportedFileTypes) (Windows 10)


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
<FileType ContentType? = A string that contains two components between 1 and 127 characters in length, separated by a forward slash ("/"). It follows the RFC 4288 naming requirements.  >

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

-   **[uap:FileType (type: ST\_FileType)](element-1-uap-filetype.md)**

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

 

 



