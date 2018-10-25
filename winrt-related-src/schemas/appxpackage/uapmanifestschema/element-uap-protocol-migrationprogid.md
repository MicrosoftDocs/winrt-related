---
author: laurenhughes
ms.assetid: d144eb77-9888-4fb9-93cb-23308235acc5
title: rescap3:MigrationProgId
description: Contains a migration Prog Id string for protocols and file type associations.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:MigrationProgId


## Description
Contains a migration Prog Id string for protocols and file type associations.


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
<dt><a href="element-uap-protocol.md">&lt;uap:Protocol&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-rescap3-migrationprogids.md">&lt;rescap3:MigrationProgIds&gt;</a></dt>
<dd><b>&lt;rescap3:MigrationProgId&gt;</b></dd>
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
<rescap3:MigrationProgId> 
    An alphanumeric string separated by a period between 1 and 39 characters in length, e.g. Foo.Bar or Foo.Bar.1
</rescap3:MigrationProgId>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3</p></td>
</tr>
</tbody>
</table>