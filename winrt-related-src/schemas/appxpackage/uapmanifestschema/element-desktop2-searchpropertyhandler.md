---
author: mcleanbyron
ms.assetid: 92f81548-6524-4d3f-8e9c-5a671fa72813
title: desktop2:SearchPropertyHandler
description: Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search.
ms.author: mcleans
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:SearchPropertyHandler


## Description
Enables Windows Desktop Bridge apps to install property handlers on your system. These handlers are used to read properties from files for indexing and search.

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
<dd><b>&lt;desktop2:SearchPropertyHandler&gt;</b></dd>
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
<desktop2:SearchPropertyHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
                                Path  = A string between 1 and 256 characters in length, ending with ".dll" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or *.
                                ProcessorArchitecture = One of the following: x86, x64, arm, arm64, neutral. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The ID of the class in the app's package. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| Path | Path relative to the binary that implements the CLSID. | A string between 1 and 256 characters in length, ending with ".dll" and cannot contain these characters: &lt;, &gt;, :, ", &#124;, ?, or *. | No |
| ProcessorArchitecture | The processor architecture. | One of the following: x86, x64, arm, arm64, neutral. | Yes |

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