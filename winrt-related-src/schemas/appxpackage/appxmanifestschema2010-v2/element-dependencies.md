---
Description: Dependencies
MS-HAID: AppxManifestSchema2010\_v2.element\_Dependencies
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Dependencies
ms.assetid: a1e745c9-a804-42cf-a107-7fb860cc8289
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# Dependencies




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
<td>[PackageDependency](element-packagedependency.md)</td>
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
<td>[Package](element-package.md)</td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Dependencies must be explicitly defined. If a dependency cannot be resolved, deployment of the package fails. By default, a package cannot take a dependency on another package if the dependency package is not declared to be a framework or resource package. Set [**Framework**](element-framework.md) to **true** to declare a framework package and [**ResourcePackage**](element-resourcepackage.md) to **true** to declare a resource package.

## Examples

```XML
<Dependencies>
    <PackageDependency Name="Microsoft.WinJS.1.0"
      Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US"
      MinVersion="1.0.0.0"/>    
</Dependencies>
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
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



