---
author: mcleanbyron
ms.assetid: a20641e1-138e-4777-a177-a404f96eeed9
title: com:TypeLib (in ComInterface/Interface)
description: A type library for an interface.
ms.author: mcleans
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:TypeLib (in ComInterface/Interface)

## Description
A type library for an interface.

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
<dd>
<dl>
<dt><a href="element-com-interface.md">&lt;com:Interface&gt;</a></dt>
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
</dd>
</dl>



## Syntax
```syntax
<com:TypeLib
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. 
    VersionNumber? = One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a >
</com:TypeLib>
```

## Key
`?`    optional (zero or one) 

## Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id      | The type library ID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| VersionNumber | The version of the type library. | One to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters, e.g., 1.5a | No |

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
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>