---
author: laurenhughes
ms.assetid: 6532bd08-d33b-49c1-9f8a-477d32b83464
title: uap4:LoopbackAccessRules
description: Contains rules for a loopback filter that enables communication between an app and a service.
ms.author: lahugh
ms.date: 05/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:LoopbackAccessRules

## Description
Contains rules for a loopback filter that enables communication between an app and a service.

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
<dd><b>&lt;uap4:LoopbackAccessRules&gt;</b></dd>
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
<uap4:LoopbackAccessRules>
  <!-- Child elements -->
  uap4:Rule{0,1000}
</uap4:LoopbackAccessRules>                   
```

### Key
`{}` specific range of occurrences

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Rule](element-uap4-rule.md) | Defines rules for inbound and outbound loopback connections. |

## Remarks
Loopback connections are supported only for TCP connections. Note that the UDP protocol is not supported.

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