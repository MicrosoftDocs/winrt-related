---
Description: Certificates (Windows 10)
MS-HAID: UapManifestSchema.element\_Certificates
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Certificates (Windows 10)
ms.assetid: 378edcd3-b9ef-46db-9a56-94470451829e
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# Certificates (Windows 10)


Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd><b>&lt;Certificates&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
## Syntax

``` syntax
<Certificates>

  <!-- Child elements -->
  Certificate{0,100},
  TrustFlags?,
  SelectionCriteria?

</Certificates>
```

### Key

`?`   optional (zero or one)
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
<td>[Certificate](element-certificate.md)</td>
<td><p>A certificate for use with the package and placed in the system certificate stores.</p></td>
</tr>
<tr class="even">
<td>[SelectionCriteria](element-selectioncriteria.md)</td>
<td><p>Defines selection criteria for the certificates defined for the package.</p></td>
</tr>
<tr class="odd">
<td>[TrustFlags](element-trustflags.md)</td>
<td><p>Indicates whether the certificates for the package are exclusive to the package.</p></td>
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
<td>[Extension (in type: CT_PackageExtensions)](element-extension.md)</td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
</tbody>
</table>

 

## See also


**Tasks**
[Working with certificates](https://msdn.microsoft.com/library/windows/apps/hh465044)

**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



