---
Description: Enables your package manifest to reference content outside the package, in a specific location on disk, for sparse package scenarios.
title: uap10:AllowExternalContent
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/22/2020
---

# uap10:AllowExternalContent

Enables your package manifest to reference content outside the package, in a specific location on disk, for [sparse package](https://docs.microsoft.com/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps) scenarios.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-properties.md">&lt;Properties&gt;</a></dt>
<dd><b>&lt;uap10:AllowExternalContent&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

```syntax
<uap10:AllowExternalContent>

  Boolean

</uap10:AllowExternalContents>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements

### Attributes

None.

### Child Elements

None.

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

The **uap10:AllowExternalContent** element contains a Boolean value. For more information about the use of the element, see [Grant identity to non-packaged desktop apps](https://docs.microsoft.com/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps).

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
