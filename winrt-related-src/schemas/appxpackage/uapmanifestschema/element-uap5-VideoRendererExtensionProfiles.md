---
author: laurenhughes
title: uap5:VideoRendererExtensionProfiles
description: Contains a list of video renderer profiles.
ms.author: lahugh
ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:VideoRendererExtensionProfiles

## Description
Contains a list of video renderer profiles.

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
<dd><b>&lt;uap5:VideoRendererExtensionProfiles&gt;</b></dd>
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
<uap5:VideoRendererExtensionProfiles>   
  <!-- Child elements -->
  uap5:VideoRendererExtensionProfile{0,1000}
</uap5:VideoRendererExtensionProfiles>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes
None


### Child Elements

| Child Element | Description |
|---------------|-------------|
| [VideoRendererExtensionProfile](element-uap5-VideoRendererExtensionProfile.md) | Specifies a video renderer profile. |


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