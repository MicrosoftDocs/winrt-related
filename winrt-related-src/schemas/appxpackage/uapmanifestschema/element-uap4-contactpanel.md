---
author: laurenhughes
ms.assetid: 76e05698-cd02-451b-b2b7-bb79169ea082
title: uap4:ContactPanel
description: Enables the contacts panel in a Windows app.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:ContactPanel

## Description
Enables the contacts panel in a Windows app.

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
<dt><a href="element-uap4-extension.md">&lt;uap4:Extension&gt;</a></dt>
<dd><b>&lt;uap4:ContactPanel&gt;</b></dd>
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
<uap4:ContactPanel SupportsUnknownContacts = Boolean. >               
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| SupportsUnknownContacts | True if the contact panel supports unknown contacts, otherwise false. | Boolean. | Yes |

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