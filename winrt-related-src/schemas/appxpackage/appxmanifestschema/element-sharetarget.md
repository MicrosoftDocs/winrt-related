---
Description: Declares an app extension point of type windows.shareTarget.
Search.Product: eADQiWindows 10XVcnh
title: ShareTarget
ms.assetid: 42f77354-83be-4f41-bf89-95566d026687


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ShareTarget


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
<dt><a href="element-1-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;ShareTarget&gt;</b></dd>
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
<ShareTarget>

  <!-- Child elements -->
  SupportedFileTypes?,
  DataFormat{0,10000}

</ShareTarget>
```

### Key

`?`   optional (zero or one)

`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-dataformat.md">DataFormat</a> </td>
<td><p>Specifies a data package format such as text or HTML format that the app can share. It is unique per application in the package and is case sensitive.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-supportedfiletypes.md">SupportedFileTypes (type: CT_CharmsSupportedFileTypes)</a> </td>
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
<td><a href="element-1-extension.md">Extension (in type: CT_ApplicationExtensions)</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The Share charm provides access to a list of target apps that can receive data that the user wants to share. This extensibility point enables your app to be included in the list of share targets.

**ShareTarget** must specify either [**SupportedFileTypes**](element-supportedfiletypes.md) element, or at least one [**DataFormat**](element-dataformat.md) element. It cannot omit both. The schema allows omitting both, but semantic validation will fail.

## Examples

```XML
<Extension Category="windows.shareTarget">
  <ShareTarget>
    <SupportedFileTypes>
      <SupportsAnyFileType />
    </SupportedFileTypes>
    <DataFormat>Text</DataFormat>
    <DataFormat>Uri</DataFormat>
    <DataFormat>Bitmap</DataFormat>
    <DataFormat>Html</DataFormat>
    <DataFormat>http://schema.org/Book</DataFormat>
  </ShareTarget>
</Extension>
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
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



