---
description: Declares the minimum operating system and software requirements that must exist for the package to be applicable to the system (Windows 8).
Search.Product: eADQiWindows 10XVcnh
title: Prerequisites (Windows 8 package schema)
ms.assetid: 93b13906-9c63-46d0-8659-0f382ce8f477


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Prerequisites (package schema for Windows 8)


Declares the minimum operating system and software requirements that must exist for the package to be applicable to the system.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Prerequisites&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Prerequisites>

  <!-- Child elements -->
  ( OSMinVersion
  & OSMaxVersionTested
  )

</Prerequisites>
```

### Key

`&`   interleave connector (may occur in any order)

## Attributes and Elements


### Attributes

None.

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
<td><a href="element-osmaxversiontested.md">OSMaxVersionTested</a> </td>
<td><p>This should be filled in by the developer with the highest version of Windows that the package was tested on. This field is required. Windows will not block installation of the package on versions of the OS higher than the value provided in this field. When an app is executed, Windows will compare this field to the actual OS version. If the value provided in this field is less than the current OS version, Windows may provide behavior compatible with the highest tested OS version for some or all APIs. If the value provided in this field is greater than or equal to the current OS version, Windows will not apply any compatibility changes to APIs.</p></td>
</tr>
<tr class="even">
<td><a href="element-osminversion.md">OSMinVersion</a> </td>
<td><p>The minimum version of the operating system that the package requires.</p></td>
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
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
<Prerequisites>
  <OSMinVersion>6.2</OSMinVersion>
  <OSMaxVersionTested>6.2</OSMaxVersionTested>
</Prerequisites>
```

## Requirements

|               |    Value                                                         |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



