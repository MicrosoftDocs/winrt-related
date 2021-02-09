---
description: StoreManifest schema for Windows 8.1 and earlier
Search.Product: eADQiWindows 10XVcnh
title: StoreManifest
ms.assetid: 01d2ebcb-9da0-4bcc-9eb4-c284810f894b


keywords: windows 10, uwp, schema, storemanifest


ms.topic: reference
ms.date: 04/05/2017
---

# StoreManifest


Root node for the StoreManifest schema (for Windows 8.1 and earlier).

## Element hierarchy

**&lt;StoreManifest&gt;**

## Syntax

``` syntax
<StoreManifest>

  <!-- Child elements -->
  ProductFeatures?

</StoreManifest>
```

### Key

`?`   optional (zero or one)

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
<td><a href="element-productfeatures.md">ProductFeatures</a> </td>
<td><p>The ProductFeatures element is the container for all existing and future product features that will be configured through the StoreManifest XML file.</p></td>
</tr>
</tbody>
</table>

 

### Parent Elements

This outermost (document) element may not be contained by any other elements.

## Remarks

For UWP apps, see [StoreManifest schema](../storemanifestschema2015/schema-root.md).

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2010/StoreManifest` |

 

 
