---

title: uap7:Capability
description: Declares a capability.

ms.date: 10/03/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap7:Capability

## Description
Declares a capability required by a package.

## Element hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;uap7:Capability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap7:Capability Name = "globalMediaControl" | "gazeInput" />
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the capability. | This attribute can have one of the following values: <ul><li>globalMediaControl</li><li>gazeInput</li></ul> | Yes |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/7</p></td>
</tr>
</tbody>
</table>