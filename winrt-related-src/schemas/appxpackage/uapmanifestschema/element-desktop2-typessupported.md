---
author: laurenhughes
ms.assetid: f2d6f151-53bb-4ae0-971b-23f8deb16980
title: desktop2:TypesSupported
description: Contains the event log types that are supported.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:TypesSupported


## Description
Contains the event log types that are supported.

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
<dd><b>&lt;desktop2:TypesSupported&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<desktop2:TypesSupported>
  <!-- Child elements -->
  desktop2:TypeSupported{1,5} 
</desktop2:TypesSupported>
```

### Key
`{}` specific range of occurrences

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [TypeSupported](element-desktop2-typesupported.md) | Specifies the types of events that are supported. |

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