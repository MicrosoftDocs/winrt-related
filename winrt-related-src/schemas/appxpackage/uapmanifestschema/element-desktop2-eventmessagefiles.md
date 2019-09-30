---
author: mcleanbyron
ms.assetid: a0d13555-3408-4d8e-8ac9-223f7b31059f
title: desktop2:EventMessageFiles
description: Contains event message files.
ms.author: mcleans
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:EventMessageFiles


## Description
Contains event message files.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-package-extension.md">&lt;desktop2:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop2-DesktopEventLogging.md">&lt;desktop2:DesktopEventLogging&gt;</a></dt>
<dd><b>&lt;desktop2:EventMessageFiles&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<desktop2:EventMessageFiles>
  <!-- Child elements -->
  desktop2:File{1,1000}
</desktop2:EventMessageFiles>
```

### Key
`{}` specific range of occurrences

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [File](element-desktop2-file.md) | Specifies the path to an event message file. |

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