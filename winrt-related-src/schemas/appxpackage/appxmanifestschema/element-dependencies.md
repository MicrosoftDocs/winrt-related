---
description: Declares other packages that a package depends on to complete its software.
Search.Product: eADQiWindows 10XVcnh
title: Dependencies (package schema for Windows 8)
ms.assetid: a1e745c9-a804-42cf-a107-7fb860cc8289


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Dependencies (package schema for Windows 8)


Declares other packages that a package depends on to complete its software.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Dependencies&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Dependencies>

  <!-- Child elements -->
  PackageDependency{1,128}

</Dependencies>
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
<td><a href="element-packagedependency.md">PackageDependency</a> </td>
<td><p>Declares a dependency on another package that is marked as a framework package.</p></td>
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

Dependencies must be explicitly defined. If a dependency cannot be resolved, deployment of the package fails. By default, a package cannot take a dependency on another package if the dependency package is not declared to be a framework package. Set [**Framework**](element-framework.md) to **true** to declare a framework package.

## Examples

```XML
<Dependencies>
    <PackageDependency Name="Microsoft.WinJS.1.0"
      Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
      MinVersion="1.0.0.0"/>    
</Dependencies>
```

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/manifest` |

 

 



