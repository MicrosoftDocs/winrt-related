---
author: mcleanbyron
ms.assetid: 706cd678-5620-4733-880b-72641a308c3c
title: desktop2:SearchFilterHandler
description: Enables Windows Desktop Bridge apps to register IFilters to extract file properties for searching.
ms.author: mcleans
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:SearchFilterHandler


## Description
Enables Windows Desktop Bridge apps to register IFilters to extract file properties for searching.

## Element Hierarchy
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
<dt><a href="element-desktop2-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd><b>&lt;desktop2:SearchFilterHandler&gt;</b></dd>
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
```syntax
<desktop2:SearchFilterHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
                              Path?  = A string between 1 and 256 characters in length, ending with ".dll" and cannot contain these characters: <, >, :, ", |, ?, or *.
                              ProcessorArchitecture? = One of the following: x86, x64, arm, arm64, neutral. >

 <!-- Child elements -->
 desktop2:FilterExtension{0,10000}
</desktop2:SearchFilterHandler>
```

### Key
`{}` specific range of occurrences
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The ID of the class that will be activated to handle requests for files. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| Path | The path to the binary in the app's package. | A string between 1 and 256 characters in length, ending with ".dll" and cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | No |
| ProcessorArchitecture | The processor architecture. | One of the following: x86, x64, arm, arm64, neutral. | Yes |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [FilterExtension](element-desktop2-FilterExtension.md) | Specifies the file type to be registered by the app. |

## Remarks

## Examples

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>