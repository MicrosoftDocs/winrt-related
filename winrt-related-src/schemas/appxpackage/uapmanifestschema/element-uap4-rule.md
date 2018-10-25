---
author: laurenhughes
ms.assetid: 7ec485fd-ecd8-49f3-82cd-fbf1e0656222
title: uap4:Rule
description: Defines rules for inbound and outbound loopback connections.
ms.author: lahugh
ms.date: 05/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, extension 
---

# uap4:Rule

## Description
Defines rules for inbound and outbound loopback connections.

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
<dd>
<dl>
<dt><a href="element-uap4-loopbackaccessrules.md">&lt;uap4:LoopBackAccessRules&gt;</a></dt>
<dd><b>&lt;uap4:Rule&gt;</b></dd>
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
<uap4:Rule Direction = String value. This can either be "in" or "out".
           PackageFamilyName = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >                  
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Direction | Specifies whether the connection will be inbound or outbound over loopback. | String value. This can either be "in" or "out". | Yes |
| PackageFamilyName | The package family name of the app to connect to. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |

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