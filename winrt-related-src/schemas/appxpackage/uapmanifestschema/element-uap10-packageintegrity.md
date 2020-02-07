---
Description: Indicates whether Windows will enforce runtime package integrity checks on the package.
title: uap10:PackageIntegrity
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 02/06/2020
---

# uap10:PackageIntegrity

Specifies the level of run time package integrity checks and remediation for the package. If enabled, Windows will perform runtime checks and initiate a package remediation and repair workflow before launching the app if it detects a tampered or corrupt package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;uap10:PackageIntegrity&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

```syntax
<uap10:PackageIntegrity>

  <!-- Child elements -->
  ( uap10:Content? )

</uap10:PackageIntegrity>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-uap10-content.md">uap10:Content</a> </td>
<td><p>Optional. Indicates whether Windows will enforce runtime package integrity checks on the entire contents of the package.</p></td>
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
<td><a href="element-properties.md">Properties</a> </td>
<td><p>Defines additional metadata about the package including attributes that describe how the package behaves.</p></td>
</tr>
</tbody>
</table>

## Remarks

If you include a **uap10:PackageIntegrity** element without a child [uap10:Content](element-uap10-content.md) element, Windows will not enforce runtime package integrity checks.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/10</p></td>
</tr>
</tbody>
</table>
