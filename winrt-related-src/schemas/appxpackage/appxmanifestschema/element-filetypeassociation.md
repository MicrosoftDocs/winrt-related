---
Description: FileTypeAssociation
MS-HAID: AppxManifestSchema.element\_FileTypeAssociation
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: FileTypeAssociation
ms.assetid: 864e99f6-8685-4010-ae55-a4d09f53159f
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# FileTypeAssociation


Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types.

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
<dd><b>&lt;FileTypeAssociation&gt;</b></dd>
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
<FileTypeAssociation Name = A string between 1 and 100 characters in length. >

  <!-- Child elements -->
  ( DisplayName?
  & Logo?
  & InfoTip?
  & EditFlags?
  & SupportedFileTypes
  )

</FileTypeAssociation>
```

### Key

`?`   optional (zero or one)

`&`   interleave connector (may occur in any order)

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
<td><strong>Name</strong></td>
<td><p>The name of the file type association. You can use this name to organize and group file types. The name must be all lower case characters with no spaces.</p></td>
<td>A string between 1 and 100 characters in length.</td>
<td>Yes</td>
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
<td>[DisplayName](element-1-displayname.md)</td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td>[EditFlags](element-editflags.md)</td>
<td><p>Specifies the type of info the user sees when opening a file associated to the extensibility point.</p></td>
</tr>
<tr class="odd">
<td>[InfoTip](element-infotip.md)</td>
<td><p>Defines a string that provides additional info to the user about the file type.</p></td>
</tr>
<tr class="even">
<td>[Logo](element-1-logo.md)</td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="odd">
<td>[SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-supportedfiletypes.md)</td>
<td><p>Defines the file types associated with the app. They are unique per package and are case sensitive.</p></td>
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
<td>[Extension (in type: CT_ApplicationExtensions)](element-1-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
<Application Id="App" StartPage="default.html">
    <Extensions>
      <Extension Category="windows.fileTypeAssociation">
        <FileTypeAssociation Name="alsdkjs">
          <SupportedFileTypes>
            <FileType>.alsdkjs</FileType>
          </SupportedFileTypes>
        </FileTypeAssociation>
      </Extension>
    </Extensions>
</Application>
```

## See also


**Tasks**
[How to handle file activation](https://msdn.microsoft.com/library/windows/apps/hh452684)

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

 

 



