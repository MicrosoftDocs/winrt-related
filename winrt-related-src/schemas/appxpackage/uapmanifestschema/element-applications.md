---
description: Represents one or more apps that comprise the package.
Search.Product: eADQiWindows 10XVcnh
title: Applications (Windows 10)
ms.assetid: ad9e07fc-ba58-4465-b3fa-b330ba149f92


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Applications (Windows 10)


Represents one or more apps that comprise the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Applications&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Applications>

  <!-- Child elements -->
  Application{1,100}

</Applications>
```

### Key

`{}`   specific range of occurrences
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
<td><a href="element-application.md">Application</a> </td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
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

 

## Remarks

You can use the **Applications** element to specify one or more apps for the package. Note that although each package can contain one or more apps, packages that contain multiple apps won't pass the Store certification process.

## Requirements

|   | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 



