---

ms.assetid: e257f16b-91a1-4ce1-95c5-d2d80e13ad3c
title: Resources
description: Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, optional bundle 
---

# Resources

## Description
Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains.

## Element Hierarchy
<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-optionalbundle.md">&lt;OptionalBundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-optionalbundle-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Resources&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Resources>
  <!-- Child elements -->
  Resource{1,200}
</Resources>
```

### Key
`{}`  specific range of occurrences

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [Resource](element-optionalbundle-resource.md) | Declares language, resolution scale, and DirectX feature level for a resource in the package. |

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