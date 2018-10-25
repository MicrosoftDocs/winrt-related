---
author: laurenhughes
ms.assetid: 0a5b6804-915b-43b4-87ba-56a0018e58ad
title: uap2:SupportedVerbs
description: Contains verbs for a file context menu.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap2:SupportedVerbs

## Description
Contains verbs for a file context menu.

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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-FileTypeAssociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;uap2:SupportedVerbs&gt;</b></dd>
</dl>
</dd>
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
<uap2:SupportedVerbs>
  <!-- Child elements -->
  uap2:Verb{1,10000}
</uap2:SupportedVerbs>

```

### Key
`{}` specific range of occurrences


## Child Elements
| Child Element | Description |
|---------------|-------------|
| [Verb](element-uap2-verb.md) | Defines the verbs associated with a file context menu and enables Windows Desktop Bridge apps to use ddeexec to launch. |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/2</p></td>
</tr>
</tbody>
</table>