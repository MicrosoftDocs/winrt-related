---
Description: Defines the root element of the app package block map.
Search.Product: eADQiWindows 10XVcnh
title: BlockMap
ms.assetid: 75eed334-6c80-4eb3-8776-fc34d7aa5357


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# BlockMap




Defines the root element of the app package block map. The [**BlockMap**](element-blockmap.md) element specifies the algorithm that is used to compute cryptographic hashes and contains a sequence of [**File**](element-file.md) child elements that are associated with each file that is stored in the package.

## Element hierarchy

**&lt;BlockMap&gt;**

## Syntax

``` syntax
<BlockMap HashMethod = anyURI >

  <!-- Child elements -->
  File+

</BlockMap>
```

### Key

`+`   required (one or more)

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
<td><strong>HashMethod</strong></td>
<td><p>The <strong>HashMethod</strong> attribute is used to compute the cryptographic hash for each data block.</p></td>
<td>anyURI</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-file.md">File</a> </td>
<td><p>Represents a file contained in the package.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

The **HashMethod** attribute specifies the method for computing cryptographic hash of each block of data that is described in the block map. While the schema allows any Uniform Resource Identifier (URI) value to be specified, the value must be a well-known URI defined by World Wide Web Consortium (W3C) for a hash algorithm. Specifically, the following algorithm identifiers are currently supported:

| Algorithm | Identifier                                      |
|-----------|-------------------------------------------------|
| SHA2-256  | <http://www.w3.org/2001/04/xmlenc#sha256>       |
| SHA2-384  | <http://www.w3.org/2001/04/xmldsig-more#sha384> |
| SHA2-512  | <http://www.w3.org/2001/04/xmlenc#sha512>       |

 

App packages that are created by Visual Studio or the [app packager (MakeAppx.exe)](/windows/win32/appxpkg/make-appx-package--makeappx-exe-) utility use the <http://www.w3.org/2001/04/xmlenc#sha256> hash algorithm by default.

**Note**  When signing the package, the **BlockMap**’s **HashMethod** attribute must also match the file digest hash algorithm (“/fd” parameter) specified to SignTool. For more info, see [To sign the package using SignTool](/windows/win32/appxpkg/make-appx-package--makeappx-exe-).

 

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/blockmap` |


 

 