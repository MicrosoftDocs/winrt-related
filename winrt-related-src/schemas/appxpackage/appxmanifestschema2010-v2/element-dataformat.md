---
Description: Specifies a data package format such as text or HTML format that the app can share. 
Search.Product: eADQiWindows 10XVcnh
title: DataFormat
ms.assetid: a9aa181e-236d-4d33-adcd-54ec8e656891
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# DataFormat




Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-sharetarget.md">&lt;ShareTarget&gt;</a></dt>
<dd><b>&lt;DataFormat&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DataFormat>

  A string between 1 and 255 characters in length. DataFormat values specified by the user must be unique within the app. 

</DataFormat>
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
<td>[ShareTarget](element-sharetarget.md)</td>
<td><p>Declares an app extension point of type <strong>windows.shareTarget</strong>. The app can share the specified types of files.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XAML
<ShareTarget>
  <SupportedFileTypes>
    <FileType>.txt</FileType>
    <FileType>.docx</FileType>
  </SupportedFileTypes>
  <DataFormat>Text</DataFormat>
  <DataFormat>Uri</DataFormat>
  <DataFormat>Bitmap</DataFormat>
  <DataFormat>Html</DataFormat>
  <DataFormat>http://schema.org/Book</DataFormat>
</ShareTarget>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



