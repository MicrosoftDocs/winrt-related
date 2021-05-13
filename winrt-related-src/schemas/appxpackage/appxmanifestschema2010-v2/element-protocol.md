---
description: Declares an app extensibility point of type windows.protocol
Search.Product: eADQiWindows 10XVcnh
title: Protocol (Windows 8.1 extensions schema)
ms.assetid: ac911c85-02eb-408c-8c4b-24a4e172df8b


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Protocol (extensions schema for Windows 8.1)

Declares an app extensibility point of type **windows.protocol**. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;Protocol&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Protocol Name           = A string between 2 and 39 characters in length that contains numbers, lowercased letters, dots ('.'), pluses('+'), or hyphens ('-'). The string can't start with a dot ('.').

          m:DesiredView? = "default" | "useLess" | "useHalf" | "useMore" | "useMinimum" >

  <!-- Child elements -->
  ( Logo?
  & DisplayName?
  )

</Protocol>
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
<td><p>The name of the URI scheme, such as &quot;mailto&quot;. This name must be unique for the package.</p></td>
<td>A string between 2 and 39 characters in length that contains numbers, lowercased letters, dots ('.'), pluses('+'), or hyphens ('-'). The string can't start with a dot ('.').</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>m:DesiredView</strong></td>
<td><p>The desired view of the app.</p>
<blockquote>
<strong>Windows Phone:  DesiredView</strong> isn't supported for Windows Phone.
</blockquote></td>
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
<td><a href="element-1-displayname.md">DisplayName</a> </td>
<td><p>A friendly name that can be displayed to users. This string is localizable.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-logo.md">Logo</a> </td>
<td><p>A path to a file that contains an image.</p></td>
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

 

## See also


**Tasks**
[How to handle URI activation](/previous-versions/windows/apps/hh452686(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
