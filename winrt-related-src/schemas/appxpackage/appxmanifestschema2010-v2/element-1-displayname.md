---
Description: A friendly name that can be displayed to users. This string is localizable. 
Search.Product: eADQiWindows 10XVcnh
title: DisplayName
ms.assetid: 3c16ea92-5f60-4d15-ac7d-8fc8fee3a51f


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# DisplayName




A friendly name that can be displayed to users. This string is localizable. 

## Element hierarchy

<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-filetypeassociation.md">&lt;FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;DisplayName&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-protocol.md">&lt;Protocol&gt;</a></dt>
<dd><b>&lt;DisplayName&gt;</b></dd>
</dl>
</dd>
</dl>
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;DisplayName&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<DisplayName>

  A string between 1 and 256 characters in length. This string is localizable. 

</DisplayName>
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

 

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 