---
author: laurenhughes
ms.assetid: 3e8f1959-50fd-4183-9fb7-ee30a2b020a1
title: Resource
description: Declares language, resolution scale, and DirectX feature level for a resource in the package.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, optional bundle 
---

# Resource

## Description
Declares language, resolution scale, and DirectX feature level for a resource in the package.

## Element Hierarchy
<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-optionalbundle.md">&lt;OptionalBundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-optionalbundle-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-optionalbundle-resources.md">&lt;Resources&gt;</a></dt>
<dd><b>&lt;Resource&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
``` syntax
<Resource Language?       = language
          Scale?          = "100" | "120" | "140" | "150" | "160" | ...
          DXFeatureLevel? = "dx9" | "dx10" | "dx11" />
```

### Key
`?`   optional (zero or one) 

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DXFeatureLevel | The [DirectX feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) for the resource. | One of the following: "dx9", "dx10", "dx11" | No |
| Language | The language for the resource. The syntax of this attribute is defined by the IETF's [BCP47: Tags for Identifying Languages](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). | language | No |
| Scale | The resolution scale for the resource. | One of the following: "100", "120", "125", "140", "150", "160", "180", "200", "220", "225", "240", "250", "300", "400", "500" | | No |

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
<td><p>http://schemas.microsoft.com/appx/2016/bundle</p></td>
</tr>
</tbody>
</table>