---
Description: Declares an app extension point of type windows.shareTarget.
Search.Product: eADQiWindows 10XVcnh
title: uap:ShareTarget (Windows 10)
ms.assetid: 92622f42-dfef-4fd2-a42d-73d4ac47357c
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:ShareTarget (Windows 10)


Declares an app extension point of type **windows.shareTarget**. The app can share the specified types of files.

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
<dd><b>&lt;uap:ShareTarget&gt;</b></dd>
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
<ShareTarget Description? = A string between 1 and 256 characters in length. >

  <!-- Child elements -->
  uap:SupportedFileTypes?,
  uap:DataFormat{0,10000}

</uap:ShareTarget>
```

### Key

`?`   optional (zero or one)
`{}`   specific range of occurrences
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
<td><strong>Description</strong></td>
<td><p>The description of the share target.</p></td>
<td>A string between 1 and 256 characters in length.</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[uap:DataFormat](element-uap-dataformat.md)</td>
<td><p>Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="even">
<td>[uap:SupportedFileTypes (type: CT_CharmsSupportedFileTypes)](element-1-uap-supportedfiletypes.md)</td>
<td><p>Defines the file types that the app can share.</p></td>
</tr>
</tbody>
</table>

 

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
<td>[uap:Extension](element-uap-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The Share feature provides access to a list of target apps that can receive data that the user wants to share. This extensibility point enables your app to be included in the list of share targets.

[**ShareTarget**](https://msdn.microsoft.com/library/windows/apps/br211466) must specify either [**SupportedFileTypes**](https://msdn.microsoft.com/library/windows/apps/br211468) element, or at least one [**DataFormat**](https://msdn.microsoft.com/library/windows/apps/br211426) element. It cannot omit both. The schema allows omitting both, but semantic validation will fail.

## Examples

```XML
<uap:Extension Category="windows.shareTarget">
  <uap:ShareTarget>
    <uap:SupportedFileTypes>
      <uap:SupportsAnyFileType />
    </uap:SupportedFileTypes>
    <uap:DataFormat>Text</uap:DataFormat>
    <uap:DataFormat>Uri</uap:DataFormat>
    <uap:DataFormat>Bitmap</uap:DataFormat>
    <uap:DataFormat>Html</uap:DataFormat>
    <uap:DataFormat>http://schema.org/Book</DataFormat>
  </uap:ShareTarget>
</uap:Extension>
```

## See also


**Tasks**
[Adding share](https://msdn.microsoft.com/library/windows/apps/hh758314)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

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

 

 



