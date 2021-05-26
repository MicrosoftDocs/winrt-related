---

ms.assetid: 7dbfa1d3-68fe-4021-93db-d8948a6f4435
title: com:TypeLib
description: Registers a type library.

ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:TypeLib 

## Description
Registers a type library.

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
<dt><a href="element-com-cominterface.md">&lt;com:ComInterface&gt;</a></dt>
<dd><b>&lt;com:TypeLib&gt;</b></dd>
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
<com:TypeLib
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. >

  <!-- Child elements -->
  Version{1,1000}  
</com:TypeLib>
```

## Key
`{}`   specific range of occurrences 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id      | The type library ID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Child Elements
 
| Child Element | Description |
|---------------|-------------|
| [Version](element-com-version.md) | Version number and additional information about the type library. |


## Remarks

## Examples

## Requirements
|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |