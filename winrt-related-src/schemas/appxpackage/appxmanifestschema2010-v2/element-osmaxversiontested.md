---
description: Represents the highest version of Windows that the package was tested on.
Search.Product: eADQiWindows 10XVcnh
title: OSMaxVersionTested
ms.assetid: 2f820978-5080-427d-b364-08951afae9ee


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# OSMaxVersionTested

This should be filled in by the developer with the highest version of Windows that the package was tested on. This field is required. Windows will not block installation of the package on versions of the OS higher than the value provided in this field. When an app is executed, Windows will compare this field to the actual OS version. If the value provided in this field is less than the current OS version, Windows may provide behavior compatible with the highest tested OS version for some or all APIs. If the value provided in this field is greater than or equal to the current OS version, Windows will not apply any compatibility changes to APIs.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-prerequisites.md">&lt;Prerequisites&gt;</a></dt>
<dd><b>&lt;OSMaxVersionTested&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<OSMaxVersionTested>

  A version string in duo notation (major.minor) or trio notation (major.minor.appversion).

</OSMaxVersionTested>
```

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
<td><a href="element-prerequisites.md">Prerequisites</a> </td>
<td><p>Declares the minimum operating system and software requirements that must exist for the package to be applicable to the system.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



