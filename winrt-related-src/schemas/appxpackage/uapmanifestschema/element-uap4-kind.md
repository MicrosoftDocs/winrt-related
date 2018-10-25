---
author: laurenhughes
ms.assetid: 1f37ad76-f29e-433f-83b5-6af02d723b59
title: uap4:Kind
description: Specifies the Kind value.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:Kind

## Description
Specifies the Kind value. 

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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-filetypeassociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap4-kindmap.md">&lt;uap4:KindMap&gt;</a></dt>
<dd><b>&lt;uap4:Kind&gt;</b></dd>
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
<uap4:Kind Value = A string value. See the Attributes table for more details.>
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Value | The Kind value. | Must be one of the following values: <ul><li>calendar</li><li>communication</li><li>contact</li><li>document</li><li>email</li><li>feed</li><li>folder</li><li>game</li><li>instantmessage</li><li>journal</li><li>link</li><li>movie</li><li>music</li><li>note</li><li>picture</li><li>program</li><li>recordedtv</li><li>searchfolder</li><li>task</li><li>unknown</li><li>video</li><li>webhistory</li></ul> | Yes |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>