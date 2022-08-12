---
description: Declares an app extensibility point of type windows.fileTypeAssociation (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:FileTypeAssociation (Windows 10)
ms.assetid: 5e876ef3-c8ca-461d-9764-4ea672e7c0ea


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
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
<FileTypeAssociation  Name         = A string between 1 and 100 characters in length.
                      DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" 
                      desktop2:UseUrl? = boolean.
                      desktop2:AllowSilentDefaultTakeOver? = boolean 
                      desktop5:ThumbnailTypeOverlay = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both. >

  <!-- Child elements -->
  ( uap:DisplayName?
  & uap:Logo?
  & uap:InfoTip?
  & uap:EditFlags?
  & uap:SupportedFileTypes?
  & uap2:SupportedVerbs?
  & uap4:KindMap?
  & rescap3:MigrationProgIds?
  & desktop2:ThumbnailHandler?
  & desktop2:OleClass?
  & desktop2:DesktopPreviewHandler?
  & desktop2:DesktopPropertyHandler?
  & desktop3:PropertyLists?
  & desktop7:Logo?
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
<tr class="odd">
<td><strong>desktop2:AllowSilentDefaultTakeOver</strong></td>
<td><p>If set to <b>true</b>, the app will appear in an "Open With" list, but it won't be the default app for the file type.</p></td>
<td>Boolean.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>desktop2:UseUrl</strong></td>
<td><p>If set to true, specifies that the application can accept a URL, instead of a file name, on the command line. Applications that can open documents directly from the internet, like web browsers and media players, should use this value. When **ShellExecuteEx** starts an application and this value is set to false, the default behavior, **ShellExecuteEx** downloads the document to a local file and invokes the handler on the local copy.</p></td>
<td>Boolean.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>desktop5:ThumbnailTypeOverlay</strong></td>
<td><p>An image resource for a thumbnail overlay.</p></td>
<td>A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.</td>
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
<td><a href="element-uap-displayname.md">uap:DisplayName</a> </td>
<td><p>A friendly name that can be displayed to users.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-editflags.md">uap:EditFlags</a> </td>
<td><p>Specifies the type of info the user sees when opening a file associated to the extensibility point.</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap-infotip.md">uap:InfoTip</a> </td>
<td><p>Defines a string that provides additional info to the user about the file type.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap-logo.md">uap:Logo</a> </td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="odd">
<td><a href="element-uap-supportedfiletypes.md">uap:SupportedFileTypes (type: CT_FTASupportedFileTypes)</a> </td>
<td><p>Defines the file types associated with the app. They are unique per package and are case sensitive.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap2-supportedverbs.md">uap2:SupportedVerbs</a> </td>
<td><p>Contains verbs for a file context menu.</p></td>
</tr>
<tr class="even">
<td><a href="element-uap4-kindmap.md">uap4:KindMap</a> </td>
<td><p>Specifies what Kind is and how it's used.</p></td>
</tr>
<tr class="odd">
<td><a href="element-rescap3-migrationprogids.md">rescap3:MigrationProgIds</a> </td>
<td><p>Contains <a href="/windows/win32/shell/fa-progids">programmatic identifier (ProgID)</a> values that describe the application, component, and version of each desktop application from which you want to inherit file associations.</p></td>
</tr>
<tr class="even">
<td><a href="element-desktop2-ThumbnailHandler.md">desktop2:ThumbnailHandler</a> </td>
<td><p>Enables a ThumbnailProvider for a file type association.</p></td>
</tr>
<tr class="odd">
<td><a href="element-desktop2-oleclass.md">desktop2:OleClass</a> </td>
<td><p>Enables OLE to get the OLE class registered for a given file extension.</p></td>
</tr>
<tr class="even">
<td><a href="element-desktop2-DesktopPreviewHandler.md">desktop2:DesktopPreviewHandler</a> </td>
<td><p>Enables declaration of a preview handler for a file type association.
</p></td>
</tr>
<tr class="odd">
<td><a href="element-desktop2-DesktopPropertyHandler.md">desktop2:DesktopPropertyHandler</a> </td>
<td><p>Enables declaration of a property handler for a file type association.
</p></td>
</tr>
<tr class="even">
<td><a href="element-desktop3-propertylists.md">desktop3:PropertyLists</a> </td>
<td><p>Contains a list of properties to show under the properties tab of a file.
</p></td>
</tr>
<tr class="odd">
<td><a href="element-desktop7-logo.md">desktop7:Logo</a> </td>
<td><p>A path to a file that contains an image. Adds support for .ico file extensions.</p></td>
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
<td><a href="element-uap-extension.md">uap:Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 
