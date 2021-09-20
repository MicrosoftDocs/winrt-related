---
description: A path to a file that contains an image (Windows 8.1, child of Properties).
Search.Product: eADQiWindows 10XVcnh
title: Logo (Windows 8.1 extensions schema, child of Properties)
ms.assetid: ffbb17ac-d3c5-42ea-9a39-167a8dc4d2ba


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Logo (extensions schema for Windows 8.1, child of Properties)




A path to a file that contains an image.

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-filetypeassociation.md">&lt;FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;Logo&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-protocol.md">&lt;Protocol&gt;</a></dt>
<dd><b>&lt;Logo&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;Logo&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Logo>

  A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.

</Logo>
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
<td><a href="element-filetypeassociation.md">FileTypeAssociation</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.fileTypeAssociation</strong>. A file type association indicates that the app is registered to handle files of the specified types.</p></td>
</tr>
<tr class="even">
<td><a href="element-properties.md">Properties</a> </td>
<td><p>Defines additional metadata about the package including attributes that describe how the package appears to users.</p>
<div class="alert">
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td><a href="element-protocol.md">Protocol</a> </td>
<td><p>Declares an app extensibility point of type <strong>windows.protocol</strong>. A URI association indicates that the app is registered to handle URIs with the specified scheme.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The logo image can be given as either a direct path to an image file or as a resource. By using a resource reference, you can supply images of different scales so that Windows can choose the best size for the device and screen resolution. You can also supply high contrast images for accessibility and localized images to match different UI languages. For more info, see the [Globalization](/previous-versions/windows/apps/hh831183(v=win.10)) topic.

Size requirements of logo images provided through this element for various parent elements are shown here:

Image
Scale
Image size in pixels
Package\\Properties\\Logo
100
50x50
140
70x70
180
90x90
Applications\\Application\\Extensions\\Extension\\FileTypeAssociation\\Logo
Does not use scale
N/A
Applications\\Application\\Extensions\\Extension\\Protocol\\Logo
Does not use scale
N/A
 

## Requirements

|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 
