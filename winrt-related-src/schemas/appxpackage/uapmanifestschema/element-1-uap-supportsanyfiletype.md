---
description: Indicates whether all file types are supported for sharing.
Search.Product: eADQiWindows 10XVcnh
title: uap:SupportsAnyFileType (Windows 10)
ms.assetid: dbc9307b-0811-49b6-8f97-938313188453


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:SupportsAnyFileType (Windows 10)


Indicates whether all file types are supported for sharing.

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
<dt><a href="element-uap-sharetarget.md">&lt;uap:ShareTarget&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:SupportsAnyFileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-uap-fileopenpicker.md">&lt;uap:FileOpenPicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-2-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:SupportsAnyFileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-uap-filesavepicker.md">&lt;uap:FileSavePicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-3-uap-supportedfiletypes.md">&lt;uap:SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;uap:SupportsAnyFileType&gt;</b></dd>
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
<SupportsAnyFileType>

  xs:anyType

</uap:SupportsAnyFileType>
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
<td><a href="element-2-uap-supportedfiletypes.md">uap:SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 



