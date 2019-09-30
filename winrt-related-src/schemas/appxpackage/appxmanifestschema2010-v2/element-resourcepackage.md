---
Description: Indicates whether the package is a resource package. 
Search.Product: eADQiWindows 10XVcnh
title: ResourcePackage
ms.assetid: 51cabad7-a2eb-4fa3-ab52-59298555aefb
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# ResourcePackage

Indicates whether the package is a resource package. A resource package can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a resource.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;ResourcePackage&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ResourcePackage>

  boolean

</ResourcePackage>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

None.

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-properties.md">Properties</a> </td>
<td><p>Defines additional metadata about the package including attributes that describe how the package appears to users.</p>
<div class="alert">
<strong>Note</strong>  You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely “|” and “all”, due to which Windows fails to create the AppContainer profile for the package . Use this reference for [troubleshooting](https://msdn.microsoft.com/library/windows/desktop/hh973484) if you get an error.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

## Remarks

If **ResourcePackage** is set to **true**, the manifest performs these semantic checks, which aren't enforced in the schema. A manifest that violates these semantic checks will just fail to validate via the [Packaging APIs](https://msdn.microsoft.com/library/windows/desktop/hh446766).

-   A resource package can't define the [**Dependencies**](element-dependencies.md), [**Capabilities**](appxmanifestschema/../element-capabilities.md), [**Applications**](https://msdn.microsoft.com/library/windows/apps/br211417), [**Extensions**](element-extensions.md), and [**Framework**](element-framework.md) elements.
-   A resource package can't define [**Package\\Identity\\@ProcessorArchitecture**](https://msdn.microsoft.com/library/windows/apps/br211441), so it always defaults to **neutral**.
-   [**Resources\\Resource**](element-resource.md) elements for a resource package can only define one type of attribute, for example, only **Language** or **Scale**.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



