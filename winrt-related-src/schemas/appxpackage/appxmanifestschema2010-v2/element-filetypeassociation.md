---
description: Declares an app extensibility point of type windows.fileTypeAssociation (Windows 8.1).
Search.Product: eADQiWindows 10XVcnh
title: FileTypeAssociation (Windows 8.1 extensions schema)
ms.assetid: 864e99f6-8685-4010-ae55-a4d09f53159f


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# FileTypeAssociation (extensions schema for Windows 8.1)




Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;FileTypeAssociation&gt;</b></dd>
</dl>

## Syntax

``` syntax
<FileTypeAssociation Name           = A string between 1 and 100 characters in length.
                     m:DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" >

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
<tr class="even">
<td><strong>m:DesiredView</strong></td>
<td><p>The desired view of the app.</p>

<strong>Windows Phone:  DesiredView</strong> isn't supported for Windows Phone.
</td>
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
<td><a href="element-displayname.md">DisplayName</a> </td>
<td><p>A friendly name that can be displayed to users. This string is localizable.</p></td>
</tr>
<tr class="even">
<td><a href="element-editflags.md">EditFlags</a> </td>
<td><p>Specifies the type of info the user sees when opening a file associated to the extensibility point.</p></td>
</tr>
<tr class="odd">
<td><a href="element-infotip.md">InfoTip</a> </td>
<td><p>Defines a string that provides additional info to the user about the file type.</p></td>
</tr>
<tr class="even">
<td><a href="element-logo.md">Logo</a> </td>
<td><p>A path to a file that contains an image.</p></td>
</tr>
<tr class="odd">
<td><a href="element-supportedfiletypes.md">SupportedFileTypes (type: CT_FTASupportedFileTypes)</a> </td>
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
<td><a href="element-extension.md">Extension (type: CT_ApplicationExtension)</a> </td>
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
[How to handle file activation](/previous-versions/windows/apps/hh452684(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
