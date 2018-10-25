---
author: laurenhughes
ms.assetid: 6997bc14-c33f-4a88-aec1-21c1ddd5a8f2
title: uap4:Capability
description: Declares a capability required by a package.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:Capability

## Description
Declares a capability required by a package.

## Element hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;uap4:Capability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap4:Capability Name = "offlineMapsManagement" | "userDataTasks"
</uap4:Capability>
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the capability. | This attribute can have one of the following values: <ul><li>offlineMapsManagement</li><li>userDataTasks</li></ul> | Yes |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/4</p></td>
</tr>
</tbody>
</table>