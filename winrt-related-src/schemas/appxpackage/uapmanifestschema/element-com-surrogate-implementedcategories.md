---

ms.assetid: 194c0da4-ada9-4107-b5dd-3bf609f328b2
title: com:ImplementedCategories (in SurrogateServer/Class)
description: Specifies categories implemented by the class.

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---

# com:ImplementedCategories (in SurrogateServer/Class)

## Description
Specifies categories implemented by the class.

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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-comserver.md">&lt;com:ComServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogateserver.md">&lt;com:SurrogateServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogateserver-class.md">&lt;com:Class&gt;</a></dt>
<dd><b>&lt;com:ImplementedCategories&gt;</b></dd>
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
</dd>
</dl>


## Syntax
```syntax
<com:ImplementedCategories>  
  <!-- Child elements -->
  ImplementedCategory{1,1000}
</com:ImplementedCategories>
```

## Key
`{}`   specific range of occurrences 

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [ImplementedCategory](element-com-surrogate-implementedcategory.md) | Indicates that the class has implemented the specified category. |

## Remarks

## Examples

## Requirements
|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |