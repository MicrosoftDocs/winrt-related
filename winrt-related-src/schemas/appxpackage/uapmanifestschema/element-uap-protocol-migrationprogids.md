---

ms.assetid: 5872b49b-5572-4198-8765-775c7a5a36fc
title: rescap3:MigrationProgIds
description: "Learn more about: rescap3:MigrationProgIds"

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:MigrationProgIds


## Description
Contains Migration Prog Ids for protocols and file type associations.


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
| [MigrationProgId](element-uap-protocol-migrationprogid.md) | Contains a migration Prog Id string for protocols and file type associations. | 

## Remarks

## Examples

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
