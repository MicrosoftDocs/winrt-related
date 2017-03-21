---
Description: uap:FileTypeAssociation (Windows 10)
Search.Product: eADQiWindows 10XVcnh
title: uap:FileTypeAssociation (Windows 10)
ms.assetid: 5e876ef3-c8ca-461d-9764-4ea672e7c0ea
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# uap:FileTypeAssociation (Windows 10)


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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd><b>&lt;uap:FileTypeAssociation&gt;</b></dd>
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
<FileTypeAssociation Name         = A string between 1 and 100 characters in length.
                         DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" >

  <!-- Child elements -->
  ( uap:DisplayName?
  & uap:Logo?
  & uap:InfoTip?
  & uap:EditFlags?
  & uap:SupportedFileTypes
  )

</uap:FileTypeAssociation>
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
<td><strong>DesiredView</strong></td>
<td><p>The desired amount of screen space to use when the appointment launches.</p></td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>default</li>
<li>useLess</li>
<li>useHalf</li>
<li>useMore</li>
<li>useMinimum</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
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
<td>[uap:DisplayName](element-uap-displayname.md)</td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td>[uap:EditFlags](element-uap-editflags.md)</td>
<td><p>Specifies the type of info the user sees when opening a file associated to the extensibility point.</p></td>
</tr>
<tr class="odd">
<td>[uap:InfoTip](element-uap-infotip.md)</td>
<td><p>Defines a string that provides additional info to the user about the file type.</p></td>
</tr>
<tr class="even">
<td>[uap:Logo](element-uap-logo.md)</td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="odd">
<td>[uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)](element-uap-supportedfiletypes.md)</td>
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
<td>[uap:Extension](element-uap-extension.md)</td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

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

 

 



