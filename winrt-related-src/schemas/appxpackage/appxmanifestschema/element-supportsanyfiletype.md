---
description: Indicates whether all file types are supported for sharing (package schema for Windows 8, descendant of ShareTarget).
Search.Product: eADQiWindows 10XVcnh
title: SupportsAnyFileType (Windows 8 package schema, descendant of ShareTarget)
ms.assetid: be446c1e-2be7-47eb-8ac9-9dd32733465a


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# SupportsAnyFileType (package schema for Windows 8, descendant of ShareTarget)


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
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-sharetarget.md">&lt;ShareTarget&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;SupportsAnyFileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-fileopenpicker.md">&lt;FileOpenPicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-2-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;SupportsAnyFileType&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-filesavepicker.md">&lt;FileSavePicker&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-3-supportedfiletypes.md">&lt;SupportedFileTypes&gt;</a></dt>
<dd><b>&lt;SupportsAnyFileType&gt;</b></dd>
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

</SupportsAnyFileType>
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
<td><a href="element-1-supportedfiletypes.md">SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XAML
<ShareTarget>
  <SupportedFileTypes>
    <SupportsAnyFileType />
  </SupportedFileTypes>
  <DataFormat>Text</DataFormat>
  <DataFormat>Uri</DataFormat>
</ShareTarget>
```

## Requirements

|               |   Value                                                          |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



