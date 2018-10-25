---
Description: Specifies a data package format such as text or HTML format that the app can share. 
Search.Product: eADQiWindows 10XVcnh
title: uap:DataFormat (Windows 10)
ms.assetid: 348b61e7-ecbd-42ea-8a82-81ef85e728cb
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:DataFormat (Windows 10)


Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.

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
<dd><b>&lt;uap:DataFormat&gt;</b></dd>
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
<DataFormat>

  A string between 1 and 255 characters in length. DataFormat values specified by the user must be unique within the app. 

</uap:DataFormat>
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
<td>[uap:ShareTarget](element-uap-sharetarget.md)</td>
<td><p>Declares an app extension point of type <strong>windows.shareTarget</strong>. The app can share the specified types of files.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XAML
<uap:ShareTarget>
  <uap:SupportedFileTypes>
    <uap:FileType>.txt</uap:FileType>
    <uap:FileType>.docx</uap:FileType>
  </uap:SupportedFileTypes>
  <uap:DataFormat>Text</uap:DataFormat>
  <uap:DataFormat>Uri</uap:DataFormat>
  <uap:DataFormat>Bitmap</uap:DataFormat>
  <uap:DataFormat>Html</uap:DataFormat>
  <uap:DataFormat>http://schema.org/Book</uap:DataFormat>
</uap:ShareTarget>
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
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



