---
Description: Declares a package extensibility point of type windows.certificates.
Search.Product: eADQiWindows 10XVcnh
title: Certificates (Windows 10)
ms.assetid: 378edcd3-b9ef-46db-9a56-94470451829e


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
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
<td><a href="element-certificate.md">Certificate</a> </td>
<td><p>A certificate for use with the package and placed in the system certificate stores.</p></td>
</tr>
<tr class="even">
<td><a href="element-selectioncriteria.md">SelectionCriteria</a> </td>
<td><p>Defines selection criteria for the certificates defined for the package.</p></td>
</tr>
<tr class="odd">
<td><a href="element-trustflags.md">TrustFlags</a> </td>
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
<td><a href="element-extension.md">Extension (in type: CT_PackageExtensions)</a> </td>
<td><p>Declares an extensibility point for the package.</p></td>
</tr>
</tbody>
</table>

 

## See also


**Tasks**
[Working with certificates](/previous-versions/windows/apps/hh465044(v=win.10))

**Concepts**
[App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 