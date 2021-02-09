---
description: Represents...
title: uap10:Content
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 02/06/2020
---

# uap10:Content

Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package. If enabled, Windows will perform run time checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-packageintegrity.md">&lt;uap10:PackageIntegrity&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-content.md">&lt;uap10:Content&gt;</a></dt>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax

```xml
<uap10:PackageIntegrity>

  <!-- Child elements -->
  <uap10:Content Enforcement="on" />

</uap10:PackageIntegrity>
```

## Attributes and Elements

### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enforcement</strong></td>
<td><p>Indicates whether Windows will enforce run time package integrity checks on the entire contents of the package.</p>
</td>
<td><p>One of the following string values: "on", "off", or "default". The value "default" currently has the same behavior as "off".</p></td>
<td><p>Yes</p></td>
<td><p>"off"</p></td>
</tr>
</tbody>
</table>

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-uap10-packageintegrity.md">uap10:PackageIntegrity</a> </td>
<td><p>Specifies the level of run time package integrity checks and remediation for the package.</p></td>
</tr>
</tbody>
</table>

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |

