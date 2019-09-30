---
author: mcleanbyron
ms.assetid: 13623913-5515-41e8-929e-e57d8aa38635
title: rescap3:MigrationProgIds
description: Contains Migration Prog Ids for protocols and file type associations.
ms.author: mcleans
ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:MigrationProgIds


## Description
Contains [programmatic identifier (ProgID)](https://docs.microsoft.com/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations.


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
<dd><b>&lt;rescap3:MigrationProgIds&gt;</b></dd>
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
<rescap3:MigrationProgIds> 
  <!-- Child elements -->
  rescap3:MigrationProgId{0,10000} 
</rescap3:MigrationProgIds>
```

### Key
`{}` specific range of occurrences

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [MigrationProgId](element-rescap3-migrationprogid.md) | Contains a migration Prog Id string for protocols and file type associations. | 

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