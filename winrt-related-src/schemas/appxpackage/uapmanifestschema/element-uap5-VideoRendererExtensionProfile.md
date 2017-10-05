---
author: laurenhughes
title: uap5:VideoRendererExtensionProfile
description: Specifies a video renderer profile.
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:VideoRendererExtensionProfile

## Description
Specifies a video renderer profile.

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
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-VideoRendererEffect.md">&lt;uap5:VideoRendererEffect&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-VideoRendererExtensionProfiles.md">&lt;uap5:VideoRendererExtensionProfiles&gt;</a></dt>
<dd><b>&lt;uap5:VideoRendererExtensionProfile&gt;</b></dd>
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
</dd>
</dl>

## Syntax
```syntax
<uap5:VideoRendererExtensionProfile Profile = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. />
```

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Profile | Specifies a renderer profile. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

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
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>