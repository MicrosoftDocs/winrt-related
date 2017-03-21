---
author: laurenhughes
ms.assetid: a3735612-102e-47e2-ba08-a53259edc60a
title: com:TypeLib (in Package/Extensions)
description: Registers a type library.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---


# com:TypeLib (in Package/Extensions)

## -description
Registers a type library.

## -element-hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-package-cominterface.md">&lt;ComInterface&gt;</a></dt>
<dd><b>&lt;TypeLib&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>



## -syntax
```syntax
<TypeLib
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >

  <!-- Child elements -->
  Version{1,1000}  
</TypeLib>
```

## -key
`{}`   specific range of occurrences 

## -attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The ID of the type library. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## -child-elements
 
| Child Element | Description |
|---------------|-------------|
| [Version](element-com-package-version.md) | Version number and additional information about the type library. |

## -remarks

## -examples

## -requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>