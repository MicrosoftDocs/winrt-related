---
author: mcleanbyron
ms.assetid: 532ff2d5-86b6-4c61-a80f-1e9b0dde7c96
title: com:ComInterface (in Package/Extensions)
description: Declares a package extension point of type windows.comInterface.
ms.author: mcleans
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:ComInterface (in Package/Extensions)

## Description
Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: **Interface**, **ProxyStub**, or **TypeLib**.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;ComInterface&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<ComInterface>
  <!-- Child elements -->
  ( ProxyStub{0,1000},
  Interface{0,10000},
  TypeLib{0,1000}
  )  
</ComInterface>
```

## Key
`{}`   specific range of occurrences

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [ProxyStub](element-com-package-proxystub.md) | Registers a proxy stub. |
| [Interface](element-com-package-interface.md) | Registers new COM Interfaces. |
| [TypeLib](element-com-package-typelib.md) | Registers a type library. |

## Remarks
The **comInterface** extension can be under the Application/Extensions/Extension manifest element, or under the Package/Extensions/Extension manifest element. There is no functional difference between these two options, but both placements have different advantages.

If the extension is under Application/Extensions/Extension, you can improve the readability of the manifest by keeping interface registrations near the class registrations that implement them. However, if you place the extension under Package/Extensions/Extension, you won't need to determine which Application to use for each interface. It's possible to use multiple **comInterface** extensions in either Application/Extensions/Extension or Package/Extensions/Extension, but this is neither recommended nor necessary.

> [!NOTE]
> Any registrations in **comInterface** that depend on another registration (e.g. an **Interface** references a **ProxyStub** and/or a **TypeLib**) must be in the same **comInterface** extension. 

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
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>