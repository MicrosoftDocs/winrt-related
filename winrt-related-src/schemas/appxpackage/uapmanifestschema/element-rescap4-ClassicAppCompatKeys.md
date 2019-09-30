---
author: mcleanbyron
title: rescap4:ClassicAppCompatKeys
description: Contains registry keys for discovering classic app installations and launching executables.
ms.author: mcleans
ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap4:ClassicAppCompatKeys


## Description
Contains registry keys for discovering classic app installations and launching executables.

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
<dt><a href="element-rescap4-extension.md">&lt;rescap4:Extension&gt;</a></dt>
<dd><b>&lt;rescap4:ClassicAppCompatKeys&gt;</b></dd>
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
<rescap4:ClassicAppCompatKeys>
  <!-- Child elements -->
  rescap4:ClassicAppCompatKey{1,10000}
</rescap4:ClassicAppCompatKeys>
```

### Key
`{}` specific range of occurrences  

## Attributes
None.

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [ClassicAppCompatKey](element-rescap4-classicappcompatkey.md) | Registry keys for discovering classic app installations and launching executables. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4</p></td>
</tr>
</tbody>
</table>