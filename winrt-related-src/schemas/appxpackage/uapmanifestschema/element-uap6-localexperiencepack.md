---
author: mcleanbyron
title: uap6:LocalExperiencePack
description: This extension provides a means to deliver translated app resources.
ms.author: mcleans
ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap6:LocalExperiencePack

## Description
This extension provides a means to deliver translated app resources.

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
<dt><a href="element-uap6-extension.md">&lt;uap6:Extension&gt;</a></dt>
<dd><b>&lt;uap6:LocalExperiencePack&gt;</b></dd>
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
<uap6:LocalExperiencePack Language =  A string that represents language and locale containing four characters separated by a dash, e.g., "en-us" or "fr-fr" />
```

### Key
`?`   optional (zero or one)

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Language | The language and locale identifier. For example, "en-us" represents English language used in the United States. | A string that represents language and locale containing four characters separated by a dash, e.g., "en-us" or "fr-fr" | No |

### Child Elements
None

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/6</p></td>
</tr>
</tbody>
</table>